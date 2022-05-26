from random import randint
from faker import Faker
from modelos import repo, Pessoa

MEU_NOME = 'Júlio Cascalles'
#           ^^------ Insira aqui seu nome!


def cria_pessoas(qtd: int) -> list[Pessoa]:
    """
    Cria uma lista de Pessoas (SEM gravar)
    : qtd - Quantidade de pessoas na lista
    """
    faker = Faker('pt-BR')
    nomes = [
        faker.name().split('. ')[-1]
        for _ in range(qtd-1)
    ]
    nomes.insert(randint(0, qtd-2), MEU_NOME)
    return [Pessoa(nome=n) for n in nomes]


def tem_dados() -> bool:
    return repo.match(Pessoa).where(nome=MEU_NOME).exists()
