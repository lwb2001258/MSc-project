"""Loads a trained chemprop model checkpoint and makes predictions on a dataset."""

from chemprop.train import chemprop_predict
import os
if __name__ == '__main__':
    # chemprop_predict()
    dir_path = 'predict/classification'
    file_list = []
    file_name_list = []
    for file in os.listdir(dir_path):
        d = os.path.join(dir_path, file)
        if os.path.isfile(d):
            file_list.append(d)
    for file_path in file_list:
        file_name_list.append(os.path.basename(file_path).strip(".csv"))
    check_dirs = []
    rootdir = 'test_models/classification'
    for file in os.listdir(rootdir):
        d = os.path.join(rootdir, file)
        if os.path.isdir(d):
            check_dirs.append(d)
    for dir in check_dirs:
        file_name = os.path.basename(dir)
        if file_name not in file_name_list:
            print(file_name)

