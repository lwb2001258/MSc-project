import chemprop
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.offsetbox import AnchoredText
from sklearn.metrics import mean_absolute_error, mean_squared_error
from sklearn.decomposition import PCA
import time
from hyperopt import tpe, hp, fmin, STATUS_OK,Trials



f = open("test_args/classification_literature_data_{}.csv".format(str(time.time())),'w')
f.write("epochs,batch_size,depth,hidden_size,activation,dropout,init_lr,final_lr,num_folds,ensemble_size,max_lr,mean_score,std_score\n")
f.flush()
def objective(params):
    time_str = str(time.time())
    epochs = params.get("epochs")
    batch_size = params.get("batch_size")
    depth = params.get("depth")
    hidden_size = params.get("hidden_size")
    activation = params.get("activation")
    dropout = params.get("dropout")
    init_lr = params.get("init_lr")
    final_lr = params.get("final_lr")
    num_folds = params.get("num_folds")
    ensemble_size = params.get("ensemble_size")
    max_lr = params.get("max_lr")
    arguments = [
        '--data_path', 'data/enhance_classification.csv',
        '--dataset_type', 'classification',
        '--save_dir', 'test_models/classification/best/50/test_checkpoints_reg_literature_data_{}_best'.format(time_str),
        '--epochs', str(epochs),
        '--save_smiles_splits',
        '--batch_size', str(batch_size),
        '--depth', str(depth),
        '--hidden_size', str(hidden_size),
        '--activation', activation,
        '--dropout', str(dropout),
        '--init_lr', str(init_lr),
        '--final_lr', str(final_lr),
        '--num_folds', str(num_folds),
        '--ensemble_size', str(ensemble_size),
        '--max_lr', str(max_lr),

    ]
    param_list = []
    param_list.append(str(epochs))
    param_list.append(str(batch_size))
    param_list.append(str(depth))
    param_list.append(str(hidden_size))
    param_list.append(str(activation))
    param_list.append(str(dropout))
    param_list.append(str(init_lr))
    param_list.append(str(final_lr))
    param_list.append(str(num_folds))
    param_list.append(str(ensemble_size))
    param_list.append(str(max_lr))
    args = chemprop.args.TrainArgs().parse_args(arguments)
    mean_score, std_score = chemprop.train.cross_validate(args=args, train_func=chemprop.train.run_training)
    param_list.append(str(mean_score))
    param_list.append(str(std_score))
    f.write(",".join(param_list)+"\n")
    f.flush()
    return 1-mean_score



space = {
    "epochs": hp.choice("epochs", [50]),
    "batch_size": hp.choice("batch_size", [20]),
    "depth": hp.choice("depth", [2]),
    "hidden_size": hp.choice("hidden_size",[1600]),
    "activation": hp.choice("activation", ["LeakyReLU"]),
    "dropout": hp.choice("dropout",[0.15]),
    "init_lr": hp.choice("init_lr",[0.00001]),
    "final_lr": hp.choice("final_lr",[0.000001]),
    "num_folds": hp.choice("num_folds", [10]),
    "ensemble_size": hp.choice("ensemble_size",[1]),
    "max_lr": hp.choice("max_lr",[0.001]),
}
trails = Trials()
best = fmin(
    fn=objective,#目标函数
    space=space,#搜索空间
    algo=tpe.suggest,#指定搜索算法
    max_evals=40,
    trials=trails
)

print("Best: {}".format(best))

