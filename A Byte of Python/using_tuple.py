#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Filename: using_tuple.py

zoo = ('wolf','elephant','penguin')
print 'Numbser of animals in zoo is',len(zoo)

new_zoo = ('moneky','dolphin',zoo)
print 'Number of animals in the new zoo is',len(new_zoo)
print 'All animals in new zoo are',new_zoo
print 'Animals brought from old zoo are',new_zoo[2]
print 'Last animal brought from old zoo is',new_zoo[2][2]
