from modelos import repo

CARGOS = ['funcionário', 'RH', 'gerente']
FUNCIONARIO_ID = 0
RH_ID = 1
GERENTE_ID = 2

def desempregados() -> list:
    dataset = repo.graph.run('''
        match(p:Pessoa)where NOT (p)-->(:Empresa)return p
        '''
    )
    return sorted([row['p']['nome'] for row in dataset])


def pessoas_por_cargo(id_cargo: int, empresa: str='') -> list:
    dataset = repo.graph.run('''
        match(p:Pessoa)-[{}]->({})return p
        '''.format(
            ':TRABALHA_EM{cargo:$cargo}',
            'e:Empresa{nome:$empresa}' if empresa else ''
        ),
        parameters={
            'cargo': CARGOS[id_cargo],
            'empresa': empresa
        }
    )
    return sorted([row['p']['nome'] for row in dataset])

def colegas_de(pessoa: str) -> list:
    dataset = repo.graph.run('''
        match(:Pessoa{nome:$pessoa})-[:TRABALHA_EM]->
        (:Empresa)<-[:TRABALHA_EM]-(p:Pessoa)return p
        ''',
        parameters={
            'pessoa': pessoa,
        }
    )
    return [row['p']['nome'] for row in dataset]
