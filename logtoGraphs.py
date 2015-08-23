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

#初期設定
fp = matplotlib.font_manager.FontProperties(fname="C:\Windows\Fonts\msgothic.ttc")
# パス内の全ての"指定パス+ファイル名"と"指定パス+ディレクトリ名"を要素とするリストを返す
files = glob.glob('C:\Git\Othello\log\*.csv') # ワイルドカードが使用可能
 
#for file in files:
    #print file
a = u"あ" 
f = pd.read_csv(files[0])
#plt.plot(f[f.columns[1]], f[f.columns[5]])
#plt.plot(f[f.columns[1]], f[f.columns[6]])
plt.xlabel(f.columns[1].decode('utf_8'), fontproperties=fp )
plt.ylabel("Y-axis")
#plt.legend([f.columns[5],f.columns[6]], prop=fontprop)  # 凡例をグラフにプロット

import matplotlib.pyplot as plt
import matplotlib.font_manager
fp = matplotlib.font_manager.FontProperties(fname="C:\Windows\Fonts\msgothic.ttc")
a = "あ"
plt.xlabel(a.decode('utf_8'), fontproperties=fp)