#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Filename: test35.py
# Author: peter.chen

class MyClass:
    name = 'Sam'

    def sayHi(self):
        print 'Hello %s' % self.name

mc = MyClass()
print mc.name
mc.sayHi()
