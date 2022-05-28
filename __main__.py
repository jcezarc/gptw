from inicia_bd import associa_nodes
from pessoas import tem_dados, MEU_NOME
from consulta.relativas import menor_caminho_entre


if not tem_dados():
    associa_nodes(print)
print(
    menor_caminho_entre(MEU_NOME, 'MAGAZINE LUIZA')
)
