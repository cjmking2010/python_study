#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Filename: lesson62.py
# Author: peter.chen

import random
a = 0
for i in range(25):
    print 'i: %d' % i
    b = random.choice(range(5))
    print 'b: %d' % b
    a += i / b
    print
print a