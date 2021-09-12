#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 12 21:35:36 2021

@author: kimhuiseong
"""

print('Hellow world!')
#%%
# 은 comment 주석 이다. 문자열은 '',"" 둘다 사용가능
#%% 연습문제 1
print('Hellow world! \n을 사용하여 줄바꿈가능')
#%%
x=2
x=x+5
x=x-3
x=x*2.5
x=x/3
y=3
x+=y
print(x)
#%% 연습문제 2
x=2
x=x*x*x
#%%
L1 = list()
L2 = []

L3 = [3,4,1,6,7,5]
L4 = [[2,9,-5],[-1,9,4],[3,1,2]]
#%%
import numpy as np #npmpy 에 as를 사용해 np 라는 별칭을 붙여줌
nparray = np.zeros((5,5))
#%%
a=5
if a>0:
    print('a is greater than 0')
elif a==0:
    print('a is equal to 0')
else:
    print('a is lower than 0')
#%%
a=7
if a%3==0:
    print('3의로 나누어 떨어짐')
else:
    print('3의로 나누어 떨어지지 않음')