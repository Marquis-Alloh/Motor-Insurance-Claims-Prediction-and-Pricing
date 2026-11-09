import pandas as pd
import numpy as np

def eval_accuracy(MN_pred: list[float], pred = True):
    if pred: return np.array(MN_pred).max()
    return np.array(MN_pred).min()
