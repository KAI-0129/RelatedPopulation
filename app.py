import re
from flask import Flask, render_template, redirect, request, session
from flask.templating import render_template
import random
import sqlite3
from werkzeug.datastructures import Range
app = Flask(__name__)
# Flask では標準で Flask.secret_key を設定すると、sessionを使うことができます。この時、Flask では session の内容を署名付きで Cookie に保存します。
app.secret_key = 'related population'
# -----------------トップ-----------------------
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/detail')
def detail():
    return render_template('detail.html')
if __name__ == "__main__":
    DEBUG:True
    app.run()
