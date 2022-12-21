#!/usr/bin/env python3

import signal
import sys
import json
from pathlib import Path

def handler(signum, frame):
    print(f'Signal handler called with signal {signum}')
    sys.exit()

def main():
    signal.signal(signal.SIGINT, handler)
    signal.signal(signal.SIGTERM, handler)
    config = json.loads(Path('/opt/erostamas/subchart-test/config.json').read_text())
    print(f'Number is : {config["the_number"]}')
    print('Waiting for signal...')
    signal.pause()

if __name__ == '__main__':
    main()