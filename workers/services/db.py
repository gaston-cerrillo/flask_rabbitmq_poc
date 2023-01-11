import pandas as pd
import psycopg2
from sqlalchemy import create_engine
from decouple import config


def connect():
    try:
        db = config('db')
        user = config('user')
        password = config('db_pass')
        server = config('server')
        port = config('port')
        alchemy_engine = create_engine(
            f'postgresql+psycopg2://{user}:{password}@{server}:{port}/{db}',
            pool_recycle=3600)
        return alchemy_engine.connect()
    except Exception as e:
        print(e)


def query(sql_query):
    conn = connect()
    res = pd.read_sql(sql_query, conn)
    conn.close()
    return res
