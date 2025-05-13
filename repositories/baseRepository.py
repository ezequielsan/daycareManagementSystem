import csv
import os
import zipfile
from typing import Generic, List, Type, TypeVar

from pydantic import BaseModel

from utils.logger import logger

T = TypeVar('T', bound=BaseModel)


class BaseRepository(Generic[T]):
    def __init__(self, csv_path: str, model_class: Type[T]):
        self.csv_path = csv_path
        self.model_class = model_class

    def read_all(self) -> List[T]:
        try:
            with open(self.csv_path, mode='r', newline='') as file:
                reader = csv.DictReader(file)
                return [self.model_class(**row) for row in reader]
        except FileNotFoundError:
            return []

    def write_all(self, data: List[T]) -> None:
        if not data:
            dummy_instance = self._create_dummy_instance()
            fieldnames = dummy_instance.dict().keys()
        else:
            fieldnames = data[0].dict().keys()

        with open(self.csv_path, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for item in data:
                writer.writerow(item.dict())

    def get_by_id(self, entity_id: int) -> T:
        entities = self.read_all()
        for entity in entities:
            if entity.id == entity_id:
                return entity
        return None

    def create(self, entity: T) -> T:
        entities = self.read_all()
        if any(e.id == entity.id for e in entities):
            logger.error(
                f'Failed to create {self.model_class.__name__}: Duplicate ID {entity.id}'
            )
            return None

        entities.append(entity)
        self.write_all(entities)
        logger.info(
            f'Created new {self.model_class.__name__} with ID {entity.id}'
        )
        return entity

    def update(self, entity_id: int, new_entity: T) -> T:
        entities = self.read_all()
        for index, entity in enumerate(entities):
            if entity.id == entity_id:
                if new_entity.id != entity_id:
                    new_entity.id = entity_id
                entities[index] = new_entity
                self.write_all(entities)
                logger.info(
                    f'Updated {self.model_class.__name__} with ID {entity_id}'
                )
                return new_entity
        logger.warning(
            f'Failed to update {self.model_class.__name__}: ID {entity_id} not found'
        )
        return None

    def delete(self, entity_id: int) -> bool:
        entities = self.read_all()
        filtered_entities = [
            entity for entity in entities if entity.id != entity_id
        ]

        if len(entities) == len(filtered_entities):
            logger.warning(
                f'Failed to delete {self.model_class.__name__}: ID {entity_id} not found'
            )
            return False

        self.write_all(filtered_entities)
        logger.info(f'Deleted {self.model_class.__name__} with ID {entity_id}')
        return True

    def _create_dummy_instance(self) -> T:
        logger.debug(
            f'Creating dummy instance for {self.model_class.__name__}'
        )
        return self.model_class(id=0)

    def count(self) -> int:
        try:
            with open(self.csv_path, mode='r', newline='') as file:
                reader = csv.DictReader(file)
                count = sum(1 for _ in reader)
                logger.info(
                    f'Counted {count} {self.model_class.__name__}(s) in {self.csv_path}'
                )
                return count
        except FileNotFoundError:
            logger.warning(
                f'File {self.csv_path} not found for counting {self.model_class.__name__}(s)'
            )
            return 0

    def zip_csv(self) -> str:
        zip_path = self.csv_path.replace('.csv', '.zip')
        csv_filename = os.path.basename(self.csv_path)
        with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
            zipf.write(self.csv_path, arcname=csv_filename)
        logger.info(f'Zipped {self.csv_path} to {zip_path}')
        return zip_path
    
    def export_to_xml(self) -> str:
        xml_path = self.csv_path.replace('.csv', '.xml')
        entity_tag = self.model_class.__name__.lower()
        with open(self.csv_path, mode='r', newline='') as csv_file:
            reader = csv.DictReader(csv_file)
            with open(xml_path, mode='w') as xml_file:
                xml_file.write('<data>\n')
                for row in reader:
                    xml_file.write(f'  <{entity_tag}>\n')
                    for key, value in row.items():
                        xml_file.write(f'    <{key}>{value}</{key}>\n')
                    xml_file.write(f'  </{entity_tag}>\n')
                xml_file.write('</data>')
        logger.info(f'Exported {self.csv_path} to {xml_path}')
        return xml_path
