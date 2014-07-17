#coding: utf-8

import sys
import numpy as np
import MyGraph as mg

if __name__ == "__main__":
    N_EXP = 2000
    start = 3
    goal = 6
    rng = np.random.RandomState(22294322)

    g = mg.MyGraph(rng = rng)

    sum_step = 0
    for i in xrange(N_EXP):
        sum_step += g.walk(start = start, goal = goal)
        print >> sys.stderr, i, "/", N_EXP

    print float(sum_step)/N_EXP
