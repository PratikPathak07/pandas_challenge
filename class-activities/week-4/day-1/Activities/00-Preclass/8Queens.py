# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 20:15:48 2019

@author: benny
"""
import numpy as np

#check function 
def check(k, j):
    #check row and column 
    for i in range(Q):
        if board[i][j] == 1:
            return False
    
    #check left diagonal
    i = k-1
    m = j-1    
    while (i>=0 and m>=0):
        if board[i][m]==1:
            return False
        i-=1
        m-=1
        
    #check right diagonal
    i=k-1
    m=j+1
    while (i>=0 and m<=Q-1):
        if board[i][m]==1:
            return False
        i-=1
        m+=1
           
    return True




def findQueen(i):
    global count
    #print board after one solution
    if i > Q-1:
        count+=1
        print(board)
        print('Next')
        print('-------------------------------------')
        return 
    #recursive call in here
    for m in range(Q):
        #check if the condition is true
        if (check(i,m)):
            board[i][m]=1
            #step by step print
            #print(board)
            #print("------------------------------------")
            findQueen(i+1)
            board[i][m]=0
            
count=0
Q=int(input('How many queens and set the matrix?'))
board=np.zeros((Q,Q),dtype=int)
findQueen(0)    
print('Total solutions:'+str(count))




