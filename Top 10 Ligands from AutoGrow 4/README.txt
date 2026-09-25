# Contact Analysis

This directory contains the molecular structures and visualization files for the ten ligands selected for detailed protein-ligand interaction and contact analysis.

## Files

### `Top_10_Ligands/`

Contains the protein-ligand structures of the ten selected ligands in `.pdb` format.

Each `.pdb` file contains the corresponding protein-ligand structure used for protein-ligand contact and interaction analysis.

The ligand identifiers in the filenames correspond to those used throughout the manuscript and other deposited datasets.

### `PLIP/`

Contains files associated with protein-ligand interaction analysis and visualization.

* `interactions.csv` – Machine-readable summary of the protein-ligand interactions identified for the selected compounds.
* `top10_interactions.pse` – PyMOL session file containing the structures and visualization of the protein-ligand interactions for the selected ligands.

## Data Format

Protein-ligand structures are provided in `.pdb` format. Interaction results are provided in `.csv` format for machine-readable access. The `.pse` file is provided as a PyMOL session file for visualization of the analyzed structures and interactions.

The protein-ligand interaction analysis and criteria used for compound prioritization are described in the Methods section of the manuscript.

## Relationship to the Screening Workflow

The structures provided here correspond to the ten compounds selected for detailed protein-ligand interaction analysis following the preceding virtual screening and filtering stages.

AutoGrow4 generation and filtering
→ QED filtering
→ ensemble docking
→ ADMETox evaluation
→ selection of top compounds
→ protein-ligand contact and interaction analysis

The files in this directory provide the structural and interaction data associated with the protein-ligand contact analysis stage.
