#!/usr/bin/env python3

from flask import Response, Flask, request
import json
import prometheus_client
from prometheus_client.core import CollectorRegistry
from prometheus_client import Summary, Counter, Histogram, Gauge
import time

_INF = float("inf")

graphs = {}
graphs['c'] = Counter('python_request_operations_total', 'The total number of processed requests')
graphs['h'] = Histogram('python_request_duration_seconds', 'Histogram for the duration in seconds.', buckets=(1, 2, 5, 6, 10, _INF))

def main():
    app = Flask(__name__)
    app.config["DEBUG"] = True

    @app.route('/', methods=['GET'])
    def home():
        start = time.time()
        graphs['c'].inc()
        config_file = open('/my_files/config.json',)
        config = json.load(config_file)
        ret = {}
        ret["this what you get"] = config["the_number"]
        end = time.time()
        graphs['h'].observe(end - start)
        return json.dumps(ret)

    @app.route('/stuff', methods=['GET'])
    def codes():
        config_file = open('/my_files/config.json',)
        config = json.load(config_file)
        ret = {}
        ret["this is the stuff you get"] = config["the_number"]
        return json.dumps(ret)

    @app.route("/metrics")
    def requests_count():
        res = []
        for k,v in graphs.items():
            res.append(prometheus_client.generate_latest(v))
        return Response(res, mimetype="text/plain")

    app.run(host="0.0.0.0")


if __name__ == '__main__':
    main()