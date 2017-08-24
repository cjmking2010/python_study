#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Filename: test44.py
# Author: peter.chen

list_1 = [1,2,3,5,8,13,22]
list_2 = [i/2 for i in list_1 if i % 2 == 0]
print list_2

list = []
for i in range(1,101):
    if i % 2 == 0:
        if i % 3 == 0:
            if i % 5 == 0:
                list.append(str(i))
print ';'.join(list)

print ';'.join([str(i) for i in range(1,101) if i % 2 == 0 and i % 3 == 0 and i % 5 == 0])