import os
import psycopg2

DATABASE_URL = os.environ['DATABASE_URL']

conn = psycopg2.connect(DATABASE_URL, sslmode='require')

def create_table():
    try:
        conn = psycopg2.connect(DATABASE_URL, sslmode='require')
        cur = conn.cursor()
        cur.execute("CREATE TABLE users (id serial PRIMARY KEY, name varchar, tg_id varchar, mention varchar);")
        conn.commit()
        cur.close()
        conn.close()
    except psycopg2.Error as e:
        print(e)


def insert(mention,group_id):
    try:
        conn = psycopg2.connect(DATABASE_URL, sslmode='require')
        cur = conn.cursor()
        cur.execute(f"INSERT INTO users (mention,group_id) VALUES ('{mention}','{group_id}');")
        conn.commit()
        cur.close()
        conn.close()
    except psycopg2.Error as e:
        print(e)

def select(chat_id):
    try:
        conn = psycopg2.connect(DATABASE_URL, sslmode='require')
        cur = conn.cursor()
        cur.execute(f"SELECT mention FROM users WHERE group_id = '{chat_id}';")
        users = cur.fetchall()
        cur.close()
        conn.close()

        return users
    except psycopg2.Error as e:
        print(e)

def check(str,group_id):
    try:
        conn = psycopg2.connect(DATABASE_URL, sslmode='require')
        cur = conn.cursor()
        cur.execute(f"SELECT * FROM users WHERE mention='{str}' AND group_id='{group_id}';")
        users = cur.fetchall()
        cur.close()
        conn.close()

        return users
    except psycopg2.Error as e:
        print(e)
