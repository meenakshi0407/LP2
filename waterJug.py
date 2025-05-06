# -*- coding: utf-8 -*-
"""
Created on Mon May  5 19:55:39 2025

@author: Meenakshi
"""

from collections import deque

def waterJug(jug1_cap,jug2_cap,target):
    visited=set()
    queue=deque()
    
    queue.append((0,0))
    
    while queue:
        
        jug1,jug2=queue.popleft()
        
        if((jug1,jug2) in visited):
            continue
        
        visited.add((jug1,jug2))
        
        print(f"Jug1: {jug1}L,jug2 :{jug2}L")
        
        if(jug1==target or jug2==target):
            return True
        
        next_state=[
            
            (jug1_cap,jug2),
            (jug1,jug2_cap),
            (0,jug2),
            (jug1,0),
            (0,jug1+jug2) if (jug1+jug2<=jug2_cap) else ((jug1-(jug2_cap-jug2)),jug2_cap),
            (jug1+jug2,0) if (jug1+jug2<=jug1_cap) else (jug1_cap,(jug2-(jug1_cap-jug1)))
            
            ]
        for state in next_state:
            if state not in visited:
                queue.append(state)
    
    print("No solution is there")
    return False


jug1_cap=5
jug2_cap=2
target=4

waterJug(jug1_cap, jug2_cap, target)
        
        
        
        