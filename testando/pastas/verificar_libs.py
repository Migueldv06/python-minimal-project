# nome do arquivo: verificar_libs.py
import sys
from importlib import metadata

def log(message):
    """Função simples para imprimir no log."""
    print(message)
    sys.stdout.flush()

log("=====================================================")
log("--- VERIFICANDO BIBLIOTECAS PYTHON INSTALADAS ---")
log("=====================================================")

try:
    # Obtém a lista de todas as "distribuições" (pacotes) instaladas
    dists = metadata.distributions()

    # Formata e ordena a lista para exibição
    installed_packages = sorted(
        [f"{dist.metadata['name']}=={dist.version}" for dist in dists]
    )

    if not installed_packages:
        log("Nenhuma biblioteca externa encontrada.")
    else:
        for package in installed_packages:
            log(package)

except Exception as e:
    log(f"Ocorreu um erro ao tentar listar as bibliotecas: {e}")

log("\n--- Verificação finalizada ---")
