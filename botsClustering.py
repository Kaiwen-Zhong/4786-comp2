# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 22:29:26 2016

@author: kaiwen
"""

import numpy as np
import collections

def seqScore(bot_o, botComp):
    """
    BUG: running for forever
    """
    score = 0
    T = 5
    bot = clean(bot_o, T)
    lengthBot = len(bot)
    lengthComp = len(botComp)
    length = min(lengthBot, lengthComp)        
    i = 0

    while i<length:
        if bot[i] == botComp[i]:
            score+=1
        i+=1
    return score
    

def clean(l, threshold):
    remove_list = []
    count_dict = collections.Counter(l)
    new_bot = l[:]
    for n in count_dict:
        if count_dict[n]<threshold:
            remove_list.append(n)
    for r_n in remove_list:
        new_bot = remove(new_bot, r_n)
    return new_bot


def remove(l, r_n):
    l_new = [x for x in l if x != r_n]
    return l_new



if __name__ =='__main__':
    dataset = np.loadtxt('observations.csv', delimiter=',')
    
    bot1 = dataset[0]
    bot2 = dataset[4]
    bot3_o = dataset[5]
    bot3 = clean(bot3_o, 5)
    
    bots1 = []
    bots2 = []
    bots3 = []
    
    for i in range(len(dataset)):
        score1 = seqScore(dataset[i], bot1)
        score2 = seqScore(dataset[i], bot2)
        score3 = seqScore(dataset[i], bot3)
        if score1>score2 and score1>score3:
            bots1.append(dataset[i])
        elif score2>score1 and score2>score3:
            bots2.append(dataset[i])
        else:
            bots3.append(dataset[i])
    
    np.savetxt('bots1.csv', bots1, delimiter=',', fmt='%f')
    np.savetxt('bots2.csv', bots3, delimiter=',', fmt='%f')
    np.savetxt('bots3.csv', bots3, delimiter=',', fmt='%f')


        
        
    
    