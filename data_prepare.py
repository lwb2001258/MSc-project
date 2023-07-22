from rdkit import Chem
from chemprop.features.featurization import MolGraph
import time


def smilesToChem(smiles):
    return Chem.MolFromSmiles(smiles)


def smilestoMolGraph(smiles):
    mol = smilesToChem(smiles)
    return MolGraph(mol)


smiles = "C1CCCCC1"
graph = smilestoMolGraph(smiles)
time.sleep(10000)



