from flask import Flask

x = 1

def create_app():
    app = Flask(__name__)
    app.config["DEBUG"] = True

    @app.route("/")
    def hello_world():
        global x
        x = x + 1
        return f"{x}"

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(host="0.0.0.0", port=1234)