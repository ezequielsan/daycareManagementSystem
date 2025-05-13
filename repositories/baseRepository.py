import csv
from typing import List, TypeVar, Type, Generic, Any
from pydantic import BaseModel
import zipfile
import os

T = TypeVar('T', bound=BaseModel)

class BaseRepository(Generic[T]):
    def __init__(self, csv_path: str, model_class: Type[T]):
        self.csv_path = csv_path
        self.model_class = model_class
    
    def read_all(self) -> List[T]:
        try:
            with open(self.csv_path, mode="r", newline="") as file:
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
            
        with open(self.csv_path, mode="w", newline="") as file:
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
            return None 
        
        entities.append(entity)
        self.write_all(entities)
        return entity
    
    def update(self, entity_id: int, new_entity: T) -> T:
        entities = self.read_all()
        for index, entity in enumerate(entities):
            if entity.id == entity_id:
                if new_entity.id != entity_id:
                    new_entity.id = entity_id
                entities[index] = new_entity
                self.write_all(entities)
                return new_entity
        return None 
    
    def delete(self, entity_id: int) -> bool:
        entities = self.read_all()
        filtered_entities = [entity for entity in entities if entity.id != entity_id]
        
        if len(entities) == len(filtered_entities):
            return False 
            
        self.write_all(filtered_entities)
        return True
    
    def _create_dummy_instance(self) -> T:
        return self.model_class(id=0)

    def count(self) -> int:
        try:
            with open(self.csv_path, mode="r", newline="") as file:
                reader = csv.DictReader(file)
                return sum(1 for _ in reader)
        except FileNotFoundError:
            return 0

    def zip_csv(self) -> str:
        zip_path = self.csv_path.replace('.csv', '.zip')
        csv_filename = os.path.basename(self.csv_path)
        with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zipf:
            zipf.write(self.csv_path, arcname=csv_filename)
        return zip_path