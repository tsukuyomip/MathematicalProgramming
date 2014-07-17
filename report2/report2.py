#coding: utf-8

import sys
import numpy as np
import pylab as pl
import MyGraph as mg

if __name__ == "__main__":
    N_EXP = 5000
    start = 3
    goal = 6

    hist_bins = 100
    hist_alpha = 0.3
    rng = np.random.RandomState(22294322)

    g = mg.MyGraph(rng = rng)

    n_steps = []
    for i in xrange(N_EXP):
        tmp_step = 0
        next_node = start
        while(next_node != goal):
            next_node = g.walk(start = next_node, goal = goal)
            tmp_step += 1
        n_steps.append(tmp_step)

        if i%100 == 0:
            print >> sys.stderr, i, "/", N_EXP

    print float(sum(n_steps))/N_EXP

    pl.hist(n_steps, bins = hist_bins, alpha=hist_alpha, histtype='stepfilled', color='b')
    pl.xlabel("Number of steps")
    pl.ylabel("Frequency")
    pl.show()
