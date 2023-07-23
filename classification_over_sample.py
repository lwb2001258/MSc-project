import random

import imblearn.over_sampling
from sklearn.datasets import make_classification
from collections import Counter

X, y = make_classification(n_samples=5000, n_features=2, n_informative=2,
                           n_redundant=0, n_repeated=0, n_classes=3,
                           n_clusters_per_class=1,
                           weights=[0.01, 0.05, 0.94],
                           class_sep=0.8, random_state=0)
print(X)
print(type(X))
print(y)
print(type(y))
# Counter(y)

#
from imblearn.over_sampling import RandomOverSampler

ros = RandomOverSampler(random_state=0)
X_resampled, y_resampled = ros.fit_resample(X,y)

sorted(Counter(y_resampled).items())

# [(0, 4674), (1, 4674), (2, 4674)]

import pandas as pd
from imblearn.over_sampling import RandomOverSampler
import numpy as np
from imblearn.over_sampling import *


pd_read_csv = pd.read_csv("data/antimicrobial_data.csv")
a = pd_read_csv["SMILES"].tolist()
x = []
for item in a:
    x.append([item])
b = np.array(x)
c = pd_read_csv['active'].to_numpy()
ros = RandomOverSampler(random_state=0)
X_resampled, y_resampled =ros.fit_resample(b,c)
X = X_resampled.reshape(1,len(X_resampled))[0]
with open("data/antimicrobial_data.csv") as f:
    content = f.readlines()
smiles_info ={}
for index,line in enumerate(content):
    if index!=0:
        smiles = line.strip().split(',')[0]
        active = int(line.strip().split(',')[1])
        smiles_info[smiles] = active
Y = y_resampled.reshape(1,len(y_resampled))[0]
f = open("data/antimicrobial_oversampling_data.csv", 'w')
f.write("SMILES,active\n")
X = list(X)
random.shuffle(X)
for index, smiles in enumerate(X):
    f.write(smiles+","+str(smiles_info.get(smiles))+"\n")



