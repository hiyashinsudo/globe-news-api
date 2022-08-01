import time
import datetime
import requests
import pandas as pd
from typing import Final

country_list: Final[tuple] = ('ae', 'ar', 'at', 'au', 'be', 'bg', 'br', 'ca', 'ch', 'cn', 'co', 'cu', 'cz', 'de', 'eg',
                              'fr', 'gb', 'gr', 'hk', 'hu', 'id', 'ie', 'il', 'in', 'it', 'jp', 'kr', 'lt', 'lv', 'ma',
                              'mx', 'my', 'ng', 'nl', 'no', 'nz', 'ph', 'pl', 'pt', 'ro', 'rs', 'ru', 'sa', 'se', 'sg',
                              'si', 'sk', 'th', 'tr', 'tw', 'ua', 'us', 've', 'za')

apikey: Final[str] = "apikey here"

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
        print(df[['publishedAt', 'title', 'url', 'urlToImage']])
        df[['country', 'publishedAt', 'title', 'url', 'urlToImage']].to_csv('{}_{}_article_data.csv'.format(datetime.datetime.now(), country))
        return df[['country', 'publishedAt', 'title', 'url', 'urlToImage']]
    else:
        return None
        # 例外を投げる？


def collect_countries_article():
    all_df = pd.DataFrame()
    for country in country_list:
        df = call_top_headline_api(country)
        if not df.empty:
            all_df = pd.concat([all_df, df])
        time.sleep(0.5)

    print('collected data')
    print(all_df)
    all_df.to_csv('{}_article_data.csv'.format(datetime.datetime.now()))


collect_countries_article()
