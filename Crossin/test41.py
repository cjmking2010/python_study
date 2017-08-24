#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Filename: test41.py
# Author: peter.chen

import re

text = "Hi, I am Shirley Hilton. I am his wife."
m = re.findall(r"\b[Hh]i",text)
if m:
    print m
else:
    print 'not match'

n = re.findall(r"I.*?e",text)
if n:
    print n
else:
    print 'not match'
