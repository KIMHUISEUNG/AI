#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 11 15:09:43 2021

@author: kimhuiseong
"""

import random #random 라이브러리 파일을 import로 사용선언

yut=['xxxx', 'xxxo', 'xxox', 'xxoo', 'xoxx', 'xoxo', 'xoox', 'xooo', 'oxxx', 'oxxo', 'oxox', 'oxoo', 'ooxx', 'ooxo', 'ooox', 'oooo'] #yut이라는 변수에 다양한 경우의수 배열생성

throw = random.choice(yut) #random라이브러리의 choice라는 메서드를 호출 사용법에 따라 ()안에 yut 배열을 집어넣음 이후 throw던지기라는 기능생성

print(throw) #throw 값을 출력

n=throw.count('o') # throw.count == random.choice(yut).count 와 같다고 할 수 있다. throw 의 값의 count를 계산하며 그것을 n에 담는다.

if n==4:
    print('모')  # '0000' 이 4개라면 '모' 출력
elif n==3:
    print('도') # '000' 이 3개라면 '도' 출력
elif n==2:
    print('개') # '00' 이 2개라면 '개' 출력
elif n==1:
    print('걸') # '0' 이라면 '걸' 출력
else:
    print('윷') # '0' 이 없다면 '윷' 출력

#n의 값에 따라 모,도,개,걸,윷 중 값을 출력