# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import sys
import numpy as np
import pandas as pd
import random
import FunctionModules as fm
import datetime     

#CPUアルごリズム_ランダム
def get_next_posi_Randam(next_dia_all, turn):
    next_posi_enable = []
    for i in range(0,8):
        for j in range(0,8):
            if next_dia_all[i,j] == turn + 4:
                next_posi_enable.append(str(Inv_columnList[j])+str(Inv_rowList[i]))

    return random.choice(next_posi_enable)                

#初期化
columnArray = np.array(['a','b','c','d','e','f','g','h'])
rowArray = np.array(['1','2','3','4','5','6','7','8']).transpose()
diagrams = np.zeros((8,8,100))
condition = {'1':'人間',
             '2':'CPU'}
columnList = {'a':0,'b':1,'c':2,'d':3,'e':4,'f':5,'g':6,'h':7}
rowList = {'1':0,'2':1,'3':2,'4':3,'5':4,'6':5,'7':6,'8':7}
Inv_columnList = {v:k for k, v in columnList.items()}
Inv_rowList = {v:k for k, v in rowList.items()}
             
#対局条件設定
print("対局条件を入力してください。")
print("先攻 1：人間　2：CPU")
print('  ---------------------------------')
con_fir = input()
print("後攻 1：人間　2：CPU")
print('  ---------------------------------')
con_sec = input()
if con_fir == 2 and con_sec == 2:
    print("対局回数を入力してください。")
    print('  ---------------------------------')
    vs_count = input()
else:
    vs_count = 1
print(condition[str(con_fir)] + " VS " + condition[str(con_sec)] + " でゲームを始めます")

for i in range(0, vs_count):
    #対局初期化
    diagrams[3,3,0] = 1
    diagrams[3,4,0] = 2
    diagrams[4,3,0] = 2
    diagrams[4,4,0] = 1
    gameset = False
    turnPlayer = 1
    tempo = 0
    passtempo = False
    Blackcount = 2
    Whitecount = 2
    ID = datetime.datetime.today().strftime("%Y_%m_%d_%H_%M_%S_%f")
    log = pd.read_csv('logformat.csv')
    
    #対局部分
    while(gameset == False):
        #状況表示
        if vs_count == 1:
            fm.show_position(columnArray, rowArray, diagrams[:,:,tempo])
        next_dia_all, next_diaList = fm.search_newstone_position_all(diagrams[:,:,tempo], turnPlayer)
        if len(next_diaList) == 0:
            if passtempo == True:
                if vs_count == 1:                
                    print("お互い打つ場所がないのでゲームセットです。")
                next_posi = 'pass'
                break
            else:
                passtempo = True
                next_posi = 'pass'
                if vs_count == 1:
                    print("打つ場所がないのでパスとなります。")
        else:
            #show_position(columnArray, rowArray, next_dia_all)
            passtempo = False
            if turnPlayer == 1:
                if vs_count == 1:
                    print("先手の手番です。")
                if con_fir == 1:
                    print("石を置く位置を入力してください")
                    next_posi = str(raw_input())
                    flag, EMsg = fm.next_posi_check(next_posi, next_dia_all, turnPlayer)
                    while flag == False:
                        print(EMsg)
                        next_posi = str(raw_input())
                        flag, EMsg = fm.next_posi_check(next_posi, next_dia_all, turnPlayer)
                else:
                    next_posi = get_next_posi_Randam(next_dia_all, turnPlayer)
                    if vs_count == 1:
                        print(next_posi+"を着手します。")
            else:
                if vs_count == 1:
                    print("後手の手番です。")
                if con_sec == 1:
                    print("石を置く位置を入力してください")
                    next_posi = str(raw_input())
                    flag, EMsg = fm.next_posi_check(next_posi, next_dia_all, turnPlayer)
                    while flag == False:
                        print(EMsg)
                        next_posi = str(raw_input())
                        flag, EMsg = fm.next_posi_check(next_posi, next_dia_all, turnPlayer)
                else:
                    next_posi = get_next_posi_Randam(next_dia_all, turnPlayer)
                    if vs_count == 1:
                        print(next_posi+"を着手します。")
                
        #ログを記録
        Blackcount, Whitecount = fm.stone_count_check(diagrams[:,:,tempo])
        if Blackcount > Whitecount:
            superiorityPlayer = 1
        elif Blackcount < Whitecount:
            superiorityPlayer = 2
        else:
            superiorityPlayer = 0
            
        data = [ID, tempo, turnPlayer, next_posi, len(next_diaList), Blackcount, Whitecount, con_fir, con_sec, superiorityPlayer]
        data.extend(diagrams[:,:,tempo].T.reshape(64))
        add_log = pd.Series(data = data, index = log.columns, name = [tempo])
        log = log.append(add_log)
        
        #手数をインクリメント    
        tempo += 1
        
        #盤面を更新
        if passtempo == False:
            for next_dia in next_diaList:
                if next_dia[int(rowList[next_posi[1:]]),int(columnList[next_posi[:1]])] == 4 +  turnPlayer:
                    diagrams[:,:,tempo] = next_dia.copy()
                for i in range(0,8):
                    for j in range(0,8):
                        if diagrams[i,j,tempo] == 4 +  turnPlayer:
                            diagrams[i,j,tempo] = turnPlayer
                        elif diagrams[i,j,tempo] == 3 or diagrams[i,j,tempo] == 4: 
                            diagrams[i,j,tempo] = turnPlayer
        else:
            diagrams[:,:,tempo] = diagrams[:,:,tempo-1].copy()
                    
            
        #手番の交代
        if turnPlayer == 1:
            turnPlayer = 2
        else:
            turnPlayer = 1
    
    #終局処理
    Blackcount, Whitecount = fm.stone_count_check(diagrams[:,:,tempo])
    if Blackcount > Whitecount:
        print(str(Blackcount) + " VS " + str(Whitecount) + " で先手●の勝ちです")
    elif Whitecount > Blackcount:
        print(str(Whitecount) + " VS " + str(Blackcount) + " で後手○の勝ちです")
    else:
        print("引き分けです")
    
    log.to_csv('log\\' + ID +'.csv', index=False)
    




