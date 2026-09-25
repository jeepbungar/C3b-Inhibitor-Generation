#Correct script for conversion

import os

current_dir = os.getcwd()

for filename in os.listdir(current_dir):
  if filename.endswith(".sdf"):
    file_name, extension = os.path.splitext(filename)
    output_filename = file_name + ".pdb"

    command = "babel -i sdf " + filename + " -o pdb " + output_filename + " --gen3D"
    os.system(command)

print("Successfully converted all .sdf files to .pdb files.")
