#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 12 00:45:44 2018

@author: kazuyuki
"""

import random
import numpy as np

columnList = {'a':0,'b':1,'c':2,'d':3,'e':4,'f':5,'g':6,'h':7}
rowList = {'1':0,'2':1,'3':2,'4':3,'5':4,'6':5,'7':6,'8':7}
Inv_columnList = {v:k for k, v in columnList.items()}
Inv_rowList = {v:k for k, v in rowList.items()}

class random_choice:
    
    def __init__(self):
        pass
    
    def get_next_posi(self, diagrams, next_dia_all, next_diaList, turn):
        next_posi_enable = []
        for i in range(0,8):
            for j in range(0,8):
                if next_dia_all[i,j] == turn + 4:
                    next_posi_enable.append(str(Inv_columnList[j])+str(Inv_rowList[i]))
    
        return random.choice(next_posi_enable)
    
class max_choice:
    
    def __init__(self):
        pass
    
    def get_next_posi(self, diagrams, next_dia_all, next_diaList, turn):
        next_count = []
        for next_dia in next_diaList:
            next_count.append((next_dia==turn).sum() + (next_dia==turn+2).sum() + (next_dia==turn+4).sum())
        
        next_count = np.array(next_count)
        targets = np.where(next_count == next_count.max())
        
        target = random.choice(targets[0])
        next_dia = next_diaList[target]
        tmp = np.where(next_dia == turn+4)
        
        next_posi = str(Inv_columnList[tmp[1][0]])+str(Inv_rowList[tmp[0][0]])

        return next_posi