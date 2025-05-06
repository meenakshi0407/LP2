# -*- coding: utf-8 -*-
"""
Created on Tue May  6 22:01:20 2025

@author: Meenakshi
"""

def TOH(n,A,B,C):
    if (n==0):
        return
    TOH(n-1,A,C,B)
    print("Move Disk ",n,"from",A," to ",C)
    TOH(n-1,B,A,C)
    
n=3

TOH(n,'A','B','C')
