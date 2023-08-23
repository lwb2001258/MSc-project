import os
import chemprop
import pandas as pd
import time
import gc
if __name__ == "__main__":
    raw_dir = "zinc15/raw_data/"
    pred_dir = "zinc15/predict_result/"
    smiles_dir = "zinc15/smiles/"
    raw_file_list = []
    pred_file_list = []
    smiles_file_list = []
    for i, j, k in os.walk(raw_dir):
        raw_file_list.extend(k)
    for i, j, k in os.walk(pred_dir):
        pred_file_list.extend(k)
    for i, j, k in os.walk(smiles_dir):
        smiles_file_list.extend(k)
    with open('zinc15/finished_files.txt') as f:
        content = f.readlines()
    for line in content:
        pred_file_list.append(line.strip())
    active_file = open('zinc15/best/actives_predict_infos.csv', 'a+')
    finishe_file = open('zinc15/finished_files.txt', 'a+')
    big_smi_file_list = ['FDED.smi', 'GDAD.smi']
    for smi_file in smiles_file_list:
        # gc.collect()
        print(smi_file)
        size = os.path.getsize(smiles_dir+smi_file)
        print(size)
        # time.sleep(100000)
        if size > 1000000:
            big_smi_file_list.append(smi_file)
        if smi_file not in pred_file_list and smi_file not in big_smi_file_list:
            print(smi_file)
            try:
                arguments = [
                    '--test_path', smiles_dir+smi_file,
                    '--preds_path', pred_dir+smi_file,
                    '--checkpoint_dir', "test_models/classification/best/40/test_checkpoints_reg_literature_data_1692435425.713933_best",
                    '--num_workers', '0'
                ]
                args = chemprop.args.PredictArgs().parse_args(arguments)
                preds = chemprop.train.make_predictions(args=args)
                raw_file_path = raw_dir+smi_file
                with open(raw_file_path) as f:
                    content = f.readlines()
                smiles_dict = {}
                for index, line in enumerate(content):
                    if index!=0:
                        smi = line.strip().split(" ")[0]
                        zinc_id = line.strip().split(" ")[1]
                        smiles_dict[smi] = zinc_id

                with open(pred_dir + smi_file) as f:
                    content = f.readlines()
                for index, line in enumerate(content):
                    if index!=0:
                        smi = line.strip().split(",")[0]
                        pred_score = float(line.strip().split(",")[1])
                        if pred_score>=0.5:
                            zinc_id = smiles_dict.get(smi)
                            active_file.write(smi+','+str(zinc_id)+','+str(pred_score)+'\n')
                finishe_file.write(smi_file+'\n')
                # gc.collect()
                # print(gc.set_threshold())
            except Exception as e:
                print(smi_file, e)
