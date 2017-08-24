#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Filename: test39.py
# Author: peter.chen

geeks = ('Sheldon','Leonard','Rajesh','Howard')
for g in geeks:
    print g
print geeks[1:3]

def get_pos(n):
    return (n / 2,n * 2)
x,y = get_pos(50)
print x,y
pos = get_pos(50)
print pos[0],pos[1]
