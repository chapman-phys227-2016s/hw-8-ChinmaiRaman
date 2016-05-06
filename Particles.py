#! /usr/bin/env python

"""
File: Particles.py
Copyright (c) 2016 Chinmai Raman
License: MIT
Course: PHYS227
Assignment: 8.37
Date: May 2, 2016
Email: raman105@mail.chapman.edu
Name: Chinmai Raman
Description: Moves and plots many instances of class particle
"""

import matplotlib
matplotlib.use('Agg')
import time
import numpy as np
import matplotlib.pyplot as plt
import sys
from unittest import TestCase

class Particles:
    """
    Moves and plots particles
    """
    def __init__(self, seed = 0):
        self.x_pos = np.zeros(0)
        self.y_pos = np.zeros(0)
        self.x_lim = [-100, 100]
        self.y_lim = [-100, 100]
        self.step = 0
        if seed == 0:
            self.RNG = np.random.RandomState(np.random.randint(1000000))
        else:
            self.RNG = np.random.RandomState(seed)

    def add_particle(self, x0 = 0, y0 = 0):

        self.x_pos = np.append(self.x_pos, x0)
        self.y_pos = np.append(self.y_pos, y0)

    def move(self, stepsize = 1):
        directions = self.RNG.randint(1, 5, len(self.x_pos))
        x_move = np.zeros(len(self.x_pos))
        y_move = np.zeros(len(self.y_pos))
        x_move[directions == 1] = stepsize
        x_move[directions == 2] = -1 * stepsize
        y_move[directions == 3] = stepsize
        y_move[directions == 4] = -1 * stepsize

        self.x_pos += x_move
        self.y_pos += y_move

        bound_x = np.where(abs(self.x_pos > 99))
        bound_y = np.where(abs(self.y_pos > 99))
        self.x_pos[bound_x] -= x_move[bound_x]
        self.y_pos[bound_y] -= y_move[bound_y]

        self.step += 1

        barrier = np.where(self.x_pos == 0)

        hole_var = (self.x_pos * 999999) + self.y_pos
        hole = np.where(abs(hole_var) <= 10)

        self.x_pos[hole] += x_move[hole]
        self.y_pos[hole] += y_move[hole]

        self.x_pos[barrier] -= x_move[barrier]
        self.y_pos[barrier] -= y_move[barrier]

    def generate_frame(self):
        fig, ax = plt.subplots(nrows = 1, ncols = 1)
        ax.plot(self.x_pos, self.y_pos, 'r.')
        ax.set_ylim(self.y_lim)
        ax.set_xlim(self.x_lim)
        fig.savefig('tmp_%05d.png' % (self.step))
        plt.close(fig)

class Test_Particles(TestCase):
    def test_Particle(self):
        test_seed = int(time.time())
        print test_seed
        rng = np.random.RandomState(test_seed)
        particles_1 = Particles(test_seed)
        particles_2 = Particles(test_seed)

        for i in xrange(5):
            particles_1.add_particle(50, i)
            particles_2.add_particle(50, i)

        for i in xrange(10):
            particles_1.move()
            particles_2.move()

        check = (particles_1.x_pos == particles_2.x_pos).all() and (particles_1.y_pos == particles_2.y_pos).all()
        msg = "Failure"
        assert check, msg