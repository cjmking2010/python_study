#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Filename: lesson37.py
# Author: peter.chen

score = {
    '萧锋':95,
    '段誉':97,
    '虚竹':89
}
print score['段誉']

for name in score:
    print score[name]

score['虚竹'] = 91
score['慕容复'] = 88
del score['萧锋']

for name in score:
    print name,score[name]
