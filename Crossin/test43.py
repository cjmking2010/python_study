#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Filename: test43.py
# Author: peter.chen

import time
starttime = time.time()
print 'start:%f' % starttime
for i in range(10):
    print i
endtime = time.time()
print 'end:%f' % endtime
print 'total time:%f' % (endtime - starttime)