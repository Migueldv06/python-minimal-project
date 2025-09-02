import logging
import sys

# Configuração básica do logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.StreamHandler(sys.stdout),
        logging.FileHandler("dependencias.log", mode="w", encoding="utf-8")
    ]
)

logger = logging.getLogger(__name__)

logger.info("🔍 Testando dependências...")

try:
    import requests
    r = requests.get("https://httpbin.org/get")
    logger.info("✅ requests ok: %s", r.status_code)
except Exception as e:
    logger.error("❌ requests falhou: %s", e)

try:
    import pandas as pd
    df = pd.DataFrame({"a": [1, 2], "b": [3, 4]})
    logger.info("✅ pandas ok: %s", df.head(1).to_dict())
except Exception as e:
    logger.error("❌ pandas falhou: %s", e)

try:
    import sqlalchemy
    from sqlalchemy import create_engine
    engine = create_engine("sqlite:///:memory:")
    with engine.connect() as conn:
        conn.execute(sqlalchemy.text("SELECT 1"))
    logger.info("✅ sqlalchemy ok (sqlite)")
except Exception as e:
    logger.error("❌ sqlalchemy falhou: %s", e)

try:
    import psycopg2
    logger.info("✅ psycopg2-binary ok (importado)")
except Exception as e:
    logger.error("❌ psycopg2-binary falhou: %s", e)

try:
    from dotenv import load_dotenv
    logger.info("✅ python-dotenv ok (importado)")
except Exception as e:
    logger.error("❌ python-dotenv falhou: %s", e)

try:
    import xml.etree.ElementTree as ET
    ET.Element("root")
    logger.info("✅ xml.etree.ElementTree ok")
except Exception as e:
    logger.error("❌ xml.etree.ElementTree falhou: %s", e)

try:
    import os, time, json, smtplib
    from datetime import date, datetime
    from pathlib import Path
    from concurrent.futures import ThreadPoolExecutor, as_completed
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    logger.info("✅ módulos padrão (os, time, json, email, etc) ok")
except Exception as e:
    logger.error("❌ módulos padrão falharam: %s", e)

try:
    from azure.identity import ClientSecretCredential
    from azure.keyvault.secrets import SecretClient
    logger.info("✅ azure.identity e azure.keyvault-secrets ok (importados)")
except Exception as e:
    logger.error("❌ azure libs falharam: %s", e)

logger.info("🚀 Teste finalizado.")
