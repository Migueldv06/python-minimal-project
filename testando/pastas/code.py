import sys
import requests
import pandas as pd
import sqlalchemy
import psycopg2
# ... etc, todos os seus outros imports

def log(message):
    """Função para garantir que a mensagem seja impressa e enviada ao log imediatamente."""
    print(message)
    sys.stdout.flush()

log("🔍 Testando dependências...")

try:
    r = requests.get("https://httpbin.org/get")
    log(f"✅ requests ok: {r.status_code}")
except Exception as e:
    log(f"❌ requests falhou: {e}")

try:
    df = pd.DataFrame({"a": [1, 2], "b": [3, 4]})
    log(f"✅ pandas ok: {df.head(1).to_dict()}")
except Exception as e:
    log(f"❌ pandas falhou: {e}")

# ... continue usando log() para todas as outras mensagens ...
# Exemplo:
# try:
#     # Apenas o import é suficiente para o teste
#     log("✅ psycopg2-binary ok (importado)")
# except Exception as e:
#     log(f"❌ psycopg2-binary falhou: {e}")


log("\n🚀 Teste finalizado.")
