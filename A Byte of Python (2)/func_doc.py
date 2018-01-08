#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Filename: func_doc.py
# Author: peter.chen


def printMax(x,y):
    '''Prints the maximum of two numbers.

    The two values must be integers.'''
    x = int(x)  # convert to integers,if possible
    y = int(y)

    if x > y:
        print x,'is maximum'
    else:
        print y,'is maximum'

printMax(3,5)
print printMax.__doc__