"""
a python-based grep solution for windows and whatnot

Author: Me
Date: 1Nov2019

pygrep(Phrase to search for, File Path, 0 to return a list or 1 to write to grepout file
"""

import os
import re

os.chdir(os.getcwd())

def pygrep(phrase, path):
    r=[]
    for line in open(path, encoding="utf-8"):
        if re.search(phrase, line):
            r.append(line)
    return r

pygrep("pornhub", os.environ['USERPROFILE'] + r"\AppData\Local\Google\Chrome\User Data\Default\Bookmarks")

