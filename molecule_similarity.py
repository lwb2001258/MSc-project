import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib as plt
from rdkit.Chem import AllChem as Chem
from rdkit.Chem.Draw import IPythonConsole
from rdkit.Chem import PandasTools
from rdkit.Chem import Draw
from rdkit import DataStructs

def compare_similarity(smiles, radis):
    data = pd.read_csv('data/antimicrobial_active_smiles.csv', sep=',')
    PandasTools.AddMoleculeColumnToFrame(data,'SMILES','Molecule',includeFingerprints=True)
    fplist = []
    for mol in data['Molecule']:
        fp = Chem.GetMorganFingerprintAsBitVect( mol,radis )
        fplist.append(fp)
    data['mfp2']=fplist
    mol = Chem.MolFromSmiles(smiles)
    fp1 = Chem.GetMorganFingerprintAsBitVect( mol,radis)
    for fp2 in data['mfp2']:
        print(DataStructs.DiceSimilarity(fp1,fp2))
smiles = "NC(=O)c1cc[n+](CC2=C(N3[C@H](SC2)[C@H](NC(=O)Cc2cccs2)C3=O)C(O)=O)cc1"
compare_similarity(smiles,2)
mol = Chem.MolFromSmiles(smiles)
img = Draw.MolToImage(mol)
data = pd.read_csv('data/antimicrobial_active_smiles.csv', sep=',')
smis = data['SMILES']
mols = []
for smi in smis:
    mols.append(Chem.MolFromSmiles(smi))
img = Draw.MolToImage(mols[0])
img.save('test.png')
img = Draw.MolsToGridImage(mols,subImgSize=(500,500),returnPNG=False)
img.save("active_mols.png")
img.show()



    # fp1=data.at[0,'mfp2']
    # fp2=data.at[1,'mfp2']
    # from rdkit import DataStructs
    # fps = []
    # for index1, fp1 in enumerate(data['mfp2']):
    #     fps_item = []
    #     for index2, fp2 in enumerate(data['mfp2']):
    #         if index1 != index2:
    #             fps_item.append(DataStructs.DiceSimilarity(fp1, fp2))
    #     fps.append(max(fps_item))
    # print(fps)




