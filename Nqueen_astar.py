# -*- coding: utf-8 -*-
"""
Created on Mon May  5 20:17:12 2025

@author: Meenakshi
"""

import heapq

def calculateAttck(state):
    n=len(state)
    attack=0
    for i in range(n):
        for j in range(i+1,n):
            if(state[i]==state[j] or abs(state[i]-state[j])==abs(i-j)):
                attack+=1
    return attack

def nearest_neighbor(state):
    neighbors=[]
    n=len(state)
    for i in range(n):
        for j in range(n):
            if state[i]!=j:
                neighbor=list(state)
                neighbor[i]=j
                neighbors.append(neighbor)
    return neighbors

def NQueen(n):
    start=tuple(range(n))
    heap=[(calculateAttck(start),start)]
    visited=set()
    
    while heapq:
        cost,state=heapq.heappop(heap)
        
        if calculateAttck(state)==0:
            return state
        visited.add(state)
        
        for neighbor in nearest_neighbor(state):
            neighbor=tuple(neighbor)
            if neighbor not in visited:
                heapq.heappush(heap,(calculateAttck(neighbor),neighbor))
    return None
    

n=4
ans=NQueen(n)
print(ans)