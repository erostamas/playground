#!/usr/bin/env python3

import flask
from flask import Blueprint
import json
import gunicorn.app.base
from six import iteritems
import _thread
import threading
import signal
import wsgiserver
import time

blueprint = Blueprint('blueprint', __name__)

class Dummy:
    def __init__(self, x):
        self.x = x

def main(dummy):
    
    app = flask.Flask(__name__)
    app.config["DEBUG"] = False

    print("hellobello")
    @blueprint.route('/', methods=['GET'])
    def home():
        return {"you wanted to get": f"{dummy.x}"}

    @blueprint.route('/change', methods=['GET'])
    def change():
        dummy.x = dummy.x + 1
        return {"you wanted to get": f"{dummy.x}"}

    app.register_blueprint(blueprint, url_prefix='/my_own_prefix/')
    server = wsgiserver.WSGIServer(app, host='0.0.0.0', port=5005)
    server.start()



if __name__ == '__main__':
    #t = _thread.start_new_thread(main, ())
    dummy = Dummy(16)
    t = threading.Thread(target=main, args=(dummy,))
    t.daemon = True
    t.start()

    time.sleep(5)
    dummy.x = 17
    signal.pause()
