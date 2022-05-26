from inicia_bd import associa_nodes
from pessoas import tem_dados, MEU_NOME
from consultas import amigos_em_comum, menor_caminho_entre


if not tem_dados():
    associa_nodes(print)
# print(
#     amigos_em_comum(
#         'João Miguel da Costa',
#         'Mariane da Paz'
#     )
# )
print(
    menor_caminho_entre(MEU_NOME, 'MAGAZINE LUIZA')
)
