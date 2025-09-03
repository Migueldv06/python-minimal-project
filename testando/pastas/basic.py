import sys
import os
import time
import datetime

de lo(message):
    """Função simples para imprimir no log com timestamp e flush."""
    timestamp = datetime.datetime.now(datetime.UTC).strftime('%Y-%m-%d %H:%M:%S UTC')
    print(f"[{timestamp}] {message}")
    # Garante que a mensagem seja escrita imediatamente nos logs do contêiner
    sys.stdout.flush()

# --- Início do Script ---
log("=============================================")
log("--- SCRIPT DE TESTE PYTHON SIMPLES INICIADO ---")
log("=============================================")

# --- Diagnóstico do Ambiente ---
log("Verificando o ambiente de execução...")
log(f"  - Versão do Python: {sys.version.split()[0]}")
log(f"  - Diretório de Trabalho Atual: {os.getcwd()}")
log(f"  - Conteúdo do diretório:")
# Lista os arquivos no diretório atual para confirmar que o git clone funcionou
for item in os.listdir('.'):
    log(f"    - {item}")

# --- Simulação de Trabalho ---
log("\nIniciando uma tarefa simulada de 5 segundos...")
time.sleep(5)
log("Tarefa simulada concluída.")

# --- Mensagem Final de Sucesso ---
log("\n=============================================")
log(">>> TESTE BÁSICO CONCLUÍDO COM SUCESSO! <<<")
log("=============================================")
