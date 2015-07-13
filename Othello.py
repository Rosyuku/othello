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
        
def search_posi_all(positions, trun):
    pass

def search_posi_stone(positions, stone_c, stone_r, turn):
    if stone_c == 0 and stone_r == 0:
        pass

def search_posi_direciton(positions, stone_c, stone_r, turn, target, direction):
    positions_with_posi = positions.copy()
    #上方向    
    if direction == 0:
        if positions[stone_c, stone_r-1] == target:
            for i in range(stone_r-2, -1, -1):
                if positions[stone_c, i] == target:
                    pass
                elif positions[stone_c, i] == turn:
                    break
                elif positions[stone_c, i] == 0: 
                    positions_with_posi[stone_c, i] = 3
                    for j in range(stone_r-1, i):
                        positions_with_posi[stone_c, j] = 4
                        return positions_with_posi
    elif direction == 1:
        pass
    elif direction == 2:
        pass               
    elif direction == 3:
        if positions[stone_c, stone_r+1] == target:
            for i in range(stone_r+2, 8):
                if positions[stone_c, i] == target:
                    pass
                elif positions[stone_c, i] == turn:
                    break
                elif positions[stone_c, i] == 0: 
                    positions_with_posi[stone_c, i] = 3
                    for j in range(stone_r+1, i):
                        positions_with_posi[stone_c, j] = 4
                        return positions_with_posi            
    elif direction == 4:
        pass
    elif direction == 5:
        pass
    elif direction == 6:
        pass
    elif direction == 7:
        pass

#初期化
column = np.array(['a','b','c','d','e','f','g','h'])
row = np.array(['1','2','3','4','5','6','7','8']).transpose()
positions = np.zeros((8,8,100))
condition = {'1':'人間',
             '2':'CPU'}
#対局条件設定
print("対局条件を入力してください。")
print("先攻 1：人間　2：CPU")
print('  ---------------------------------')
con_fir = input()
print("後攻 1：人間　2：CPU")
print('  ---------------------------------')
con_sec = input()
print(condition[str(con_fir)] + " VS " + condition[str(con_sec)] + " でゲームを始めます")


positions[1,1,0] = 1
positions[3,3,0] = 2
positions[7,7,0] = 1

show_position(column, row, positions[:,:,0])





