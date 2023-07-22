import torch
import torch.nn.functional as F
from torch_geometric.nn import GraphConv, TopKPooling
from torch_geometric.nn import global_mean_pool as gap
from torch_geometric.nn import global_max_pool as gmp


# class Net(torch.nn.Module):
#     def __init__(self, num_features,multi_label):
#         super(Net, self).__init__()
#         self.conv1 = GraphConv(num_features, 500)
#         # self.conv1.weight.data.normal_()
#         self.pool1 = TopKPooling(500, ratio=0.5)
#         self.conv2 = GraphConv(500, 500)
#         self.pool2 = TopKPooling(500, ratio=0.5)
#
#         self.lin1 = torch.nn.Linear(1000, 2000)
#         self.lin2 = torch.nn.Linear(2000, 4000)
#         self.lin3 = torch.nn.Linear(4000, multi_label)
#
#     def forward(self, data):
#         x, edge_index, edge_attr, batch = data.x, data.edge_index, data.edge_attr, data.batch
#
#         x = F.relu(self.conv1(x, edge_index, edge_attr))
#         x, edge_index, edge_attr, batch, _, _ = self.pool1(x, edge_index, edge_attr, batch)
#         x1 = torch.cat([gmp(x, batch), gap(x, batch)], dim=1)
#
#         x = F.relu(self.conv2(x, edge_index, edge_attr))
#         x, edge_index, edge_attr, batch, _, _ = self.pool2(x, edge_index, edge_attr, batch)
#         x2 = torch.cat([gmp(x, batch), gap(x, batch)], dim=1)
#
#
#         x = x1 + x2
#         x = F.relu(self.lin1(x))
#         x = F.dropout(x, p=0.3, training=self.training)
#         x = F.relu(self.lin2(x))
#         x = F.dropout(x, p=0.3, training=self.training)
#         x = torch.sigmoid(self.lin3(x))
#
#         return x


class Net(torch.nn.Module):
    def __init__(self, num_features,multi_label):
        super(Net, self).__init__()
        self.conv1 = GraphConv(num_features, 500)
        # self.conv1.weight.data.normal_()
        self.pool1 = TopKPooling(500, ratio=0.5)
        self.conv2 = GraphConv(500, 500)
        self.pool2 = TopKPooling(500, ratio=0.5)

        self.lin1 = torch.nn.Linear(1000, 2000)
        self.lin2 = torch.nn.Linear(2000, 4000)
        self.lin3 = torch.nn.Linear(4000, multi_label)

    def forward(self, data):
        x, edge_index, edge_attr = data.x, data.edge_index, data.edge_attr

        x = F.relu(self.conv1(x, edge_index, edge_attr))
        x, edge_index, edge_attr,  _, _ = self.pool1(x, edge_index, edge_attr)
        x1 = torch.cat([gmp(x), gap(x)], dim=1)

        x = F.relu(self.conv2(x, edge_index, edge_attr))
        x, edge_index, edge_attr,  _, _ = self.pool2(x, edge_index, edge_attr)
        x2 = torch.cat([gmp(x), gap(x)], dim=1)


        x = x1 + x2
        x = F.relu(self.lin1(x))
        x = F.dropout(x, p=0.3, training=self.training)
        x = F.relu(self.lin2(x))
        x = F.dropout(x, p=0.3, training=self.training)
        x = torch.sigmoid(self.lin3(x))

        return x