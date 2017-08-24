#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Filename: lesson73.py
# Author: peter.chen

sum = 0
for i in range(1,101):
    sum += i
print sum


lst = xrange(1,101)
def add(x,y):
    return x + y
print reduce(add,lst)