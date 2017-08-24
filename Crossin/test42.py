#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Filename: test42.py
# Author: peter.chen

import random

print random.randint(1,100)
print random.random()
print random.uniform(3,1.5)
print random.choice([1,2,3,5,8,13])
print random.choice('hello')
print random.randrange(1,9,2)

li = [1,2,3,4,5]
print random.shuffle(li)
print li
