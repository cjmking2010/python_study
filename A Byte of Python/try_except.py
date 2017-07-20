#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Filename: try_except.py
# Author: peter.chen

import sys

try:
    s = raw_input('Enter something --> ')
except EOFError:
    print '\nWhy did you do an EOF on me?'
    sys.exit() # exit the program
except:
    print '\nSome error/exception occurered.'
    # here,we are not exiting the program

print 'Done'
