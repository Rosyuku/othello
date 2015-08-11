# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 22:45:52 2015

@author: Wakasugi Kazuyuki
"""

import numpy as np

columnList = {'a':0,'b':1,'c':2,'d':3,'e':4,'f':5,'g':6,'h':7}
rowList = {'1':0,'2':1,'3':2,'4':3,'5':4,'6':5,'7':6,'8':7}
Inv_columnList = {v:k for k, v in columnList.items()}
Inv_rowList = {v:k for k, v in rowList.items()}

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
            pass
            #print(columnArray[column],rowArray[row],directions)
            #print(diagram)
            #print(new_diagram)
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
    return diagram_possibility_all, diagram_possibilities        

#入力された手の妥当性を確認
def next_posi_check(next_posi, next_dia, turnPlayer):
    ErrMSG = ""
    if len(next_posi) != 2:
        ErrMSG = "2文字で入力してください。"
        return False, ErrMSG
    elif next_posi[:1] != 'a' and next_posi[:1] != 'b' and next_posi[:1] != 'c' and next_posi[:1] != 'd'\
    and next_posi[:1] != 'e' and next_posi[:1] != 'f' and next_posi[:1] != 'g' and next_posi[:1] != 'h':
        ErrMSG = "先頭の文字はa,b,c,d,e,f,g,hのいずれかを入力してください。"
        return False, ErrMSG
    elif next_posi[1:] != '1' and next_posi[1:] != '2' and next_posi[1:] != '3' and next_posi[1:] != '4'\
    and next_posi[1:] != '5' and next_posi[1:] != '6' and next_posi[1:] != '7' and next_posi[1:] != '8':
        ErrMSG = "先頭の文字は1,2,3,4,5,6,7,8のいずれかを入力してください。"
        return False, ErrMSG
    elif turnPlayer == 1 and next_dia[int(rowList[next_posi[1:]]),int(columnList[next_posi[:1]])] == 5:
        return True,  ErrMSG
    elif turnPlayer == 2 and next_dia[int(rowList[next_posi[1:]]),int(columnList[next_posi[:1]])] == 6:
        return True,  ErrMSG
    else:
        ErrMSG = "ルール上打てる場所を選んでください。"
        return False, ErrMSG  
        
#石の数をカウントする
def stone_count_check(diagram):
    black = 0
    white = 0
    for i in range(0,8):
        for j in range(0,8):
            if diagram[i,j] == 1:
                black += 1
            elif diagram[i,j] == 2:
                white += 1
    return black, white