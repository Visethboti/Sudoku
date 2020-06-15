# -*- coding: utf-8 -*-
"""
Created on Mon Jun 15 11:09:00 2020

@author: Hister
"""
import time
for i in range(100000):
    #time.sleep(0.5)
    print(i, end='\r')
    
    """
t =     [[0, 0, 0, 0, 0, 0, 9, 0, 0],
         [7, 0, 0, 9, 0, 0, 0, 3, 0],
         [0, 0, 0, 0, 3, 0, 1, 0, 7],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [4, 0, 3, 1, 0, 0, 2, 5, 0],
         [0, 0, 6, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 7, 0, 0, 3],
         [0, 9, 7, 5, 8, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 4 ,0, 0]]
output = ""
output += "\n".join(map(str, t))
print(output)