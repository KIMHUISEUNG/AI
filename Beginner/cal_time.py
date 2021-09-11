#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 11 14:38:53 2021

@author: kimhuiseong
"""

import time

start = time.time()
sum = 0
for i in range(1,100000001):
    sum += i
    
end = time.time()

print('1+2+...+10000000=', sum)
print('소요 시간은 ', end - start,'초입니다.')