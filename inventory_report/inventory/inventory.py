from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
from re import search
import csv
import json
import xmltodict


class Inventory:
    @staticmethod
    def read(path: str):
        if search(r".csv$", path):
            with open(path, "r") as file:
                return list(csv.DictReader(file))
        if search(r".json$", path):
            with open(path, "r") as file:
                return list(json.load(file))
        if search(r".xml$", path):
            with open(path, "r") as file:
                return list(xmltodict.parse(file.read())["dataset"]["record"])

    @staticmethod
    def import_data(path, type):
        data = Inventory.read(path)
        simple = SimpleReport.generate(data)
        complete = CompleteReport.generate(data)
        if type == "simples":
            return simple
        else:
            return complete
