from csv import DictReader
from modelos import Empresa

def grava_empresas():
    arquivo = '/users/julio/gptw/ranking.csv'
    with open(arquivo, 'r', encoding='utf-8') as f:
        reader = DictReader(f)
        return [
            Empresa(
                nome=row['empresa'].strip()
            ).save()
            for row in reader
        ]
