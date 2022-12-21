#!/usr/bin/python3 -uB

from time import sleep
import cProfile

def main():
    sleep(1000)

if __name__ == "__main__":
    cProfile.run('main()', filename='x.txt')