#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Filename: using_sys.py
# Author: peter.chen


import sys

print 'The command line arguments are: '
for i in sys.argv:
    print i

print '\n\nThe PYTHONPATH is',sys.path,'\n'