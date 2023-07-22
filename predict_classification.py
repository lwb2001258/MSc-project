import chemprop
from rdkit import Chem

arguments = [
    '--test_path', 'data/smiles.csv',
    '--preds_path', 'predict/classification/test5.csv',
    '--checkpoint_dir', 'test_models/classification/test_checkpoints_reg_1688868101.007874',
    '--num_workers', '0'
]
smiles =[ ["C1=C(SC(=N1)SC2=NN=C(S2)N)[N+](=O)[O-]"],["[N+](=O)(c1cnc(s1)Sc1sc(nn1)N)[O-]"],["c1(nnc(N)s1)Sc1sc([N+](=O)[O-])cn1"],["c1(cnc(Sc2nnc(s2)N)s1)[N+](=O)[O-]"]]
args = chemprop.args.PredictArgs().parse_args(arguments)
preds = chemprop.train.make_predictions(args=args,smiles=smiles)

# mol = Chem.MolFromSmiles("C1=C(SC(=N1)SC2=NN=C(S2)N)[N+](=O)[O-]")
# mols = []
# for _ in range(10):
#   smi = Chem.MolToSmiles(mol, doRandom=True)
#   print(smi)
#   m = Chem.MolFromSmiles(smi)
#   mols.append(m)



# smiles = [['CCCC'], ['CCCCC'], ['COCC']]
# preds = chemprop.train.make_predictions(args=args, smiles=smiles, model_objects=model_objects)