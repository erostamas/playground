#!/usr/bin/env python3

import flask
from flask import Blueprint
import json
import gunicorn.app.base
from six import iteritems
import _thread
import threading
import signal
from gunicorn.arbiter import Arbiter
from gunicorn import sock, systemd, util
import os

blueprint = Blueprint('blueprint', __name__)

class MyArbiter(Arbiter):    
    def init_signals(self):
        for p in self.PIPE:
            os.close(p)

        # initialize the pipe
        self.PIPE = pair = os.pipe()
        for p in pair:
            util.set_non_blocking(p)
            util.close_on_exec(p)

        self.log.close_on_exec()

        # initialize all signals
        #for s in self.SIGNALS:
        #    signal.signal(s, self.signal)
        #signal.signal(signal.SIGCHLD, self.handle_chld)

class StandaloneApplication(gunicorn.app.base.BaseApplication):

    def __init__(self, app, options=None):
        self.options = options or {}
        self.application = app
        super(StandaloneApplication, self).__init__()

    def load_config(self):
        config = dict([(key, value) for key, value in iteritems(self.options)
                       if key in self.cfg.settings and value is not None])
        for key, value in iteritems(config):
            self.cfg.set(key.lower(), value)

    def load(self):
        return super(StandaloneApplication, self).load(sig=False)

    #def run(self):
    #    try:
    #        MyArbiter(self).run()
    #    except RuntimeError as e:
    #        print(f"ERROR!!!!!")


def main():
    app = flask.Flask(__name__)
    app.config["DEBUG"] = False

    print("hellobello")
    @blueprint.route('/', methods=['GET'])
    def home():
        return {"you wanted to get": "the root"}

    app.register_blueprint(blueprint, url_prefix='/my_own_prefix/')
    options = {
        'bind': '%s:%s' % ('127.0.0.1', '11111'),
        'workers': 1,
        'debug': False
    }
    print("hellobello")
    app.debug = False
    StandaloneApplication(app, options).run()
    print("hellobello")
    #app.run(host="0.0.0.0", port=11111)


if __name__ == '__main__':
    #t = _thread.start_new_thread(main, ())
    t = threading.Thread(target=main)
    t.daemon = True
    t.start()

    signal.pause()
