import random

import imblearn.over_sampling
from sklearn.datasets import make_classification
from collections import Counter
import pandas as pd
from imblearn.over_sampling import RandomOverSampler
import numpy as np
from rdkit import Chem








pd_read_csv = pd.read_csv("data/antimicrobial_data.csv")
print(type(pd_read_csv))
a = pd_read_csv["SMILES"].tolist()
x = []
for item in a:
    x.append([item])

b = np.array(x)

c = pd_read_csv['active'].to_numpy()
ros = RandomOverSampler(random_state=0)
X_resampled, y_resampled =ros.fit_resample(b,c)
X = X_resampled.reshape(1,len(X_resampled))[0]
Y = y_resampled.reshape(1,len(y_resampled))[0]
with open("data/cell_regression.csv") as f:
    content = f.readlines()
inhibition_info = {}
active_smiL_list = []
unactive_smiL_list = []
for index, line in enumerate(content):
    if index != 0:
        smiles = line.strip().split(",")[0]
        Mean_Inhibition = line.strip().split(",")[1]
        if float(Mean_Inhibition)<0.1:
            active_smiL_list.append(smiles)
        else:
            unactive_smiL_list.append(smiles)
        inhibition_info[smiles] = Mean_Inhibition
new_active_smile_list = []
for smi in active_smiL_list:
    mol = Chem.MolFromSmiles(smi)
    for _ in range(22):
        smi1 = Chem.MolToSmiles(mol, doRandom=True)
        new_active_smile_list.append(smi1)
        unactive_smiL_list.append(smi1)
        inhibition_info[smi1] = inhibition_info.get(smi)
random.shuffle(unactive_smiL_list)
f = open("data/enhance_regression3.csv" ,'w')
f.write("SMILES,Mean_Inhibition\n")
X = list(X)
random.shuffle(X)
for index, smiles in enumerate(unactive_smiL_list):
    f.write(smiles+","+str(inhibition_info.get(smiles))+"\n")




