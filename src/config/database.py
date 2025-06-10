import os
import psycopg2
from psycopg2.extras import RealDictCursor
from dotenv import load_dotenv

load_dotenv()

db_host = os.getenv("DB_HOST")
db_name = os.getenv("DB_NAME")
db_user = os.getenv("DB_USER")
db_pass = os.getenv("DB_PASS")
db_port = os.getenv("DB_PORT")


def get_connection():
    try:
        conn = psycopg2.connect(
            host=db_host,
            dbname=db_name,
            user=db_user,
            password=db_pass,
            port=db_port,
            cursor_factory=RealDictCursor
        )

        return conn
    except psycopg2.Error as e:
        print("[DATABASE] Falha ao conectar - ", e)
        return None
