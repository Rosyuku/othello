#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 12 00:45:44 2018

@author: kazuyuki
"""

import random

columnList = {'a':0,'b':1,'c':2,'d':3,'e':4,'f':5,'g':6,'h':7}
rowList = {'1':0,'2':1,'3':2,'4':3,'5':4,'6':5,'7':6,'8':7}
Inv_columnList = {v:k for k, v in columnList.items()}
Inv_rowList = {v:k for k, v in rowList.items()}

class random_choice:
    
    def __init__(self):
        pass
    
    def get_next_posi_Randam(self, diagrams, next_dia_all, turn):
        next_posi_enable = []
        for i in range(0,8):
            for j in range(0,8):
                if next_dia_all[i,j] == turn + 4:
                    next_posi_enable.append(str(Inv_columnList[j])+str(Inv_rowList[i]))
    
        return random.choice(next_posi_enable)