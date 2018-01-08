#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Filename: func_param.py
# Author: peter.chen

def printMax(a,b):
    if a > b:
        print a,'is maximum'
    else:
        print b,'is maximum'

printMax(3,4)  # directly give literal values

x = 5
y = 7

printMax(x,y)  # give varables as arguments
