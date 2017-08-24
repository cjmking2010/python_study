#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Filename: test32.py
# Author: peter.chen

score = {
    'Mike':55,
    'Ben':72,
    'carol':98
}

print score['Ben']

for name in score:
    print score[name]

score['Ben'] = 91
score['Chris'] = 88
del score['Mike']
print score
