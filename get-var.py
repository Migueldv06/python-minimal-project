import os

# 1. Defina o nome da variável de ambiente que você deseja buscar.
#    - Tente 'HOME' ou 'USERPROFILE' (para o diretório inicial)
#    - Ou 'PATH' (para os diretórios de executáveis)
NOME_VARIAVEL = 'HOME' # Altere para 'USERPROFILE' se estiver no Windows

# 2. Use os.getenv() para buscar o valor da variável.
#    O segundo argumento (None) é o valor padrão a ser retornado 
#    se a variável não estiver definida.
valor_variavel = os.getenv(NOME_VARIAVEL)

# 3. Exiba o resultado.
print(f"Buscando a variável de ambiente: **{NOME_VARIAVEL}**")
print("-" * 40)

if valor_variavel is not None:
    print(f"**Valor encontrado:** {valor_variavel}")
else:
    print(f"**Aviso:** A variável de ambiente '{NOME_VARIAVEL}' não está definida.")
