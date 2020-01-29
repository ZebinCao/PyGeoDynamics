#!/usr/bin/env python

###################################################
#       Generate 1D mesh for calculation
#         Zebin Cao, Jan 29, 2020
###################################################

class 1D_Mesh:

    def __init__(self, length, nodes):
        import numpy as np
        self.length = length
        self.nodes = nodes
        self.loc_x = np.zeros(self.nodes)

    def unimesh(self):
        dx = self.length / (self.nodes - 1)

        i = 0
        loc = 0.0
        for i < self.nodes:
            self.loc_x[i] = np.copy(loc)
            i += 1
            loc += dx
