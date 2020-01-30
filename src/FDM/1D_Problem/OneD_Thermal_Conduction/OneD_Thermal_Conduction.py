#!/usr/binenv  python


#######################################################
#           1D thermal conduction solver
#             Zebin Cao, Jan 29, 2020
#######################################################
import numpy as np

class OneD_thermal_conduction:

    def __init__(self, alpha, nodes, loc):
        self.alpha = alpha
        self.nodes =  nodes
        self.loc_x = loc
        self.t = np.zeros(self.nodes)


    def linearIC(self, t_max, t_min):
        i = 0
        dt = (t_max - t_min) / (self.nodes - 1)
        t = t_max

        while i < self.nodes:
            self.t[i] = np.copy(t)
            i += 1
            t -= dt

    def deltaIC(self, t_max, t_bg, loc_index):
        i = 0 

        while  i < self.nodes:
            if i == loc_index:
                self.t[i] = t_max
            else:
                self.t[i] = t_bg
            i += 1


    def solve_temp_TBC(self, steps, dt, temp0, temp1, fre, name):
        current_step = 0
        current_t = 0.0
        temp_t = np.zeros(self.nodes)

        output_name = name + '%d.txt' %(current_step)
        self.save(current_step, current_t, output_name)

        if dt == 0:
            print("Find suitable stable dt")
            dx_min = 1000.0
            j = 0
            while j < self.nodes - 1:
                dx_temp = self.loc_x[j+1] - self.loc_x[j]
                if dx_temp < dx_min:
                    dx_min = np.copy(dx_temp)
                j += 1
            dt = 0.4 * dx_min**2 / self.alpha 
            print("The suitable stable dt is: %f" %(dt))

        while current_step <= steps:
            i = 1
            temp_t[0] = temp0
            temp_t[self.nodes - 1] = temp1
            while i < (self.nodes - 1):
                dx_1 = self.loc_x[i] - self.loc_x[i-1]
                dx_2 = self.loc_x[i+1] - self.loc_x[i]
                dx_3 = 0.5 * (dx_1 + dx_2)
                dtemp_1 = self.t[i] - self.t[i-1]
                dtemp_2 = self.t[i+1] - self.t[i]
                flux_1 = dtemp_1 / dx_1
                flux_2 = dtemp_2 / dx_2
                grad_flux = (flux_2 - flux_1) / dx_3
                temp_t[i] = self.t[i] + self.alpha * dt * grad_flux
                i += 1
            self.t = np.copy(temp_t)
            temp_t = np.zeros(self.nodes)
            current_step += 1
            current_t += dt
            if current_step % fre == 0 or  current_step == steps:
                output_name = name + '%d.txt' %(current_step)
                self.save(current_step, current_t, output_name)

    def solve_flux_TBC(self, steps, dt, temp0, temp1, fre, name):
        return

    def save(self, step, time, name):
        print('Outputing results at step: %d' % (step))
        fp = open(name,'w')
        fp.write("Results at step: %d\n" %(step))
        fp.write("at simulation time: %f\n" %(time))
        fp.write("NO.node   x_location  temperature\n")
        for i in range(self.nodes):
            fp.write("%d    %f  %f\n" %(i,self.loc_x[i],self.t[i]))
