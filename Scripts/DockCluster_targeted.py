#!/usr/bin/env python

import os
import sys
import time

########################### NOTES ###############################################
# Docking Results From PDB Cluster Analysis after MD Simulations
#
# "ClusterCenter.txt" file is needed before running this program
#
# If "ClusterCenter.txt" is not present, Run GetSpecificCenter.py
#
#################################################################################

######################## USER DEFINED PARAMETERS ################################

SizeX        = 36
SizeY        = 36
SizeZ        = 36
Modes        = 1
Exhaust      = 16
CPU          = 8

#################################################################################

######################## MAIN PROGRAM ###########################################

StartTime = time.time() 

ParameterFile = open("ClusterCenter.txt", 'r')

for Parameter in ParameterFile:
    Parameter = Parameter.split()

    ReceptorName = Parameter[0]
    LigandName   = sys.argv[1]
    CenterX      = Parameter[1]
    CenterY      = Parameter[2]
    CenterZ      = Parameter[3]
    OutputName   = ReceptorName.replace(".pdbqt", "-" + LigandName)

    VinaCommand = "vina --receptor "                 + ReceptorName
    VinaCommand = VinaCommand + " --ligand "         + LigandName
    VinaCommand = VinaCommand + " --center_x "       + str(CenterX)
    VinaCommand = VinaCommand + " --center_y "       + str(CenterY)
    VinaCommand = VinaCommand + " --center_z "       + str(CenterZ)
    VinaCommand = VinaCommand + " --size_x "         + str(SizeX)
    VinaCommand = VinaCommand + " --size_y "         + str(SizeY)
    VinaCommand = VinaCommand + " --size_z "         + str(SizeZ)
    VinaCommand = VinaCommand + " --num_modes "      + str(Modes)
    VinaCommand = VinaCommand + " --exhaustiveness " + str(Exhaust)
    VinaCommand = VinaCommand + " --cpu "            + str(CPU)
    VinaCommand = VinaCommand + " --out "            + OutputName 

    os.system(VinaCommand)

ParameterFile.close()

EndTime = time.time() - StartTime
print("Time elapsed = " + str(EndTime) + " seconds")

###################################################################################
