from py2neo.data import Node


class Caminho:
    """
    Classe que processa um path
    retornado da consulta.
    """
    def __init__(self):
        self.items = [['', '']]

    def add(self, ini:Node, fim:Node, raiz: str):
        """
        Ordena os nomes dos nodes
        para formar sequências
        """
        ini, fim = [p['nome'] for p in [ini, fim]]
        if fim == raiz:
            ini, fim = fim, ini
        elif self.items[-1][-1] in [ini, fim]:
            if fim == self.items[-1][-1]:
                self.items[-1].append(ini)
            else:
                self.items[-1].append(fim)
            return
        self.items.append([ini, fim])

    def __str__(self):
        return '\n'.join(' -> '.join(c) for c in self.items[1:])
