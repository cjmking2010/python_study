#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Filename: test45.py
# Author: peter.chen

def func(arg1=1,arg2=2,arg3=3):
    print arg1,arg2,arg3

func(2,3,4)
func(5,6)
func(7)
func(arg2=8)
func(arg3=9,arg1=10)
func(11,arg3=12)

def printAll(*args):
    for i in args:
        print i,
        print

printAll(1,2,3)
printAll(3,2)

def mixed(x,y=5,*a,**b):
    print x,y,a,b

mixed(1,y=1)
mixed(1,2,3,a=1)
mixed(1,2,3,4,k=1,t=2,o=3)