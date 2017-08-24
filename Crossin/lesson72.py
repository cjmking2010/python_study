#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Filename: lesson72.py
# Author: peter.chen

lst_1 = [1,2,3,4,5,6]
lst_2 = []
for item in lst_1:
    lst_2.append(item * 2)
print lst_2

lst_1 = [1,2,3,4,5,6]
lst_2 = [i * 2 for i in lst_1]
print lst_2

lst_1 = (1,2,3,4,5,6)
lst_2 = map(lambda x: x * 2,lst_1)
print lst_2

lst_1 = [1,2,3,4,5,6]
lst_2 = [1,3,5,7,9,11]
lst_3 = map(lambda x,y: x + y,lst_1,lst_2)
print lst_3

lst_1 = [1,2,3,4,5,6]
lst_2 = [1,3,5,7,9,11]
lst_3 = map(None,lst_1)
print lst_3
lst_4 = map(None,lst_1,lst_2)
print lst_4