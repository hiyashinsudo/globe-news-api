import os

import pandas
import psycopg2
from psycopg2 import extras

DATABASE_URL = os.environ.get('DATABASE_URL')


def df_to_tuple(df: pandas.DataFrame):
    _tuple = [tuple(x) for x in df.values]
    return _tuple


def insert_articles_into_db(news_list: list):
    insert_list = [
        ('テストタイトル1', 'テスト著者1', 'http://localhost/', 'http://localhost/img', 'テスト説明1', 'jp', '2022-08-01T12:41:03Z'),
        ('テストタイトル2', 'テスト著者2', 'http://localhost/', 'http://localhost/img', 'テスト説明2', 'jp', '2022-08-01T13:45:03Z')]

    print("insert article table")
    with psycopg2.connect(DATABASE_URL) as conn:
        with conn.cursor() as curs:
            extras.execute_values(
                curs,
                "INSERT INTO articles(title, author, url, urlToImage, description, country, published_at) VALUES %s",
                news_list)
