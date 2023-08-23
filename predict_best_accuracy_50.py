import os
import json
import pandas as pd
with open('test_result2.txt') as f:
    content = f.readlines()
# total = 0
# correct = 0
# validate_file = open("antibiotic_validate.csv",'w')
# validate_file.write("SMILES,active\n")
# for index,line in enumerate(content):
#     total +=1
#     smi = line.strip().split("\t")[0]
#     predict_result = float(line.strip().split("\t")[1])
#     mean_inhibition = float(line.strip().split("\t")[2])
#     if predict_result>=0.5:
#         predict_active = 1
#     else:
#         predict_active = 0
#     if mean_inhibition <= 0.1:
#         real_active = 1
#     else:
#         real_active = 0
#     if predict_active == real_active:
#        correct += 1
#     validate_file.write(smi + "," + str(real_active) + "\n")
#
# print(correct/total)
with open('test_classfication.txt') as f:
    content = f.readlines()
test_result={}
for index,line in enumerate(content):
    if index!=0:
        smi = line.strip().split(",")[0]
        active = line.strip().split(",")[1]
        test_result[smi] = active
check_dirs = []
rootdir = 'predict/classification/best/50/'
for file in os.listdir(rootdir):
    d = os.path.join(rootdir, file)
    if os.path.isfile(d):
        check_dirs.append(d)
params_file = open("result/classification/best/50/params_result.csv",'w')
params_file.write("dir_name,epochs,batch_size,depth,hidden_size,activation,dropout,init_lr,final_lr,num_folds,ensemble_size,max_lr,predict_accuracy,halicin_predict_score,train_source\n")
for dir in check_dirs:
    try:
        halicin_predict_score = 0.0
        file_name = os.path.basename(dir)
        with open("predict/classification/best/50/{}".format(file_name))as f:
            content = f.readlines()
        predict_result = {}
        for index,line in enumerate(content):
            if index != 0:

                smi = line.strip().split(",")[0]
                if smi == "Nc1nnc(Sc2ncc(s2)[N+]([O-])=O)s1":
                    halicin_predict_score = str(float(line.strip().split(",")[1]))
                active = float(line.strip().split(",")[1])
                if active < 0.5:
                    active = '0'
                else:
                    active = '1'

                predict_result[smi] = active
        total = 0
        total_correct = 0
        for smi in predict_result:
            if smi in test_result:
                total += 1
                if predict_result.get(smi) == test_result.get(smi):
                    total_correct += 1
        # if total_correct/total>0.8:
        if True:
            print(file_name, total_correct/total)
        try:
            dir_name = file_name.strip(".csv")
            json_file = open('test_models/classification/best/50/{}/args.json'.format(dir_name), 'r')
            json_dict = json.load(json_file)
            epochs = str(json_dict.get('epochs'))
            batch_size = str(json_dict.get('batch_size'))
            depth = str(json_dict.get('depth'))
            hidden_size = str(json_dict.get('hidden_size'))
            activation = str(json_dict.get('activation'))
            dropout = str(json_dict.get('dropout'))
            init_lr = str(json_dict.get('init_lr'))
            final_lr = str(json_dict.get('final_lr'))
            num_folds = str(json_dict.get('num_folds'))
            ensemble_size = str(json_dict.get('ensemble_size'))
            max_lr = str(json_dict.get('max_lr'))
            train_source = json_dict.get("data_path")
            predict_accuracy = str(total_correct/total)
            csv_file ="predict/classification/best/50/{}".format(file_name)
            params_list = [dir_name,epochs,batch_size,depth,hidden_size,activation,dropout,init_lr,final_lr,num_folds,ensemble_size,max_lr,predict_accuracy,halicin_predict_score,train_source]
            params_file.write(",".join(params_list)+"\n")
        except Exception as e:
            print(file_name, str(e))
            pass
    except:
        # print(dir)
        pass

