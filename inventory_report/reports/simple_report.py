from datetime import datetime
from collections import Counter


class SimpleReport:
    @staticmethod
    def generate(dict_list):
        date_create = []
        validate_product = []
        x_company = []

        for item in dict_list:
            x_company.append(item["nome_da_empresa"])
            date_create.append(item["data_de_fabricacao"])
            validate = datetime.strptime(item["data_de_validade"], "%Y-%m-%d")
            if validate >= datetime.today():
                validate_product.append((item["data_de_validade"]))
        x_company_more_products = Counter(x_company).most_common(1)
        return (
            f"Data de fabricação mais antiga: { (min(date_create)) }\n"
            f"Data de validade mais próxima: {(min( validate_product))}\n"
            f"Empresa com mais produtos: {x_company_more_products[0][0]}")
# resolvido com a ajuda da mentoria da Carol Weather Report
# disponivel em: https://app.betrybe.com/learn/course/
# 5e938f69-6e32-43b3-9685-c936530fd326/live-lectures/62d6cebd-7e2a-4e20-ba1a-54f515407308/recording/e2d95f10-7ea6-492e-bd7a-29bb138c2a5c
