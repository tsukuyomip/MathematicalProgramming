#coding: utf-8

import sys
import numpy as np

class MyGraph(object):
    def __init__(self, n_nodes = None, edge = None, phi = None, rng = None):
        if n_nodes is None:
            n_nodes = 7
        if edge is None:
            edge = [
                [0, 1, 1, 1, 0, 0, 0],
                [1, 0, 1, 1, 0, 0, 0],
                [1, 1, 0, 1, 0, 0, 0],
                [1, 1, 1, 0, 1, 0, 0],
                [0, 0, 0, 1, 0, 1, 0],
                [0, 0, 0, 0, 1, 0, 1],
                [0, 0, 0, 0, 0, 1, 0]
            ]
        if phi is None:
            phi = self.phi_1
            #phi = self.phi_2
        if rng is None:
            print >> sys.stderr, "warning(MyGraph.__init__()): rng is None. set rng to np.random"
            rng = np.random

        self.n_nodes = n_nodes
        self.edge = edge
        self.phi = phi
        self.rng = np.random

    def walk(self, start = None, goal = None):
        if start is None:
            print >> sys.stderr, "error(MyGraph.walk()): start is None."
            return None
        if goal is None:
            print >> sys.stderr, "error(MyGraph.walk()): goal is None."
            return None
        if (start < 0 or start >= self.n_nodes):
            print >> sys.stderr, "error(MyGraph.walk()): start out of range."
            return None
        if (goal < 0 or goal >= self.n_nodes):
            print >> sys.stderr, "error(MyGraph.walk()): goal out of range."
            return None

        # 遷移確率の計算
        sum_phi = 0.0
        p = np.array([])
        #print "start is", start
        for i in self.edge[start]:
            if i == 0:
                p = np.append(p, 0)
            else:
                deg = self.phi(i)
                p = np.append(p, deg)
                sum_phi += deg
        p = p/sum_phi

        next_node = self.select_with_prob(p, rng = self.rng)
        if next_node == goal:
            return 1

        return self.walk(next_node, goal) + 1

    def phi_1(self, index = None):
        """phi(x) = deg(x). nodeのdegを返す．"""
        if index is None:
            print >> sys.stderr, "error(MyGraph.phi_1()): index is None."
            return None

        retval = 0
        for i in (self.edge[index]):
            retval += i
        return retval

    def phi_2(self, index = None):
        """phi(x) = 1. 常に1を返す．"""
        return 1



    def select_with_prob(self, p = None, rng = None):
        if p is None:
            print >> sys.stderr, "error(MyGraph.select_with_prob()): p is None."
            return None
        if rng is None:
            print >> sys.stderr, "warning(MyGraph.select_with_prob()): rng is None. set 'rng' to 'np.random'"
            rng = np.random

        r = rng.rand()
        for i in xrange(len(p)):
            r -= p[i]
            if r < 0.0:
                return i

        print >> sys.stderr, "warning(MyGraph.select_with_prob()): maybe sum(p) > 1.0"
        return len(p) - 1

