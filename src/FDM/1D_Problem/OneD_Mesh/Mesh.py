#!/usr/bin/env python

###################################################
#       Generate 1D mesh for calculation
#         Zebin Cao, Jan 29, 2020
###################################################
import numpy as np

class OneD_Mesh:

    def __init__(self, xlen=10.0, xnode=11):
        self.length = xlen
        self.nodes = xnode
        self.loc_x = np.zeros(self.nodes)


    def unimesh(self):
        dx = self.length / (self.nodes - 1)
        i = 0
        loc = 0.0

        while i < self.nodes:
            self.loc_x[i] = np.copy(loc)
            i += 1
            loc += dx


    def readmesh(self, meshfile):
        with open(meshfile) as fp:
            for line in fp:
                col1,col2 = line.split()
                if col1 == 'node':
                    continue
                else:
                    index = int(col1)
                    self.loc_x[index] = float(col2)

