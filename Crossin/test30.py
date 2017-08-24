#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Filename: test30.py
# Author: peter.chen

scores = [71,99,59,65]
sum = 0
for s in scores:
    if s < 60:
        continue
    sum += s
    print s,sum
