from inventory_report.importer.importer import Importer
from re import search
import csv


class CsvImporter(Importer):
    @classmethod
    def import_data(cls, path):
        if search(r".csv$", path):
            with open(path, "r") as file:
                return list(csv.DictReader(file))
        else:
            raise ValueError("Arquivo inválido")
