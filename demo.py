import chemprop
from chemprop.features import MolGraph,BatchMolGraph,mol2graph
from chemprop.train import cross_validate, run_training
from rdkit import Chem

predict_arguments = [
    # '--data_path', 'data/tox21.csv',
    # '--dataset_type', 'classification',

    '--checkpoint_path', 'tox21_checkpoints',
    '--test_path', 'data/tox21.csv',
    '--preds_path', 'data/tox21.csv',
    # '--save_dir', 'tox21_save_dir',
]

training_arguments = [
    '--data_path', 'data/cell_classification2.csv',
    '--dataset_type', 'classification',
    '--save_dir', 'cell_classification',
    '--batch_size', '1',

]

# training_arguments = [
#     '--data_path', 'data/cell_regression.csv',
#     '--dataset_type', 'regression',
#     '--save_dir', 'cell_regression',
#
# ]




training_args = chemprop.args.TrainArgs().parse_args(training_arguments)
# predict_args = chemprop.args.PredictArgs().parse_args(predict_arguments)
cross_validate(args=training_args, train_func=run_training)


# model_objects = chemprop.train.load_model(args=args)
#
# smiles = [['CCC'], ['CCCC'], ['OCC']]
# preds = chemprop.train.make_predictions(args=args, smiles=smiles, model_objects=model_objects)
#
# smiles = [['CCCC'], ['CCCCC'], ['COCC']]
# preds = chemprop.train.make_predictions(args=args, smiles=smiles, model_objects=model_objects)
#
# smiles_list = ['C1CCCCC1','c1ccccc1','Cc1ccccc1','CCc1ccccc1']
# mol_list = []
# for smiles in smiles_list:
#     mol = Chem.MolFromSmiles(smiles)
#     mol_list.append(mol)
# molgraph_list = []
# for mol in mol_list:
#     molgraph = MolGraph(mol)
#     molgraph_list.append(molgraph)
# a = BatchMolGraph(molgraph_list)
# b = mol2graph(mol_list)
#
# # forward_index = a.b2br[:, 0]
# # backward_index = a.b2br[:, 1]
# d = 5
# print(d)