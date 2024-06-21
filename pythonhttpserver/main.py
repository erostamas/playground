from wsgiref.simple_server import make_server, WSGIRequestHandler
from flask import Flask

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def home():
    return "hello"

class MyHandler(WSGIRequestHandler):
    def log_message(self, format, *args):
        print(self.log_date_time_string() + ' ' + self.address_string() + ' ' + (format % args))

with make_server('', 4333, app, handler_class=MyHandler) as httpd:
    print("Serving HTTP on port 8000...")

    # Respond to requests until process is killed
    httpd.serve_forever()
