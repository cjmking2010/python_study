#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Filename: test13.py
# Author: peter.chen

for i in range(0,3):
    for j in range(0,3):
        print i,j

for i in range(0,5):
    for j in range(0,5):
        print '*',
    print

for i in range(0,5):
    for j in range(0,i + 1):
        print '*',
    print
