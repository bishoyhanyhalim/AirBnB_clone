#!/usr/bin/python3
import json

class FileStorage:
    __file_path = "file.json"
    __objects={}

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        objects = {}
        for name, obj in FileStorage.__objects.items():
            objects[name] = obj.to_dict()
        with open(FileStorage.__file_path, 'w') as fl:
            json.dump(objects, fl)

    def reload(self):
        from models.base_model import BaseModel
        class_mapping = {
            'BaseModel': BaseModel
        }

        try:
            with open(FileStorage.__file_path, 'r') as fl:
                objects = json.load(fl)
                for key, object_info in objects.items():
                    cls_name, id = key.split('.')
                    if cls_name in class_mapping:
                        cls = class_mapping[cls_name]
                        instance = cls(**object_info)
                    FileStorage.__objects[key] = instance
        except FileNotFoundError:
            pass
