#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Filename: lesson9.py
# Author: peter.chen

from random import randint

num = randint(1,100)

print 'Guess what I think?'
bingo = False

while bingo == False:
    answer = input()

    if answer < num:
        print 'too small!'

    if answer > num:
        print 'too big!'

    if answer == num:
        print 'BINGO'
        bingo = True
