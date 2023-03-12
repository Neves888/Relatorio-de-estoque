from inventory_report.importer.importer import Importer
from re import search
import json


class JsonImporter(Importer):
    @classmethod
    def import_data(cls, path):
        if search(r".json$", path):
            with open(path, "r") as file:
                return list(json.load(file))
        else:
            raise ValueError("Arquivo inválido")
