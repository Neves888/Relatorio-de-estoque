from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
from re import search

import csv
import json
import xmltodict


class Inventory:
    @staticmethod
    def import_data(path_file, type_file):
        data = []

        if path_file.endswith(".csv"):
            data = Inventory.reader_csv(path_file)
        elif path_file.endswith(".json"):
            data = Inventory.reader_json(path_file)
        elif path_file.endswith(".xml"):
            data = Inventory.reader_xml(path_file)
        return Inventory.generate_report(data, type_file)

    @staticmethod
    def read(path: str):
        if search(r".csv$", path):
            with open(path, encoding="utf-8") as file:
                csv_file = csv.DictReader(file, delimiter=",", quotechar='"')
                return [row for row in csv_file]
        if search(r".json$", path):
            with open(path, encoding="utf-8") as file:
                return json.load(file)
        if search(r".xml$", path):
            with open(path, encoding="utf-8") as file:
                return xmltodict.parse(file.read())["dataset"]["record"]

    @staticmethod
    def create_report(data, type_file):
        simple = SimpleReport.generate(data)
        complete = CompleteReport.generate(data)
        if type_file == "simples":
            return simple
        elif type_file == "completo":
            return complete
