#!/usr/bin/env python3

import flask
import json

def main():
    app = flask.Flask(__name__)
    app.config["DEBUG"] = True

    @app.route('/', methods=['GET'])
    def home():
        config_file = open('/my_files/config.json',)
        config = json.load(config_file)
        ret = {}
        ret["this what you get"] = config["the_number"]
        return json.dumps(ret)

    @app.route('/stuff', methods=['GET'])
    def codes():
        config_file = open('/my_files/config.json',)
        config = json.load(config_file)
        ret = {}
        ret["this is the stuff you get"] = config["the_number"]
        return json.dumps(ret)

    app.run(host="0.0.0.0")


if __name__ == '__main__':
    main()