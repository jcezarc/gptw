from modelos import repo

CARGOS = ['gerente', 'funcionário', 'RH']
GERENTE_ID = 0
FUNCIONARIO_ID = 1
RH_ID = 2

def desempregados() -> list:
    dataset = repo.graph.run('''
        match(p:Pessoa)where NOT (p)-->(:Empresa)return p
        '''
    )
    return sorted([row['p']['nome'] for row in dataset])


def pessoas_por_cargo(id_cargo: int) -> list:
    dataset = repo.graph.run('''
        match(p:Pessoa)-[:TRABALHA_EM{cargo:$cargo}]->()return p
        ''',
        parameters={
            'cargo': CARGOS[id_cargo]
        }
    )
    return sorted([row['p']['nome'] for row in dataset])

def colegas_de(pessoa: str) -> list:
    dataset = repo.graph.run('''
        match(:Pessoa{nome:$pessoa})-[:TRABALHA_EM]->
        (e:Empresa)<-[:TRABALHA_EM]-(p:Pessoa)return p
        ''',
        parameters={
            'pessoa': pessoa,
        }
    )
    return [row['p']['nome'] for row in dataset]
