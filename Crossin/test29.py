#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Filename: test29.py
# Author: peter.chen

scores = [71,99,59,65]

for s in scores:
    print s
    if s < 60:
        break

a = 1
sum = 0
while a < 10:
    sum += a
    print a,sum
    if sum > 10:
        break
    a += 1
