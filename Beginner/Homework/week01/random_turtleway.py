#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 11 15:58:33 2021

@author: kimhuiseong
"""
screen = turtle.Screen()
screen.setup(1000,1000)
screen.tracer(0,0)

#%% list array setting
walkers = list()
n = 20
for i in range(n):
    walkers.append(turtle.Turtle())
for i in range(n):
    walkers[i].color((random.uniform(0,1), random.uniform(0,1), random.uniform(0,1)))

#%% random_walk() method setting                 
def random_walk():
    for i in range(n):
        angle = random.randint(0,3)*90
        walkers[i].seth(angle)
        walkers[i].fd(10)
    screen.update()
    screen.ontimer(random_walk,1000//20)

#%% run
random_walk()