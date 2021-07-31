import psycopg2
import os

def get_connection():
    host1 = os.environ['db_url']
    port1 = os.environ['db_port']
    user1 = os.environ['db_username']
    password1 = os.environ['db_password']
    database1 = os.environ['db_database']
    return psycopg2.connect(
            host=host1,
            port=port1,
            user=user1,
            password=password1,
            database=database1
        )

def get_local_connection():
    return psycopg2.connect(
        host='localhost',
        port=5432,
        user='postgres',
        password='password',
        database='postgres'
    )