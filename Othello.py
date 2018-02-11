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
import os

import Algorithm         

class Othello:
    
    columnArray = np.array(['a','b','c','d','e','f','g','h'])
    rowArray = np.array(['1','2','3','4','5','6','7','8']).transpose()
    condition = {'1':'人間',
                 '2':'CPU'}
    columnList = {'a':0,'b':1,'c':2,'d':3,'e':4,'f':5,'g':6,'h':7}
    rowList = {'1':0,'2':1,'3':2,'4':3,'5':4,'6':5,'7':6,'8':7}
    Inv_columnList = {v:k for k, v in columnList.items()}
    Inv_rowList = {v:k for k, v in rowList.items()}
    win = [0,0]    
    
    def __init__(self, 
                 interactive=True,
                 con_fir=None,
                 con_sec=None,
                 alg_fir=None,
                 alg_sec=None,
                 vs_count=None,
                 ):
        
        self.interactive = interactive
        self.con_fir = con_fir
        self.con_sec = con_sec
        self.alg_fir = alg_fir
        self.alg_sec = alg_sec
        self.vs_count = vs_count
    
    def condition_init(self):

        if self.interactive == True:
            #対局条件設定
            print("対局条件を入力してください。")
            print("先攻 1：人間　2：CPU")
            print('  ---------------------------------')
            self.con_fir = int(input())
            if self.con_fir == 2:
                self.alg_fir = Algorithm.random_choice()
            print("後攻 1：人間　2：CPU")
            print('  ---------------------------------')
            self.con_sec = int(input())
            if self.con_sec == 2:
                self.alg_sec = Algorithm.random_choice()
            if self.con_fir == 2 and self.con_sec == 2:
                print("対局回数を入力してください。")
                print('  ---------------------------------')
                self.vs_count = int(input())
            else:
                self.vs_count = 1
            print(self.condition[str(self.con_fir)] + " VS " + self.condition[str(self.con_sec)] + " でゲームを始めます")        
    
    def diagrams_init(self):
        
        self.diagrams = np.zeros((8,8,100))
        self.diagrams[3,3,0] = 1
        self.diagrams[3,4,0] = 2
        self.diagrams[4,3,0] = 2
        self.diagrams[4,4,0] = 1
        self.gameset = False
        self.turnPlayer = 1
        self.tempo = 0
        self.passtempo = False
        self.ID = datetime.datetime.today().strftime("%Y_%m_%d_%H_%M_%S_%f")
        self.log = pd.read_csv('logformat.csv')        
            
    def one_game(self):
        
        self.diagrams_init()
        
        #対局部分
        while(self.gameset == False):
            #状況表示
            if self.vs_count == 1:
                fm.show_position(self.columnArray, self.rowArray, self.diagrams[:,:,self.tempo])
            next_dia_all, next_diaList = fm.search_newstone_position_all(self.diagrams[:,:,self.tempo], self.turnPlayer)
            if len(next_diaList) == 0:
                if self.passtempo == True:
                    if self.vs_count == 1:                
                        print("お互い打つ場所がないのでゲームセットです。")
                    next_posi = 'pass'
                    break
                else:
                    self.passtempo = True
                    next_posi = 'pass'
                    if self.vs_count == 1:
                        print("打つ場所がないのでパスとなります。")
            else:
                #fm.show_position(columnArray, rowArray, next_dia_all)
                self.passtempo = False
                if self.turnPlayer == 1:
                    if self.vs_count == 1:
                        print("先手の手番です。")
                    if self.con_fir == 1:
                        print("石を置く位置を入力してください")
                        next_posi = input()
                        if next_posi == 'quit':
                            break
                        flag, EMsg = fm.next_posi_check(next_posi, next_dia_all, self.turnPlayer)
                        while flag == False:
                            print(EMsg)
                            next_posi = input()
                            flag, EMsg = fm.next_posi_check(next_posi, next_dia_all, self.turnPlayer)
                    else:
                        next_posi = self.alg_fir.get_next_posi_Randam(self.diagrams, next_dia_all, self.turnPlayer)
                        if self.vs_count == 1:
                            print(next_posi+"を着手します。")
                else:
                    if self.vs_count == 1:
                        print("後手の手番です。")
                    if self.con_sec == 1:
                        print("石を置く位置を入力してください")
                        next_posi = input()
                        if next_posi == 'quit':
                            break
                        flag, EMsg = fm.next_posi_check(next_posi, next_dia_all, self.turnPlayer)
                        while flag == False:
                            print(EMsg)
                            next_posi = input()
                            flag, EMsg = fm.next_posi_check(next_posi, next_dia_all, self.turnPlayer)
                    else:
                        next_posi = self.alg_sec.get_next_posi_Randam(self.diagrams, next_dia_all, self.turnPlayer)
                        if self.vs_count == 1:
                            print(next_posi+"を着手します。")
                    
            #ログを記録
            Blackcount, Whitecount = fm.stone_count_check(self.diagrams[:,:,self.tempo])
            if Blackcount > Whitecount:
                superiorityPlayer = 1
            elif Blackcount < Whitecount:
                superiorityPlayer = 2
            else:
                superiorityPlayer = 0
                
            data = [self.ID, self.tempo, self.turnPlayer, next_posi, len(next_diaList), Blackcount, Whitecount, self.con_fir, self.con_sec, superiorityPlayer]
            data.extend(self.diagrams[:,:,self.tempo].T.reshape(64))
            add_log = pd.Series(data=data, index=self.log.columns, name=self.tempo)
            self.log = self.log.append(add_log)
            
            #手数をインクリメント    
            self.tempo += 1
            
            #盤面を更新
            if self.passtempo == False:
                for next_dia in next_diaList:
                    if next_dia[int(self.rowList[next_posi[1:]]),int(self.columnList[next_posi[:1]])] == 4 + self.turnPlayer:
                        self.diagrams[:,:,self.tempo] = next_dia.copy()
                    for i in range(0,8):
                        for j in range(0,8):
                            if self.diagrams[i,j,self.tempo] == 4 + self.turnPlayer:
                                self.diagrams[i,j,self.tempo] = self.turnPlayer
                            elif self.diagrams[i,j,self.tempo] == 3 or self.diagrams[i,j,self.tempo] == 4: 
                                self.diagrams[i,j,self.tempo] = self.turnPlayer
            else:
                self.diagrams[:,:,self.tempo] = self.diagrams[:,:,self.tempo-1].copy()
                        
                
            #手番の交代
            if self.turnPlayer == 1:
                self.turnPlayer = 2
            else:
                self.turnPlayer = 1
        
        #終局処理
        Blackcount, Whitecount = fm.stone_count_check(self.diagrams[:,:,self.tempo])
        if Blackcount > Whitecount:
            print(str(Blackcount) + " VS " + str(Whitecount) + " で先手●の勝ちです")
            self.win[0] += 1
        elif Whitecount > Blackcount:
            print(str(Whitecount) + " VS " + str(Blackcount) + " で後手○の勝ちです")
            self.win[1] += 1
        else:
            print("引き分けです")
        
        print("先手" + str(self.win[0]) + "勝 VS 後手" + str(self.win[1]) + "勝")
        self.log.to_csv(os.path.join('log', self.ID + '.csv'), index=False)
        
    def start(self):
        
        self.condition_init()
        for i in range(self.vs_count):
            self.one_game()

if __name__ == "__main__":
    
    othello = Othello(False, 2, 2, Algorithm.random_choice(), Algorithm.random_choice(), 10)
    othello.start()