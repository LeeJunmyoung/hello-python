from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

# $env:FLASK_APP="flaskexam.py"
# flask run
# 하지만 난 django를 공부할거당.

# 라이브러리   : 내가 작성한 코드를 남이 만든 코드를 호출하는 구조.
# 프레임 워크  : 내가 작성한 코드를 남이 만든 코드가 호출하는 구조.