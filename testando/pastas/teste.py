# Nome do arquivo: run_test.py

import datetime
import sys

# --- Bloco de Funções ---
def log_message(message):
    """Imprime uma mensagem e força a escrita imediata nos logs."""
    print(message)
    sys.stdout.flush()

# --- Início da Execução ---
log_message("==========================================")
log_message("--- INÍCIO DA EXECUÇÃO DO SCRIPT PYTHON ---")
log_message("==========================================")

# --- Mensagem Principal ---
log_message(">>> SCRIPT BÁSICO EXECUTADO COM SUCESSO! <<<")
log_message("\n") # Adiciona uma linha em branco para espaçamento

# --- Informações de Debug ---
log_message("Informações do Ambiente:")
log_message(f"  - Timestamp (UTC): {datetime.datetime.now(datetime.UTC)}")
log_message(f"  - Versão do Python: {sys.version.split()[0]}")
log_message("\n")

# --- Fim da Execução ---
log_message("==========================================")
log_message("--- FIM DA EXECUÇÃO DO SCRIPT PYTHON ---")
log_message("==========================================")
