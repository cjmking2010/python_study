#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Filename: test37.py
# Author: peter.chen

class Vehicle:
    speed = 60.0

    def drive(self,distance):
        time = distance /self.speed
        print time

class Bike(Vehicle):
    speed = 25.0

class Train(Vehicle):
    speed = 200.0
    fuel = 500.0

bike = Bike()
bike.drive(1000.0)

train = Train()
train.drive(1000.0)
print train.fuel
