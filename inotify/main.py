#!/usr/bin/env python3

import inotify.adapters
from pathlib import Path
import os

DIR = Path(os.path.dirname(os.path.realpath(__file__)))
def _main():
    i = inotify.adapters.Inotify()

    i.add_watch((DIR / Path('file')).as_posix())

    for event in i.event_gen(yield_nones=False):
        (_, type_names, path, filename) = event

        print("PATH=[{}] FILENAME=[{}] EVENT_TYPES={}".format(
              path, filename, type_names))

if __name__ == '__main__':
    _main()