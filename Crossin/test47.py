#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Filename: test47.py
# Author: peter.chen

def func(x):
    global y
    print 'X in the beginning of func(x): ',x
    x = 2
    y = 3
    print 'X in the end of func(x): ',x

x = 50
y = 100
func(x)
print 'X after calling func(x): ',x
print 'Y after calling func(x): ',y