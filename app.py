from os import environ

from flask import Flask
from controllers import home

app = Flask(__name__)

app.register_blueprint(home)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(environ.get("PORT", 5000)))
