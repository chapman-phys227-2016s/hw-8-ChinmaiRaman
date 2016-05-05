#! /usr/bin/env python

"""
File: disorder2
Copyright (c) 2016 Chinmai Raman
License: MIT
Course: PHYS227
Assignment: 8.37
Date: April 26th, 2016
Email: raman105@mail.chapman.edu
Name: Chinmai Raman
Description: Implements a random walk class that can handle boundaries. THANK YOU MICHAEL!!!!
"""

from Particles import Particles
import sys
import subprocess

if len(sys.argv) < 1:
    num_frames = 1
else:
    num_frames = sys.argv[1]

p = Particles()
for i in xrange(-99, -1):
    for j in xrange(-99,99):
        p.add_particle(i, j)

p.generate_frame()
for i in xrange(int(num_frames)):
    for j in xrange(20):
        p.move()
    p.generate_frame()

subprocess.call("convert -delay 1 -loop 0 *.png gas.gif", shell=True)
subprocess.call("rm *.png", shell=True)