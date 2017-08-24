#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Filename: lesson55.py
# Author: peter.chen

import re
text = "Hi,I am Shirley Hiltion.I am his wife."
m1 = re.findall(r"hi",text)
if m1:
    print m1
else:
    print 'not match'

m2 = re.findall(r"\bhi\b",text)
if m2:
    print m2
else:
    print 'not mathc'

m3 = re.findall(r"[Hh]i",text)
if m3:
    print m3
else:
    print 'not mathc'
