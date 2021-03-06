from flask import Flask
import settings

app = Flask(__name__)


@app.route("/")
def index():
    return "hello word!"


if __name__ == '__main__':
    app.run(host=settings.HOST, port=settings.PORT, debug=settings.DEBUG)
