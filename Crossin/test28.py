#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Filename: test28.py
# Author: peter.chen

word = 'helloworld'
for c in word:
    print c

print word[0]
print word[-2]

print word[5:7]
print word[:-5]
print word[:]

newword = ','.join(word)
print newword
