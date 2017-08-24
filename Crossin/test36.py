#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Filename: test36.py
# Author: peter.chen

class Car:
    speed = 60.0

    def drive(self,distance):
        time = distance / self.speed
        print time

car = Car()
car.drive(100.0)
car.drive(200.0)
