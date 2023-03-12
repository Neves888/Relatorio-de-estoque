from inventory_report.reports.simple_report import SimpleReport
from collections import Counter


class CompleteReport(SimpleReport):
    @staticmethod
    def generate(dict_list):
        simple_report = SimpleReport.generate(dict_list)
        x_company = []
        for product in dict_list:
            x_company.append(product["nome_da_empresa"])

        x_company_counter = Counter(x_company)
        product_company = ""
        for item in x_company_counter:
            product_company += f"- {item}: {x_company_counter[item]}\n"

        return (
            f"{simple_report}\n"
            f"Produtos estocados por empresa:\n"
            f"{product_company}"
        )
