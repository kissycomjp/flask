#!/usr/bin/python3
# coding: utf-8
from flask import Flask, request, jsonify
app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False  # JSONでの日本語文字化け対策

@app.route('/', methods=['POST'])
def post_json():
    json = request.get_json()  # POSTされたJSONを取得
    for key,val in json.items():
      print(key, 'is', val)
      for k2,v2 in val.items():
        print(k2, 'is', v2)
    
    return jsonify(json)  # JSONをレスポンス

@app.route('/', methods=['GET'])
def get_json_from_dictionary():
    dic = {
        'foo': 'bar',
        'ほげ': 'ふが'
    }
    return jsonify(dic)  # JSONをレスポンス

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)

