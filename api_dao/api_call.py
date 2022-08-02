import os
import time
import datetime
import requests
import pandas as pd
from typing import Final

from country import Country

apikey: Final[str] = os.environ["NEWS_API_KEY"]

headers = {'X-Api-Key': apikey}


# Everything
def call_everything_api():
    url = 'https://newsapi.org/v2/everything'
    params = {
        'q': 'コロナウイルス AND ワクチン',
        'sortBy': 'publishedAt',
        'pageSize': 100
    }

    # Get response
    response = requests.get(url, headers=headers, params=params)
    print(response)
    print(response.json())

    pd.options.display.max_colwidth = 25

    if response.ok:
        data = response.json()
        df = pd.DataFrame(data['articles'])
        print('totalResults:', data['totalResults'])

    # タイトル、国、記事URL、画像URL、
    print(df[['publishedAt', 'title', 'url']])


# Top headlines Endpoint
def call_top_headline_api(country: str):
    print('-----------')
    print(f'country: {country}')
    url = 'https://newsapi.org/v2/top-headlines'
    params = {
        # 'category': 'business',
        'country': country
    }

    # Get response
    response = requests.get(url, headers=headers, params=params)
    # Make dataframe
    if response.ok:
        data = response.json()
        df = pd.DataFrame(data['articles'])
        df['country'] = country
        print('totalResults:', data['totalResults'])
        print('df')
        print(df[['title','author','url','urlToImage','country']])
        # df[['country', 'publishedAt', 'title', 'url', 'urlToImage']].to_csv('{}_{}_article_data.csv'.format(datetime.datetime.now(), country))
        return df[['title','author','url','urlToImage','description','country','publishedAt']]
    else:
        return None
        # 例外を投げる？


def collect_countries_article():
    all_df = pd.DataFrame()
    cnt = 0  # FIXME: APIをあまり叩かないようにするためcntセットしている。本番は外す。
    for co in Country:
        cnt += 1
        if cnt >= 3:
            break
        df = call_top_headline_api(co.value)
        if not df.empty:
            all_df = pd.concat([all_df, df])
        time.sleep(0.5)

    print(f'collected data: {datetime.datetime.now()}')
    # all_df.to_csv('{}_article_data.csv'.format(datetime.datetime.now()))
    return all_df
