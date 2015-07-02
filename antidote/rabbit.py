# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 12:54:12 2015

@author: sangeet
"""

meetings = [[0, 1], [1, 2], [2, 3], [3, 5], [4, 5]]

def answer(meetings):
    som = sorted(meetings)
    lis = []
    i=0
    while i < len(som):
        j=i
        base = som[j][1]
        if base <= som[(j)][0]:
            lis.append(som[j])
            print(lis,(i,j,base))
            base = som[j][1]
        j=j+1
        i=i+1
            
    ans = lis
    return ans
    
print answer(meetings)