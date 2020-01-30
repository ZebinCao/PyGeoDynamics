#!/usr/bin/env python

##################################################
#           Main function for 1D problem
#               Zebin Cao, Jan 29, 2020
##################################################

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
    if settings['mesh'] == '0':
        mesh.unimesh()
    elif settings['mesh'] == '1':
        mesh_file = settings['mesh_file']
        mesh.readmesh(mesh_file)
    else:
        print('Unknown Mesh Type!!!\nExisting Code!!!\n')


##################################################
if __name__ == "__main__":
    main()
##################################################
