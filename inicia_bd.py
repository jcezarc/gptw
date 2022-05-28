from random import sample, choice, randint
from modelos import Pessoa #, Empresa
from empresas import grava_empresas
from pessoas import cria_pessoas
from consulta.emprego import CARGOS

PESSOAS_POR_EMPRESA = 5 # 4 funcionários e uma desempregada

def associa_nodes(notifica: callable):
    notifica('Gravando empresas...')
    lista_de_empresas = grava_empresas()
    notifica('Criando a lista de pessoas...')
    lista_de_pessoas = cria_pessoas(
        PESSOAS_POR_EMPRESA * len(lista_de_empresas)
    )
    notifica('Associando pessoas a empresas...')
    funcionarios = lista_de_pessoas.copy()
    for empresa in lista_de_empresas:
        for i in range(PESSOAS_POR_EMPRESA):
            pessoa = funcionarios.pop(0)
            for amigo in sample(lista_de_pessoas, 10):
                if amigo == pessoa:
                    continue
                pessoa.amigo_de.add(amigo)
            if i > 0:  # uma das pessoas está "open to work"
                pessoa.trabalha_em.add(
                    empresa,
                    properties={
                        'cargo': choice(CARGOS),
                        'meses': randint(1, 240), # até 20 anos
                    }
                )
            pessoa.save()
    notifica('CONCLUÍDO!')
