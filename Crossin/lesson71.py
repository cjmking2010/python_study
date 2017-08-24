#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Filename: lesson71.py
# Author: peter.chen

def func():
    global x
    print 'X in the beginning of func(x): ',x
    x = 2
    print 'X in the end of func(x): ',x

x = 50
func()
print 'X after calling func(x): ',x