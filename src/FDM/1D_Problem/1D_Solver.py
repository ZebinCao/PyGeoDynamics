#!/usr/bin/env python

##################################################
#           Main function for 1D problem
#               Zebin Cao, Jan 29, 2020
##################################################
import numpy as np

def main():

    import sys,os
    from OneD_Problem_Parser.Parser import OneD_Parser as parser
    from OneD_Mesh.Mesh import OneD_Mesh

    # Define model settings
    param = sys.argv[1]

    print("PyGeoDynamics: 1D Problem Solver")

    # Start reading parameters
    print("Start reading model setting: %s" %(param))

    infile = parser(param)
    settings = infile.parse_file()

    # Generate Mesh
    xlen = float(settings['length'])
    nodes = int(settings['nodes'])
    mesh = OneD_Mesh(xlen,nodes)

    if settings['mesh_type'] == '0':
        mesh.unimesh()
    elif settings['mesh_type']== '1':
        mesh.readmesh(settings['meshfile'])
    else:
        print("Unknown mesh type!!!\n Exiting code!!!\n")
        sys.exit()

    # Determine the solver and solve it

    ## Solve for 1D thermal conduction problem
    if settings['solver'] ==  'conduction':
        from OneD_Thermal_Conduction.OneD_Thermal_Conduction import OneD_thermal_conduction as tc
        print("Solve 1D thermal conduction problem")
        alpha = float(settings['therm_cond'])
        t_field = tc(alpha, mesh.nodes, mesh.loc_x)

        if settings['TIC_type'] == '0':
            t_max = float(settings['TIC_max'])
            t_min = float(settings['TIC_min'])
            t_field.linearIC(t_max,t_min)
        elif settings['TIC_type'] == '1':
            t_max = float(settings['TIC_max'])
            t_bg = float(settings['TIC_bg'])
            loc_index =  int(settings['TIC_per_loc'])
            t_field.deltaIC(t_max, t_bg, loc_index)
        else:
            print("Unknown IC type!!!\n Exiting code!!!\n")
            sys.exit()

        steps = int(settings['steps'])
        dt = float(settings['time_step'])
        output_fre = int(settings['output_frequency'])
        if settings['TBC_type'] == '0':
            tbc_0 = float(settings['TBC_temp_0'])
            tbc_1 = float(settings['TBC_temp_1'])
            t_field.solve_temp_TBC(steps, dt, tbc_0, tbc_1, output_fre, settings['output_name'])
        elif settings['TBC_type'] == '1':
            flux_0 = float(settings['TBC_flux_0'])
            flux_1 = float(settings['TBC_flux_1'])
            t_field.solve_flux_TBC(steps, dt, flux_0, flux_1, output_fre, settings['output_name'])
        else:
            print('Unknown TBC type!!!\n Exiting code!!!\n')

##################################################
if __name__ == "__main__":
    main()
##################################################
