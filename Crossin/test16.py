#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Filename: test16.py
# Author: peter.chen

print bool('False')
print bool(' ')
print bool(None)
print bool([])
print bool([0])

a = '123'
if a:
    print 'this is not a blank string'
