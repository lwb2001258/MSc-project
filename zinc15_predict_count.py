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
    total_count = 0
    for pred_file in pred_file_list:
        with open(pred_dir+pred_file) as f:
            content = f.readlines()
        total_count = total_count+len(content)
    print(total_count)