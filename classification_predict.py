import os
import chemprop
if __name__ == "__main__":
    # with open('literature_predict_result.txt') as f:
    #     content = f.readlines()
    # pred_info = {}
    # for index, line in enumerate(content):
    #     if index == 0:
    #         smiles1 = line.strip().split("\t")[0]
    #     smiles = line.strip().split("\t")[0]
    #     score = line.strip().split("\t")[1]
    #     pred_info[smiles] = float(score)
    # with open("preds") as f:
    #     content = f.readlines()
    # result_info = {}
    # for index,line in enumerate(content):
    #     if index!=0:
    #         smiles = line.strip().split(",")[0].strip("[]").replace("'","").replace("\\\\","\\")
    #         score = float(line.strip().split(",")[1])
    #         result_info[smiles]=score
    # diff_info = {}
    # for key in result_info.keys():
    #     result = result_info.get(key)
    #     pred = pred_info.get(key)
    #     diff = None
    #     if result and pred:
    #         diff = result-pred
    #     diff_info[key] = diff
    # with open("diff1.csv",'w') as f:
    #     f.write("smiles,active\n")
    #     for key in diff_info:
    #         f.write(key+","+str(diff_info.get(key))+"\n")
    with open('literature_predict_result.txt') as f:
        content = f.readlines()
    pred_info = {}
    for index, line in enumerate(content):
        if index == 0:
            smiles1 = line.strip().split("\t")[0]
        smiles = line.strip().split("\t")[0]
        score = line.strip().split("\t")[1]
        pred_info[smiles] = float(score)
    dir_path = 'predict/classification'
    file_list = []
    file_name_list = []
    for file in os.listdir(dir_path):
        d = os.path.join(dir_path, file)
        if os.path.isfile(d):
            file_list.append(d)
    for file_path in file_list:
        file_name_list.append(os.path.basename(file_path).replace(".csv",""))
    check_dirs = []
    rootdir = 'test_models/classification'
    for file in os.listdir(rootdir):
        d = os.path.join(rootdir, file)
        if os.path.isdir(d):
            check_dirs.append(d)
    for dir in check_dirs:
        file_name = os.path.basename(dir)
        # if file_name not in file_name_list:
        if True:
            try:
                arguments = [
                    '--test_path', 'data/smiles.csv',
                    '--preds_path', 'predict/classification/{}.csv'.format(file_name),
                    '--checkpoint_dir', dir,
                    '--num_workers', '0'
                ]

                args = chemprop.args.PredictArgs().parse_args(arguments)
                preds = chemprop.train.make_predictions(args=args)
                with open('predict/classification/{}.csv'.format(file_name)) as f:
                    content = f.readlines()
                result_info = {}
                for index,line in enumerate(content):
                    if index!=0:
                        smiles = line.strip().split(",")[0]
                        score = float(line.strip().split(",")[1])
                        result_info[smiles]=score
                diff_info = {}
                total_diff = 0
                result_file = open("result/classification.txt","a+")
                for key in result_info.keys():
                    result = result_info.get(key)
                    pred = pred_info.get(key)
                    diff = None
                    if result and pred:
                        diff = result-pred
                        total_diff = total_diff + abs(diff)
                    diff_info[key] = diff
                with open("diff1.csv",'w') as f:
                    f.write("smiles,active\n")
                    for key in diff_info:
                        f.write(key+","+str(diff_info.get(key))+"\n")
                result_file.write(file_name + "      "+str(total_diff) +"\n")
            except Exception as e:
                print(str(e))
                print(file_name)




