#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  5 14:35:58 2022

@author: arpanrajpurohit
"""

import numpy as np
from numpy.random import choice
import math
import random
import matplotlib.pyplot as plt

M = 200
N = 5000
n = 0.2
y = 0.9

class Robby:
    def __init__(self, x=0, y=0, r=0, c=0): 
        self.x = x
        self.y = y
    def curr(self, grid):
        return grid[self.x][self.y]
    def north(self, grid):
        return grid[self.x][self.y+1]
    def south(self, grid):
        return grid[self.x][self.y-1]
    def east(self, grid):
        return grid[self.x+1][self.y]
    def west(self, grid):
        return grid[self.x-1][self.y]
    
    def pickUp(self, grid): 
        if (grid[self.x][self.y] == 1):
            grid[self.x][self.y] = 0
            return True 
        else:
            return False
    def moveNorth(self, grid): 
        if (self.north(grid) == 3):
            return False
        self.y += 1
        return True 
    def moveSouth(self, grid): 
        if (self.south(grid) == 3):
            return False
        self.y -= 1
        return True 
    def moveEast(self, grid): 
        if (self.east(grid) == 3):
            return False
        self.x += 1
        return True 
    def moveWest(self, grid): 
        if (self.west(grid) == 3):
            return False
        self.x -= 1
        return True
    
    def convState(self, grid): 
        stateVector = (self.curr(grid), self.north(grid), self.south(grid), self.east(grid), self.west(grid))
        return stateVector
    
    def slctAct(self, cur, Qmatrix, epsilon):
        if (random.randint(1,100) <= (100*epsilon)):
            act = random.randint(0,4)
            return act
        pos_actions = list() 
        PU = Qmatrix[cur][0] 
        pos_actions.append(PU)
        N = Qmatrix[cur][1] 
        pos_actions.append(N)
        S = Qmatrix[cur][2] 
        pos_actions.append(S)
        E = Qmatrix[cur][3] 
        pos_actions.append(E)
        W = Qmatrix[cur][4] 
        pos_actions.append(W)
        Max = max(pos_actions) 
        if (Max == N):
            act = 1
        if (Max == PU):
            act = 0
        elif (Max == S):
            act = 2
        elif (Max == E):
            act = 3
        elif (Max == W):
            act = 4
        return act
    
    def prfrmAct (self, act, grid): 
        if (act == 0): 
            suc = self.pickUp(grid)
            if (suc == True):
                self.c += 1
                return 10
            else:
                return -1
        elif (act == 1): 
            suc = self.moveNorth(grid)
            if (suc == True):
                return 0
            else:
                return -5
        elif (act == 2): 
            suc = self.moveSouth(grid)
            if (suc == True):
                return 0
            else:
                return -5
        elif (act == 3): 
            suc = self.moveEast(grid)
            if (suc == True):
                return 0
            else:
                return -5
        elif (act == 4): 
            suc = self.moveWest(grid)
            if (suc == True):
                return 0
            else:
                return -5
            
    def Epi (self, grid, Qmatrix, eps): 
        i = 0 
        while (i < M):
            cur = self.convState(grid)
            if cur not in Qmatrix: 
                Qmatrix[cur] = np.zeros(5)
            act = self.slctAct(cur, Qmatrix, eps)
            rew = self.prfrmAct(act, grid)
            self.r += rew
            new = self.convState(grid)
            if new not in Qmatrix: 
                Qmatrix[new] = np.zeros(5)
            Qmatrix[cur][act] = Qmatrix[cur][act] + n*(rew + y * max(Qmatrix[new]) - Qmatrix[cur][act])
            i+=1
    
    def tstEpisode (self, gd, Qmatrix, eps):
        i = 0 
        while (i < M):
            cur = self.convState(gd)
            act = self.slctAct(cur, Qmatrix, eps)
            rew = self.prfrmAct(act, gd)
            self.r += rew
            i+=1  

    def train (self, Qmatrix):
        k = 0 
        eps = 0.1 
        rew_lst = list()
        while (k < N):
            gd = np.random.randint(2, size=(12, 12)) 
            for i, g in enumerate(gd):
                for j, gr in enumerate(gd[i]):
                    if (j == 0 or j == 11 or i == 0 or i == 11):
                        gd[i][j] = 3
            self.x = random.randint(1,10)
            self.y = random.randint(1,10)
            self.c = 0
            self.r = 0
            self.Epi(gd, Qmatrix, eps)
            print ("Cans :")
            print (self.c)
            print ("Reward:")
            print (self.r)
            print ("Points")
            lst = ((self.c * 10) - self.r)
            print (lst)
            print ("Iter:")
            print (k)
            k+=1
            if ((N-k) % 50 == 0): 
                eps -= 0.001
                rew_lst.append(self.r)
        print ("Average(Training):")
        print (sum(rew_lst)/(N/50))
        plt.plot(rew_lst)
        fg = plt.figure()
        plt.show()

    def test (self, Qmatrix):
        k = 0 
        eps = 0.1 
        rew_lst = list()
        while (k < N):
            gd = np.random.randint(2, size=(12, 12)) 
            for i, g in enumerate(gd):
                for j, gr in enumerate(gd[i]):
                    if (j == 0 or j == 11 or i == 0 or i == 11):
                        gd[i][j] = 3
            self.x = random.randint(1,10)
            self.y = random.randint(1,10)
            self.c = 0
            self.r = 0
            self.tstEpisode (gd, Qmatrix, eps)
            rew_lst.append(self.r)
            k+=1
        print ("Average Rew(Test):")
        print (sum(rew_lst)/N)
        plt.plot(rew_lst)
        fg = plt.figure()
        plt.show()
        
Qmatrix = {}  
robby = Robby()
robby.train(Qmatrix) 
robby.test(Qmatrix) 