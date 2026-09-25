import pandas as pd
from rdkit import Chem
from rdkit.Chem import AllChem
import os

df = pd.read_csv('SMILES.csv')

for i, row in df.iterrows():
    smi, lib = row['SMILES'], row['NUMBER']

    # Convert SMILES to molecule
    mol = Chem.MolFromSmiles(smi)

    # Add hydrogens
    mol = Chem.AddHs(mol)

    # Generate 3D conformation
    AllChem.EmbedMolecule(mol, AllChem.ETKDG())

    # Optimize conformation
    AllChem.UFFOptimizeMolecule(mol, 1000)

    # Create SDF writer
    os.makedirs('output_directory', exist_ok=True)
    writer = Chem.SDWriter(f'output_directory/ligand_{i+1}.sdf')

    # Set molecule properties
    #mol.SetProp('_Library', lib)
    mol.SetProp('_Name', f'ligand_{i+1}')
    #mol.SetProp('_SourceID', lib)
    mol.SetProp('_SMILES', smi)

    # Write molecule to SDF file
    writer.write(mol)

    # Close writer
    writer.close()
