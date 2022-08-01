from flask import Flask, request, jsonify
import os

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False  # 日本語文字化け対策
app.config["JSON_SORT_KEYS"] = False  # ソートをそのまま


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
        'status': 'OK',
        'data': data
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("PORT")))
