#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Filename: lesson65_2.py
# Author: peter.chen

import pickle

f = file('test.data')
test_data = pickle.load(f)
f.close()

print test_data