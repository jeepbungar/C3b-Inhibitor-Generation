#!/usr/bin/env python

import os

os.system("ls *.pdbqt > PDBList.tmp")

CenterX = ""
CenterY = ""
CenterZ = ""

StoreArray = []

ListFile = open("PDBList.tmp", 'r')

for ListLine in ListFile:
    ListLine = ListLine.replace("\n", "")

    PDBFile = open(ListLine, 'r')

    for AtomLine in PDBFile:
        #modify this lines
        if "OD1 ASP   346" in AtomLine:
            AtomArray = AtomLine.split()

            CenterX = str(AtomArray[5])
            CenterY = str(AtomArray[6])
            CenterZ = str(AtomArray[7])

            ToAppend = ListLine + " " + CenterX + " " + CenterY + " " + CenterZ
            StoreArray.append(ToAppend + "\n")

    PDBFile.close()

ListFile.close()

CenterList = open("ClusterCenter.txt", 'w')

CenterList.writelines(StoreArray)

CenterList.close()

os.system("rm PDBList.tmp")
