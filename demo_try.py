from chemprop.data import MoleculeDataLoader,get_data,MoleculeDataset,MoleculeDatapoint
from GCNmodel import *
from chemprop.features import MolGraph
from rdkit import Chem


data = get_data("data/cell_classification3.csv")
data.targets()
data.smiles()
# data = MoleculeDataset([MoleculeDatapoint(["C1CCCCC1"],["1.0"])
                           # ,MoleculeDatapoint(["CCCCCCCCCC"],["0.0"])
                        # ])
# def getMolGraph(data):
#     molGraphList=[]
#     for data_item in data:
#         smilesList = data_item.smiles
#         targetList = data_item.targets
#         for index, smiles in enumerate(smilesList):
#             mol = Chem.MolFromSmiles(smiles)
#             moleculeGraph = MolGraph(mol)
#             molGraphList.append((moleculeGraph, targetList[index]))
#     return molGraphList
# molGraphList = getMolGraph(data)
moleculeDataLoader = MoleculeDataLoader(dataset=data,batch_size=20,num_workers=0,shuffle=True)

model = Net(150,2)
for moleculeBatch in moleculeDataLoader:
    moleculeBatch


# for molGraph in molGraphList:
#     a = molGraph[0].a2b
#     atom_bond_info = {}
#     for index, item in enumerate(self.a2b):
#         for bond_index in item:
#             if bond_index%2 == 0:
#                 bond_index = int(bond_index/2)
#             else:
#                 bond_index = int(bond_index/2)
#
#             if not atom_bond_info.get(index):
#                 atom_bond_info[index] = []
#             atom_bond_info[index].append(bond_index)
#     bond_connect_info = {}
#     for atom in atom_bond_info.keys():
#         bond_list = atom_bond_info.get(atom)
#         for bond in bond_list:
#             if not bond_connect_info.get(bond):
#                 bond_connect_info[bond] = []
#             bond_connect_info[bond].append(atom)
#     edge_index =torch.tensor(list( bond_connect_info.values()),dtype=torch.long).T









    print(100)

    print(1000)
    print(int(3/2))











