from inventory_report.importer.importer import Importer
from re import search
import xmltodict


class XmlImporter(Importer):
    @classmethod
    def import_data(cls, path):
        if search(r".xml$", path):
            with open(path, "r") as file:
                return list(xmltodict.parse(file.read())["dataset"]["record"])
        else:
            raise ValueError("Arquivo inválido")
