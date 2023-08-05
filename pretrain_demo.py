import torchvision.models

from chemprop.utils import load_checkpoint
import torch

model = load_checkpoint("test_models/classification/test_checkpoints_reg_1688090328.4075499/fold_0/model_0/model.pt")
print(model.state_dict())
print()
print()
print()
print()
print()

print(model.parameters())




pretrainNet = torchvision.models.resnet18(pretrained=True)