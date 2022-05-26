from inicia_bd import associa_nodes
from pessoas import eu
from consultas import amigos_em_comum


if not eu():
    associa_nodes(print)
print(
    amigos_em_comum(
        'João Miguel da Costa',
        'Mariane da Paz'
    )
)
