from api_dao.api_call import collect_countries_article
from psql_dao.connect_db import insert_articles_into_db, df_to_tuple


def collect_insert_news():
    all_df = collect_countries_article()
    all_list = df_to_tuple(all_df)
    insert_articles_into_db(all_list)
