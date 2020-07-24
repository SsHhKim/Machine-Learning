from flask import Flask
app = Flask(__name__)

@app.route('/')    #웹 주소의 루트로 요청이 오면 낸다는 표시(웹주소 이후에 붙여짐, 생략되어있음)
def index():
    return 'Hello Flask!!!'

if __name__ == '__main__':
    app.run(debug=True)


from flask import 