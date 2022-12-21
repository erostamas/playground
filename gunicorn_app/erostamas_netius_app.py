#!/usr/bin/env python3

import netius.servers
import flask
from flask import Blueprint
import threading
import time


class MyServer:
    def __init__(self):
        self.__value = 16

    def start(self):
        self.__t = threading.Thread(target=self.__start)
        self.__t.daemon = True
        self.__t.start()

    def __start(self):
        blueprint = Blueprint('blueprint', __name__)

        app = flask.Flask(__name__)
        app.config["DEBUG"] = False
        print("hellobello")
        @blueprint.route('/', methods=['GET'])
        def home():
            self.__value = self.__value + 1
            return {"you wanted to get": "the root", "value": self.__value}

        app.register_blueprint(blueprint, url_prefix='/my_own_prefix/')

        server = netius.servers.WSGIServer(app)
        server.serve(host = '0.0.0.0', port = 1234)

server = MyServer()
server.start()
time.sleep(3600)