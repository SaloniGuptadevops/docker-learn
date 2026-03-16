from flask import Flask
import psycopg2
import redis
import os

app = Flask(__name__)

db_host=os.getenv("DB_HOST")
redis_host=os.getenv("REDIS_HOST")

@app.route('/')
def hello():

    try:
        conn = psycopg2.connect(
            host=db_host,
            database="testdb",
            user="postgres",
            password="postgres"
        )

        cur=conn.cursor()
        cur.execute("SELECT version();")
        db_version=cur.fetchone()
        conn.close()

    except:
        db_version="DB not connected"

    try:
        r=redis.Redis(host=redis_host,port=6379)
        r.set('visits',1)
        cache="Redis connected"

    except:
        cache="Redis not connected"

    return f"Hello DevOps 🚀 <br> DB: {db_version} <br> Cache: {cache}"

app.run(host='0.0.0.0',port=5000)
