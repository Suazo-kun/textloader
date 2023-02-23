#!/usr/bin/python3

from textloader import *

functions = [
    CirculatePointsLoader, DownPointsLoader, SetPointsLoader,
    RotatePointsLoader]

if __name__ == "__main__":
    for func in functions:
        temp = func()
        temp.PrintAsyncAnimation()
        sleep(temp.number_of_characters * temp.animation_delay * 5)
        temp.StopAsyncAnimation()
        print("\n")
