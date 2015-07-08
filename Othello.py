# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import sys
import numpy as np

#盤面描画
def show_position(column, row, positions):
    sentence = '　   '
    for c in column:
        sentence += c + '   '
    print(sentence)
    print('  ---------------------------------')
    
    
    for i in range(0, len(row)):
        sentence = str(row[i])+'　| '
        for p in positions[i,:]:
            if p == 0:
                sentence += ' ' + ' | ' 
            elif p == 1:
                sentence += '○' + ' | ' 
            elif p == 2:
                sentence += '●' + ' | ' 
        print(sentence)
        print('  ---------------------------------')
        

#初期化
column = np.array(['a','b','c','d','e','f','g','h'])
row = np.array(['1','2','3','4','5','6','7','8']).transpose()
positions = np.zeros((8,8,100))
condition = {'1':'人間',
             '2':'CPU'}

#対局条件設定
print("先攻 1：人間　2：CPU")
con_fir = input()
print("後攻 1：人間　2：CPU")
con_sec = input()
print(condition[str(con_fir)] + " VS " + condition[str(con_sec)] + " でゲームを始めます")

positions[1,1,0] = 1
positions[3,3,0] = 2
positions[7,7,0] = 1

show_position(column, row, positions[:,:,0])





