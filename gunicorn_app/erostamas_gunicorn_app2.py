#!/usr/bin/env python3

import flask
from flask import Blueprint
import json
import gunicorn.app.base
from six import iteritems
import _thread
import threading
import signal
import os
import subprocess

blueprint = Blueprint('blueprint', __name__)

@blueprint.route('/', methods=['GET'])
def home():
    return {"you wanted to get": "the root"}

def setup_app():
    app = flask.Flask(__name__)
    app.config["DEBUG"] = False
    app.register_blueprint(blueprint, url_prefix='/my_own_prefix/')
    return app

def main():
    

    print("hellobello")
    
    options = {
        'bind': '%s:%s' % ('127.0.0.1', '11111'),
        'workers': 1,
        'debug': False
    }

    gunicorn = subprocess.Popen(["gunicorn", '--bind=0.0.0.0:11111', '--workers=1', 'erostamas_gunicorn_app2:setup_app()'])


if __name__ == '__main__':
    main()
    signal.pause()
