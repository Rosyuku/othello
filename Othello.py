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
                sentence += ' '
            elif p == 1:
                sentence += '●'
            elif p == 2:
                sentence += '○'
            elif p == 3:
                sentence += '-'
            elif p == 4:
                sentence += '-'
            elif p == 5:
                sentence += '■'
            elif p == 6:
                sentence += '□'
            sentence += ' | ' 
        print(sentence)
        print('  ---------------------------------')


#石を置ける位置を全方位探索
def search_all_directions(diagram, row, column, turn, opturn):
    directions = np.zeros(8)
    new_diagram = diagram.copy()
    new_diagram_temp = diagram.copy()
    possible = False
    if diagram[row,column] != 0:
        return possible, new_diagram
    else:
        #左上
        if(column > 1 and row > 1):
            if(diagram[row-1, column-1] == opturn):               
                directions[0] = 1
                new_diagram_temp[row-1,column-1] = turn + 2
                for i in range(2,9):
                    if(row-i>=0 and column-i>=0):
                        if(diagram[row-i,column-i]==0):
                            new_diagram_temp = new_diagram.copy()
                            break
                        elif(diagram[row-i,column-i]==opturn):
                            new_diagram_temp[row-i,column-i] = turn + 2
                        else:
                            new_diagram = new_diagram_temp.copy()
                            new_diagram[row,column] = turn + 4
                            new_diagram_temp = new_diagram.copy()
                            directions[0] = 2
                            possible = True
                            break
                    else:
                        new_diagram_temp = new_diagram.copy()
                        break
        #上
        if(row > 1):
            if(diagram[row-1, column] == opturn):
                directions[1] = 1
                new_diagram_temp[row-1,column] = turn + 2
                for i in range(2,9):
                    if(row-i>=0):
                        if(diagram[row-i,column]==0):
                            new_diagram_temp = new_diagram.copy()
                            break
                        elif(diagram[row-i,column]==opturn):
                            new_diagram_temp[row-i,column] = turn + 2
                        else:
                            new_diagram = new_diagram_temp.copy()
                            new_diagram[row,column] = turn + 4
                            new_diagram_temp = new_diagram.copy()
                            directions[1] = 2
                            possible = True
                            break
                    else:
                        new_diagram_temp = new_diagram.copy()
                        break
        #右上
        if(column < 6 and row > 1):
            if(diagram[row-1, column+1] == opturn):
                directions[2] = 1
                new_diagram_temp[row-1,column+1] = turn + 2
                for i in range(2,9):
                    if(row-i>=0 and column+i<=7):
                        if(diagram[row-i,column+i]==0):
                            new_diagram_temp = new_diagram.copy()
                            break
                        elif(diagram[row-i,column+i]==opturn):
                            new_diagram_temp[row-i,column+i] = turn + 2
                        else:
                            new_diagram = new_diagram_temp.copy()
                            new_diagram[row,column] = turn + 4
                            new_diagram_temp = new_diagram.copy()
                            directions[2] = 2
                            possible = True
                            break
                    else:
                        new_diagram_temp = new_diagram.copy()
                        break
        #左
        if(column > 1):
            if(diagram[row, column-1] == opturn):
                directions[3] = 1
                new_diagram_temp[row,column-1] = turn + 2
                for i in range(2,9):
                    if(column-i>=0):
                        if(diagram[row,column-i]==0):
                            new_diagram_temp = new_diagram.copy()
                            break
                        elif(diagram[row,column-i]==opturn):
                            new_diagram_temp[row,column-i] = turn + 2
                        else:
                            new_diagram = new_diagram_temp.copy()
                            new_diagram[row,column] = turn + 4
                            new_diagram_temp = new_diagram.copy()
                            directions[3] = 2
                            possible = True
                            break
                    else:
                        new_diagram_temp = new_diagram.copy()
                        break
        #右
        if(column < 6):
            if(diagram[row, column+1] == opturn):
                directions[4] = 1
                new_diagram_temp[row,column+1] = turn + 2
                for i in range(2,9):
                    if(column+i<=7):
                        if(diagram[row,column+i]==0):
                            new_diagram_temp = new_diagram.copy()
                            break
                        elif(diagram[row,column+i]==opturn):
                            new_diagram_temp[row,column+i] = turn + 2
                        else:
                            new_diagram = new_diagram_temp.copy()
                            new_diagram[row,column] = turn + 4
                            new_diagram_temp = new_diagram.copy()
                            directions[4] = 2
                            possible = True
                            break
                    else:
                        new_diagram_temp = new_diagram.copy()
                        break
        #左下
        if(column > 1 and row < 6):
            if(diagram[row+1, column-1] == opturn):
                directions[5] = 1
                new_diagram_temp[row+1,column-1] = turn + 2
                for i in range(2,9):
                    if(row+i<=7 and column-i>=0):
                        if(diagram[row+i,column-i]==0):
                            new_diagram_temp = new_diagram.copy()
                            break
                        elif(diagram[row+i,column-i]==opturn):
                            new_diagram_temp[row+i,column-i] = turn + 2
                        else:
                            new_diagram = new_diagram_temp.copy()
                            new_diagram[row,column] = turn + 4
                            new_diagram_temp = new_diagram.copy()
                            directions[5] = 2
                            possible = True
                            break
                    else:
                        new_diagram_temp = new_diagram.copy()
                        break
        #下
        if(row < 6):
            if(diagram[row+1, column] == opturn):
                directions[6] = 1
                new_diagram_temp[row+1,column] = turn + 2
                for i in range(2,9):
                    if(row+i<=7):
                        if(diagram[row+i,column]==0):
                            new_diagram_temp = new_diagram.copy()
                            break
                        elif(diagram[row+i,column]==opturn):
                            new_diagram_temp[row+i,column] = turn + 2
                        else:
                            new_diagram = new_diagram_temp.copy()
                            new_diagram[row,column] = turn + 4
                            new_diagram_temp = new_diagram.copy()
                            directions[6] = 2
                            possible = True
                            break
                    else:
                        new_diagram_temp = new_diagram.copy()
                        break
        #右下
        if(column < 6 and row < 6):
            if(diagram[row+1, column+1] == opturn):
                directions[7] = 1
                new_diagram_temp[row+1,column+1] = turn + 2
                for i in range(2,9):
                    if(row+i<=7 and column+i<=7):
                        if(diagram[row+i,column+i]==0):
                            new_diagram_temp = new_diagram.copy()
                            break
                        elif(diagram[row+i,column+i]==opturn):
                            new_diagram_temp[row+i,column+i] = turn + 2
                        else:
                            new_diagram = new_diagram_temp.copy()
                            new_diagram[row,column] = turn + 4
                            new_diagram_temp = new_diagram.copy()
                            directions[5] = 2
                            possible = True
                            break
                    else:
                        new_diagram_temp = new_diagram.copy()
                        break
                
        if possible == True:
            print(columnArray[column],rowArray[row],directions)
            print(diagram)
            print(new_diagram)
        return possible, new_diagram

#石を置ける位置を探索
def search_newstone_position_all(diagram, turn):
    diagram_possibility_all = diagram.copy()
    diagram_possibilities = []
    possibilities = 0
    if turn == 1:
        opturn = 2
    else:
        opturn = 1
        
    for column in range(0,8):
        for row in range(0,8):
            possible, new_diagram = search_all_directions(diagram, row, column, turn, opturn)
            if possible == True:
                diagram_possibilities.append(new_diagram)
                possibilities += 1
                diagram_possibility_all = np.maximum(new_diagram, diagram_possibility_all)
    return diagram_possibility_all        

#初期化
columnArray = np.array(['a','b','c','d','e','f','g','h'])
rowArray = np.array(['1','2','3','4','5','6','7','8']).transpose()
diagrams = np.zeros((8,8,100))
condition = {'1':'人間',
             '2':'CPU'}
gameset = False
turnPlayer = 1
tempo = 0
             
#対局条件設定
print("対局条件を入力してください。")
print("先攻 1：人間　2：CPU")
print('  ---------------------------------')
con_fir = input()
print("後攻 1：人間　2：CPU")
print('  ---------------------------------')
con_sec = input()
print(condition[str(con_fir)] + " VS " + condition[str(con_sec)] + " でゲームを始めます")

"""
#対局部分
while(gameset == True):
    #手数をインクリメント    
    tempo += 1
    
    #手番の交代
    if turnPlayer == 1:
        turnPlayer = 2
    else:
        turnPlayer = 2
"""      

diagrams[2,1,0] = 1
diagrams[2,2,0] = 2
diagrams[2,3,0] = 2
diagrams[3,3,0] = 1
diagrams[3,4,0] = 2
diagrams[4,3,0] = 2
diagrams[4,4,0] = 1
diagrams[7,7,0] = 1

show_position(columnArray, rowArray, diagrams[:,:,0])
next_dia = search_newstone_position_all(diagrams[:,:,0], 1)
show_position(columnArray, rowArray, next_dia)





