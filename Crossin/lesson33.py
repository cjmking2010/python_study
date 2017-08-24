#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Filename: lesson33.py
# Author: peter.chen

f = file('scores.txt')
lines = f.readlines()
#print lines
f.close()

results = []

for line in lines:
    data = line.split()

    sum = 0
    for score in data[1:]:
        sum += int(score)
    result = '%s \t: %d\n' % (data[0],sum)
#    print result

    results.append(result)
#print results

output = file('result.txt','w')
output.writelines(results)
output.close()
