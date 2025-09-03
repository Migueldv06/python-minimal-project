import logging
import sys

# Configuração de logging APENAS para o console (stdout)
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger(__name__)

logger.info("🔍 Testando dependências...")

# Lista de bibliotecas para testar
libs_to_test = [
    "requests", "pandas", "sqlalchemy", "psycopg2",
    "dotenv", "azure.identity", "azure.keyvault.secrets"
]

for lib in libs_to_test:
    try:
        __import__(lib)
        logger.info(f"✅ {lib} ok")
    except ImportError as e:
        logger.error(f"❌ {lib} falhou: {e}")

logger.info("🚀 Teste finalizado.")
