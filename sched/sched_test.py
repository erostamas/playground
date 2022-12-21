#!/usr/bin/env python3

import sched
import time

scheduler = sched.scheduler(time.time, time.sleep)

def print_it():
    global count
    if count > 0:
        print('hello')
        for e in scheduler.queue:
            print(e)
        scheduler.enter(5, 1, print_it)
        count = count - 1

scheduler.enter(5, 1, print_it)
scheduler.enter(50, 1, print_it)
scheduler.enter(500, 1, print_it)
count = 5
scheduler.run()
