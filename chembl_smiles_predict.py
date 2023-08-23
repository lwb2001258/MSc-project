import os
import chemprop
import pandas as pd
import time
import gc
if __name__ == "__main__":
    arguments = [
        '--test_path', 'data/chembl_smiles.csv',
        '--preds_path', 'predict/chembl_predict/first_predict_test_checkpoints_reg_1688915122.125031.csv',
        '--checkpoint_dir', "test_models/classification/test_checkpoints_reg_1688915122.125031",
        '--num_workers', '0'
    ]
    args = chemprop.args.PredictArgs().parse_args(arguments)
    preds = chemprop.train.make_predictions(args=args)
    # raw_file_path = raw_dir+smi_file
    # with open(raw_file_path) as f:
    #     content = f.readlines()
    # smiles_dict = {}
    # for index, line in enumerate(content):
    #     if index!=0:
    #         smi = line.strip().split(" ")[0]
    #         zinc_id = line.strip().split(" ")[1]
    #         smiles_dict[smi] = zinc_id
    #
    # with open(pred_dir + smi_file) as f:
    #     content = f.readlines()
    # for index, line in enumerate(content):
    #     if index!=0:
    #         smi = line.strip().split(",")[0]
    #         pred_score = float(line.strip().split(",")[1])
    #         if pred_score>=0.5:
    #             zinc_id = smiles_dict.get(smi)
    #             active_file.write(smi+','+str(zinc_id)+','+str(pred_score)+'\n')
    # finishe_file.write(smi_file+'\n')
