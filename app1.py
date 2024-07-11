from flask import Flask, render_template

# flaskの相関のモジュールを導入します。

import RPi.GPIO as GPIO
# 　RPi.GPIOを導入します。

import time

# タイムのモジュールを導入します。

Led_pins = [26, 19, 13]
# 26は赤い
# 19は黄色
# 13は緑色

GPIO.setmode(GPIO.BCM)
# Raspberry Pi のチップ上のピン番号を指します。このモードを設定することで、後続のピン設定で BCM ピン番号を使用できます。
GPIO.setup(Led_pins, GPIO.OUT)
# LED ピンを出力として使用できるようになります。

# 新しいflaskの実例を作ります。
app = Flask(__name__, template_folder='template')


# home 画面 のルート
@app.route('/', methods=['GET'])
def main():
    return render_template("index.html")
    # index.htmlの画面を返事します。
    # 実は　templateフォルダーの中でのindex.htmlを返事します。


# 緑色のLEDルートを作る
@app.route('/green', methods=['GET'])
def green():
    GPIO.output(13, GPIO.HIGH)  # GPIO.13は電源を入れる
    time.sleep(3.5)  # 時間3.5s
    return render_template("green.html", ID="緑色", info="緑色のLEDを付けました。")


# 黄色のLEDルートを作る
@app.route('/yellow', methods=['GET'])
def yellow():
    GPIO.output(19,GPIO.HIGH)   # GPIO.19は電源を入れる
    time.sleep(3.5)             # 時間3.5s
    return render_template("yellow.html", ID="黄色", info="黄色のLEDを付けました。")


# 赤いLEDのルート
@app.route('/red', methods=['GET'])
def red():
    GPIO.output(26,GPIO.HIGH)   # GPIO.26は電源を入れる
    time.sleep(3.5)             # 時間3.5s
    return render_template("yellow.html", ID="赤い", info="赤いLEDを付けました。")


@app.route('/404', methods=['GET'])
def error():
    GPIO.output(26,GPIO.HIGH)   # GPIO.26は電源を入れる
    time.sleep(3.5)             # 時間3.5s
    return render_template("error.html")


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8080, debug=False)
    # このプロジェクトはローカルのサーバーで実行、ポット8080。
    # debug=True 開発の時は　true
    # debug=False 開発終わった時は　False
GPIO.clearnup()
