#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Filename: lesson66_1.py
# Author: peter.chen

list_1 = [1,2,3,5,8,13,22]
list_2 = []
for i in list_1:
    if i % 2 == 0:
        list_2.append(i)
print list_2