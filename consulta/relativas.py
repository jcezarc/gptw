from modelos import repo
from caminho import Caminho

def menor_caminho_entre(pessoa: str, empresa: str) -> Caminho:
    dataset = repo.graph.run('''
        MATCH(origem:Pessoa{nome:$pessoa})
        MATCH(destino:Pessoa)-[:TRABALHA_EM]
        ->(e:Empresa{nome:$empresa})
        MATCH p=shortestPath((origem)-[*..10]-(destino))
        RETURN p
        ''',
        parameters={
            'pessoa': pessoa,
            'empresa': empresa
        }
    )
    caminho = Caminho()
    for row in dataset:
        for path in row['p']:
            caminho.add(*path.nodes, pessoa)
    return caminho

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
