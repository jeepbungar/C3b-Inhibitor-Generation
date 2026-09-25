#/bin/bash

shopt -s extglob
mkdir -p finished
for lig in !(avg.*)pdbqt; do
  python DockCluster_targeted.py $lig
  mv $lig finished/
done
