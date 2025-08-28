import sys

print("🔍 Testando dependências...")

try:
    import requests
    r = requests.get("https://httpbin.org/get")
    print("✅ requests ok:", r.status_code)
except Exception as e:
    print("❌ requests falhou:", e)

try:
    import pandas as pd
    df = pd.DataFrame({"a": [1, 2], "b": [3, 4]})
    print("✅ pandas ok:", df.head(1).to_dict())
except Exception as e:
    print("❌ pandas falhou:", e)

try:
    import sqlalchemy
    from sqlalchemy import create_engine
    # conexão fake só pra validar driver
    engine = create_engine("sqlite:///:memory:")
    with engine.connect() as conn:
        conn.execute(sqlalchemy.text("SELECT 1"))
    print("✅ sqlalchemy ok (sqlite)")
except Exception as e:
    print("❌ sqlalchemy falhou:", e)

try:
    import psycopg2
    print("✅ psycopg2-binary ok (importado)")
except Exception as e:
    print("❌ psycopg2-binary falhou:", e)

try:
    from dotenv import load_dotenv
    print("✅ python-dotenv ok (importado)")
except Exception as e:
    print("❌ python-dotenv falhou:", e)

try:
    import xml.etree.ElementTree as ET
    ET.Element("root")
    print("✅ xml.etree.ElementTree ok")
except Exception as e:
    print("❌ xml.etree.ElementTree falhou:", e)

try:
    import os, time, json, smtplib
    from datetime import date, datetime
    from pathlib import Path
    from concurrent.futures import ThreadPoolExecutor, as_completed
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    print("✅ módulos padrão (os, time, json, email, etc) ok")
except Exception as e:
    print("❌ módulos padrão falharam:", e)

try:
    from azure.identity import ClientSecretCredential
    from azure.keyvault.secrets import SecretClient
    print("✅ azure.identity e azure.keyvault-secrets ok (importados)")
except Exception as e:
    print("❌ azure libs falharam:", e)

print("\n🚀 Teste finalizado.")
