# AutoGrow4 Results

This directory contains the molecular structures and screening results generated from five independent AutoGrow4 runs used in the computational prioritization workflow.

Each run (`Run_1` through `Run_5`) is provided in a separate directory. The files document the progression of compounds through the initial AutoGrow4 docking-based filtering and subsequent QED filtering.

## Directory Structure

* `Run_1/` – AutoGrow4 run 1
* `Run_2/` – AutoGrow4 run 2
* `Run_3/` – AutoGrow4 run 3
* `Run_4/` – AutoGrow4 run 4
* `Run_5/` – AutoGrow4 run 5

## Files in Each Run

### `all_compounds.smi`

Contains the molecular structures generated during the corresponding AutoGrow4 run, represented as SMILES strings.

### `Run X_Passed QED.csv`

Contains compounds that passed the initial AutoGrow4 docking/binding-energy filtering criterion. The file includes the following information:

* Ligand identifier
* Ensemble docking score
* Standard deviation of ensemble docking score
* SMILES
* AutoGrow4 docking score
* Molecular weight
* QED
* Compound name
* Compound origin

The QED values are provided for characterization of the compounds following the initial AutoGrow4 filtering.

### `Run X Passed Docking.csv`

Contains the subset of compounds from the corresponding AutoGrow4 run that passed the QED filtering criterion and were subsequently retained for ensemble docking and further computational evaluation.

The file contains the same fields as the corresponding `Passed QED` file, including ligand identifier, docking scores, SMILES, molecular weight, QED, compound name, and compound origin.

## Filtering Workflow

The files represent sequential stages of the computational screening workflow:

AutoGrow4 compound generation
→ AutoGrow4 docking/binding-energy filtering
→ QED filtering
→ ensemble docking
→ ADMETox evaluation
→ subsequent compound prioritization

The ensemble docking and ADMETox results are provided separately in the corresponding filtering/results directory of the repository.

## Data Format

Molecular structures are provided as SMILES strings in `.smi` format. Screening and filtering results are provided as `.csv` files to facilitate machine-readable access and reuse.

The AutoGrow4 parameters, docking protocol, and filtering criteria are described in the Methods section of the manuscript.

Temporary AutoGrow4 files and intermediate files not required to interpret the reported results are not included.
