#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Filename: test31.py
# Author: peter.chen

try:
    a = int('0.5')
    print a
except:
    print 'error: convert "0.5" to int'
print 'Done'
