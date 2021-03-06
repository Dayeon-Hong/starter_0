# app.py
from flask import Flask, render_template
from flask_cors import CORS

#Flask 객체 인스턴스 생성
app = Flask(__name__)
# CORS(app)
CORS(app, resources={r'*':{'origins': 'http://localhost:3000'}})

@app.route('/api') # 접속하는 url
def main():
  return 'Hi';

@app.route('/api/checkCors', methods = ['POST'])
def setBtn():
  return 'Server has checked your request';

if __name__=="__main__":
  # host 등을 직접 지정하고 싶다면
  app.run(host="127.0.0.1", port="5000", debug=True)