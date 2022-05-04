"""
a countdown timer for various things
Author: Me
Date: 6DEC2019
"""

import os, time

os.chdir(os.getcwd())

def countdown(t):
    while t >=0:
        print(t, end="\n")
        time.sleep(1)
        t -= 1

#countdown(5)
