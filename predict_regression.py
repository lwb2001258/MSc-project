import chemprop

arguments = [
    '--test_path', 'data/smiles.csv',
    '--preds_path', 'predict/regression/test2.csv',
    '--checkpoint_dir', 'test_models/regression/test_checkpoints_reg_1688198664.715639',
    '--num_workers', '0'
]
smiles =[ ["C1=C(SC(=N1)SC2=NN=C(S2)N)[N+](=O)[O-]"]]
args = chemprop.args.PredictArgs().parse_args(arguments)
preds = chemprop.train.make_predictions(args=args, smiles=smiles)