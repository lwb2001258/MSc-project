import chemprop
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.offsetbox import AnchoredText
from sklearn.metrics import mean_absolute_error, mean_squared_error
from sklearn.decomposition import PCA
import time
from hyperopt import tpe, hp, fmin, STATUS_OK,Trials


def plot_parity(y_true, y_pred, y_pred_unc=None):
    axmin = min(min(y_true), min(y_pred)) - 0.1 * (max(y_true) - min(y_true))
    axmax = max(max(y_true), max(y_pred)) + 0.1 * (max(y_true) - min(y_true))

    mae = mean_absolute_error(y_true, y_pred)
    rmse = mean_squared_error(y_true, y_pred, squared=False)

    plt.plot([axmin, axmax], [axmin, axmax], '--k')

    plt.errorbar(y_true, y_pred, yerr=y_pred_unc, linewidth=0, marker='o', markeredgecolor='w', alpha=1, elinewidth=1)

    plt.xlim((axmin, axmax))
    plt.ylim((axmin, axmax))

    ax = plt.gca()
    ax.set_aspect('equal')

    at = AnchoredText(
        f"MAE = {mae:.2f}\nRMSE = {rmse:.2f}", prop=dict(size=10), frameon=True, loc='upper left')
    at.patch.set_boxstyle("round,pad=0.,rounding_size=0.2")
    ax.add_artist(at)

    plt.xlabel('True')
    plt.ylabel('Chemprop Predicted')

    plt.show()

    return
f = open("test_args/classification_hiv_{}.csv".format(str(time.time())),'w')
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
        '--data_path', 'data/enhance_hiv_classification.csv',
        '--dataset_type', 'classification',
        '--save_dir', 'test_models/hiv/test_enhance_checkpoints_reg_{}'.format(time_str),
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
        '--num_workers', '0',

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
    "epochs": hp.choice("epochs", [30,40]),
    "batch_size": hp.choice("batch_size", [20]),
    "depth": hp.choice("depth", [5,6]),
    "hidden_size": hp.choice("hidden_size",[1600]),
    "activation": hp.choice("activation", ["LeakyReLU",'ReLU']),
    "dropout": hp.choice("dropout",[0.20,0.35]),
    "init_lr": hp.choice("init_lr",[0.0001]),
    "final_lr": hp.choice("final_lr",[0.000001]),
    "num_folds": hp.choice("num_folds", [1]),
    "ensemble_size": hp.choice("ensemble_size",[1]),
    "max_lr": hp.choice("max_lr",[0.001]),
}
trails = Trials()
best = fmin(
    fn=objective,#目标函数
    space=space,#搜索空间
    algo=tpe.suggest,#指定搜索算法
    max_evals=1000,
    trials=trails
)

print("Best: {}".format(best))

