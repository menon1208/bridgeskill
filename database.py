import psycopg2

def connect_db():
    return psycopg2.connect(
        host="localhost",
        database="bridgeskill",
        user="postgres",
        password="123456"
    )


