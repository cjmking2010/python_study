#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Filename: test38.py
# Author: peter.chen

a = 3
result = (a > 0) and "big" or "small"
print result

a = 0
b = 17
c = True and a or b
d = (True and [a] or [b])[0]
print c,d
