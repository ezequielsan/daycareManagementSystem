import csv
import os
from typing import Type, List, Any

def read_data_csv(path_csv: str, model_class: Type) -> List:
    if not os.path.exists(path_csv):
        print(f"File {path_csv} does not exist.")
        return []
    
    with open(path_csv, mode='r', newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        return [model_class(**row) for row in reader]

def write_data_csv(path_csv: str, data: List[Any]) -> None:
    if data:
        fieldnames = data[0].dict().keys()
        with open(path_csv, mode="w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for item in data:
                writer.writerow(item.dict())
