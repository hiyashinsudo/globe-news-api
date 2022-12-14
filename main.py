import os
from enum import Enum
from flask import Flask, request, jsonify

from country import Country

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False  # 日本語文字化け対策
app.config["JSON_SORT_KEYS"] = False  # ソートをそのまま


class Status(Enum):
    OK = 'OK'
    NG = 'NG'


@app.route('/hello', methods=['GET'])
def hello():
    return "hello_world"


@app.route('/hellojson', methods=['GET'])
def hello_json():
    data = [
        {"name": "山田"},
        {"age": 30}
    ]
    return jsonify({
        'status': Status.OK,
        'data': data
    })


@app.route('/testnews', methods=['GET'])
def test_news():
    data = [
        {'title': "最低賃金引き上げ額、過去最大の31円 平均961円に 中央審決定 - 毎日新聞 - 毎日新聞"},
        {'url': 'https://mainichi.jp/articles/20220801/k00/00m/020/097000c'},
        {'urlToImage': 'https://cdn.mainichi.jp/vol1/2022/06/28/20220628k0000m040241000p/0c10.jpg?1'},
        {'country': Country.JP}
    ]
    return jsonify({
        'status': Status.OK,
        'data': data
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("PORT")))
