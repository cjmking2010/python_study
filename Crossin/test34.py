#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Filename: test34.py
# Author: peter.chen

def hello(name = 'world'):
    print 'hello ' + name

hello()
hello('python')

def func(a,b = 5):
    return a + b

print func(1)
print func(2,3)
