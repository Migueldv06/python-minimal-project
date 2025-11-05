import os

NOME_VARIAVEL = 'VAR'

valor_variavel = os.getenv(NOME_VARIAVEL)

print(f"Buscando a variável de ambiente: **{NOME_VARIAVEL}**")
print("-" * 40)

if valor_variavel is not None:
    print(f"**Valor encontrado:** {valor_variavel}")
else:
    print(f"**Aviso:** A variável de ambiente '{NOME_VARIAVEL}' não está definida.")
