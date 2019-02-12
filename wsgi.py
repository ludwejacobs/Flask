from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello():
    return "<h1> BIG BOOIIII</h1>"

if __name__ == "__main__":
    application.run()
