"""
a python-based grep solution for windows and whatnot

Author: Me
Date: 1Nov2019

pygrep(Phrase to search for, File Path, 0 to return a list or 1 to write to grepout file
"""

import os
import re

os.chdir(os.getcwd())

def pygrep(phrase, path, opt):
    r=[]
    for line in open(path):
        if re.search(phrase, line):
            r.append(line)
    if opt == 0:
        return r
    else:
        with open("grepout", "w+") as f:
            for x in r:
                f.write("%s\n" % r)


    

