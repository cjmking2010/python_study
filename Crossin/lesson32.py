#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Filename: lesson32.py
# Author: peter.chen

f = file('data.txt')
data = f.read()
out = file('lesson32_txt1.txt','w')
out.write(data)
out.close()
f.close()

out2 = file('lesson32_txt2.txt','w')
data2 = raw_input('Please enter some words: ')
out2.write(data2)
out2.close()
