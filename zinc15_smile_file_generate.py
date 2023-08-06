import os
import chemprop
import pandas as pd
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
    for raw_file in raw_file_list:
        if raw_file not in smiles_file_list:
            data = pd.read_csv(raw_dir+raw_file, sep=' ')
            smi_list = data['smiles']
            with open(smiles_dir+raw_file, 'w') as f:
                f.write("SMILES\n")
                for smi in smi_list:
                    f.write(smi+"\n")