#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Filename: lambda.py
# Author: peter.chen

def make_repeater(n):
    return lambda s: s*n

twice = make_repeater(2)

print twice('word')
print twice(5)
