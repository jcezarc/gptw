from modelos import Empresa, Pessoa, repo

def menor_caminho_até(empresa: Empresa) -> list[Pessoa]:
    pass


def amigos_em_comum(pessoa1: str, pessoa2: str) -> list:
    dataset = repo.graph.run('''
        MATCH(p1:Pessoa)-[:AMIGO_DE]-(c)-[:AMIGO_DE]-(p2:Pessoa)
        WHERE p1.nome=$pessoa1 AND p2.nome=$pessoa2
        RETURN c
        ''',
        parameters={
            'pessoa1': pessoa1,
            'pessoa2': pessoa2
        }
    )
    return [row['c']['nome'] for row in dataset]
