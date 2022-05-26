from py2neo.ogm import (
    Repository,
    Model,
    Property,
    RelatedFrom,
    RelatedTo
)

repo = Repository("bolt://neo4j@localhost:7687", password="1234")

class Empresa(Model):
    nome = Property()
    funcionarios = RelatedFrom('Pessoa', 'mora_em')

    def save(self):
        repo.save(self)
        return self


class Pessoa(Model):
    nome = Property()
    amigo_de = RelatedTo("Pessoa")
    trabalha_em = RelatedTo(Empresa)

    def save(self):
        repo.save(self)
        return self
