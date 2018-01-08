#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Filename: break.py
# Author: peter.chen

while True:
    s = raw_input('Enter something: ')
    if s == 'quit':
        break
    print 'Length of the string is',len(s)
print 'Done'
