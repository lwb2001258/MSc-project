from chemprop.data import *
from rdkit import Chem
from chemprop.features import MolGraph
import torch
from GCNmodel import *


def get_dataset(path):
    data = get_data(path)
    smiles = data.smiles()
    targets = data.targets()
    smiles_target_list = []
    for index,smile in enumerate(smiles):
        smiles_target_list.append((smile[0], targets[index][0]))
    dataset = []
    for item in smiles_target_list:
        smiles = item[0]
        target = item[1]
        mol = Chem.MolFromSmiles(smiles)
        molGraph = MolGraph(mol)
        dataset.append((molGraph,target))
    return dataset


# class GraphDataLoader(object):
#     def __init__(self, path, batch_size):
#         # 假设数据长度是100，batch_size 是4
#         self.dataset = get_dataset(path)
#         # 假设 sampler 是 SequentialSampler，那么实际上就是 [0,1,...,99] 列表而已
#         # 如果 sampler 是 RandomSampler，那么可能是 [30,1,34,2,6,...,0] 列表
#         self.sampler = range(len(self.dataset))
#         self.batch_size = batch_size
#         self.index = 0
#
#     # def collate_fn(self, data):
#     #     # batch 维度聚合数据
#     #     batch_img = torch.stack(data[0], 0)
#     #     batch_target = torch.stack(data[1], 0)
#     #     return batch_img, batch_target
#
#     def collate_fn(self, data):
#         # batch 维度聚合数据
#         batch_graph = []
#         batch_target = []
#         for item in data:
#             batch_graph.append(item[0])
#             batch_target.append(item[1])
#
#         return batch_graph, batch_target
#
#     def __next__(self):
#         # 0.batch_index 输出，实际上就是 BatchSampler 做的事情
#         i = 0
#         batch_index = []
#         while i < self.batch_size:
#             # 内部会调用 sampler 对象取单个索引
#             batch_index.append(self.sampler[self.index])
#             self.index += 1
#             i += 1
#
#         # 1.得到 batch 个数据了，调用 dataset 对象
#         data = [self.dataset[idx] for idx in batch_index]
#
#         # 2. 调用 collate_fn 在 batch 维度拼接输出
#         batch_data = self.collate_fn(data)
#         return batch_data
#
#     def __iter__(self):
#         return self


# data_list = get_dataset(path="data/cell_classification3.csv")
# model =Net(150,2)
#
#
# def train():
#     model.train()
#     optimizer.zero_grad()
#
#     # print(data.x)
#     # print()# Clear gradients.
#     out = model(molGraph)  # Perform a single forward pass.
#     loss = criterion(out[molGraph.train_mask],
#                      data.y[data.train_mask])  # Compute the loss solely based on the training nodes.
#     loss.backward()  # Derive gradients.
#     optimizer.step()  # Update parameters based on gradients.
#     return loss
# for epoch in range(1, 201):
#     for i, data in enumerate(data_list):
#         molGraph, label = data
#         optimizer = torch.optim.Adam(model.parameters(), lr=0.01)
#         criterion = torch.nn.CrossEntropyLoss()
#         loss = train()
#         print(f'Epoch: {epoch:03d}, Loss: {loss:.4f}')

a = [[0,0, 0],[1,1,1], [2,2,2]]
a = torch.tensor(a)
print(a[0])
