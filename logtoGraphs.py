# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 22:54:34 2015

@author: Wakasugi Kazuyuki
"""

import glob
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager

def OneSummaryGraph(f,name,folder, font):
    #グラフ1
    plt.title(name)    
    plt.plot(f[f.columns[1]], f[f.columns[5]])
    plt.plot(f[f.columns[1]], f[f.columns[6]])
    plt.plot(f[f.columns[1]], f[f.columns[4]])
    plt.xlabel(f.columns[1].decode('utf_8'), fontproperties=font )
    plt.legend([f.columns[5].decode('utf_8'),f.columns[6].decode('utf_8'), f.columns[4].decode('utf_8')], prop=font, loc=0)  # 凡例をグラフにプロット
    plt.tight_layout()
    plt.savefig(folder + name + '_s1.png')
    
    #グラフ2    
    fig = plt.figure(figsize=(16, 12))
    for i in range(1,65):
        
        plt.subplot(8,8,i)
        plt.title(f.columns[9+i])
        plt.ylim(0, 2.2)
        if(f[f.columns[9+i]][f[f.columns[1]].max()]) == 1:
            plt.plot(f[f.columns[1]], f[f.columns[9+i]], "r")
        elif (f[f.columns[9+i]][f[f.columns[1]].max()]) == 2:
            plt.plot(f[f.columns[1]], f[f.columns[9+i]], "b")
    plt.suptitle(name)
    plt.tight_layout()
    plt.savefig(folder + name + '_s2.png')
    
#初期設定
fp = matplotlib.font_manager.FontProperties(fname="C:\Windows\Fonts\msgothic.ttc")
files = glob.glob('C:\Git\Othello\log\*.csv')
savefolder = 'C:\Git\Othello\Graph\\'

f = pd.read_csv(files[0])
OneSummaryGraph(f,f[f.columns[0]][0],savefolder,fp)

"""
for file in files:
    #print file
    f = pd.read_csv(files[0])
    OneSummaryGraph(f,f[f.columns[0]][0],savefolder,fp)
"""

#pd.tools.plotting.scatter_matrix(f)
