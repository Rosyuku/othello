#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 12 21:41:44 2018

@author: kazuyuki
"""

import glob
import numpy as np
import pandas as pd
import seaborn as sns

from joblib import Parallel, delayed

def getlast(f):
    
    df = pd.read_csv(f, index_col=[0])
    last = df.iloc[[-1]]
    return last

def getreverseNum(f):
    
    df = pd.read_csv(f, index_col=[0])
    reverseNum = (df.iloc[:, -64:].diff() != 0).sum() - 2
    return reverseNum

if __name__ == "__main__":
    
    #初期設定
    files = glob.glob('log_random_vs_random/*.csv')
    
    lastdfs = Parallel(n_jobs=-1, verbose=10)(delayed(getlast)(f) for f in files)
    reverseNumdfs = Parallel(n_jobs=-1, verbose=10)(delayed(getreverseNum)(f) for f in files)
    
    lastdf = pd.concat(lastdfs)
    reverseNumdf = pd.concat(reverseNumdfs, axis=1).T
    reverseNumdf[reverseNumdf == -1] = 0
    
    sns.heatmap(reverseNumdf.mean().values.reshape(8, 8), square=True, annot=True, cmap='bwr')
    
    #lastdf['優勢'].value_counts().plot.pie()
    
    lastdf = lastdf[lastdf[['先手石数', '後手石数']].max(axis=1) > 10]
    
    #lastdf[['先手石数', '後手石数']].max(axis=1).value_counts().sort_index().plot.bar()
    
    tdf = lastdf.copy()
    tdf = tdf[tdf['優勢'] == 2]
    tdf = tdf.iloc[:, -64:]
    tdf1 = tdf.mean()
    tdf2 = (tdf == 1.0).mean()
    tdf3 = (tdf == 2.0).mean()
    
    tdf = tdf2
    sns.heatmap(tdf.values.reshape(8, 8), square=True, annot=True, cmap='bwr')
    
    res = pd.DataFrame(index=range(lastdf.shape[0]), columns=range(3), data=0)
    for i in range(200, lastdf.shape[0]):
        res.iloc[i, :] = (lastdf.iloc[:i+1,:].pivot_table(index='優勢', values='手数', aggfunc='count') / (i+1)).values.reshape(-1)
