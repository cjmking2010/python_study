#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Filename: test19.py
# Author: peter.chen

def isEqual(num1,num2):
    if num1 < num2:
        return False;
    if num1 > num2:
        return False;
    if num1 == num2:
        return True

a = isEqual(3,5)
b = isEqual(7,7)
print a
print b
