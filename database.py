import psycopg2
import os

def connect_db():
    return psycopg2.connect(os.environ.get("DATABASE_URL"))