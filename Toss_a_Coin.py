# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 15:09:35 2020

@author: Manoj Bonam
"""

# -*- coding: utf-8 -*-
"""
Problem:
    There are N coins, each showing either heads or tails. We would like all the coins to form a sequence of heads and tails.
    What is the minimum number of coins that must be reversed to achieve this?

Translation:
    Write a function that, given an array A consisting of N integers representing the coins, returns the minumim number of coins that must be reversed.
    Consecutive elements of array A represent consecutive coins and contain either a 0(heads) or a 1(tails). N is an integer witin the range [1...100]
    Each element in the array A is an integer that can be either 0 or 1.

Example:
#1. Given array A=[1,0,1,0,1,1]
    After resversing the sixth coin, we achieve an alternating sequence of coins. The function should return:
    Minimum number of coins need to reversed = 1
    The new array A=[1,0,1,0,1,1]
    
#2. Given array A=[1,1,0,1,1]
    After resversing the first and fifth coin, we achieve an alternating sequence of coins. The function should return:
    Minimum number of coins need to reversed = 2
    The new array A=[0,1,0,1,0]
    
#3. Given array A=[0,1,0]
    They are already in the correct pattern. The function should return:
    Minimum number of coins need to reversed = 0
    The new array A=[0,1,0]    

#4. Given array A=[0,1,1,0]
    After rvesersing the first and second coin, we achieve an alternating sequence of coins. The function should return:
    Minimum number of coins need to reversed = 2
    The new array A=[1,0,1,0]    

"""

'''This function takes in an array of 1s and 0s and rerranges them to either 01 or 10 pattern '''
import re
def rearrangeTheCoins(lst):
    lstLen = len(lst)
    #Converting the input list inetgers to a string to get the count of 01s and 10s
    list_to_string = ''.join(str(s) for s in lst )
    
    #Find the the number of 01 occurrences in the string.
    pattern_01 = re.compile('01')
    matches_01 = pattern_01.finditer(list_to_string) 
    i_01 = 0
    for match in matches_01:
        i_01 += 1     

    #Find the the number of 10 occurrences in the string.
    pattern_10 = re.compile('10')
    matches_10 = pattern_10.finditer(list_to_string) 
    i_10 = 0
    for match in matches_10:
        i_10 += 1
    
    turnToHeads = 0
    turnToTails = 0
    totalReversed = 0
    
    try:
       if lst[0] == 0 and i_01 >= i_10:   #If the list starts with 0 and we have more 01's. let's make it a 01 pattern list.
           for index in range(1,lstLen):
               if index%2 != 0:
                   if lst[index] != 1:
                       lst[index] = 1
                       turnToTails += 1
               else:
                   if lst[index] != 0:
                       lst[index] = 0
                       turnToHeads += 1
           totalReversed = turnToTails + turnToHeads  
       elif lst[0] == 1 and i_10 >= i_01: #If the list starts with 1 and we have more 10's. let's make it a 10 pattern list.
           for index in range(1,lstLen):
               if index%2 != 0:
                   if lst[index] != 0:
                       lst[index] = 0
                       turnToHeads += 1
               else:
                   if lst[index] != 1:
                       lst[index] = 1
                       turnToTails += 1          
           totalReversed = turnToTails + turnToHeads
    except Exception as e:
        print(f'Exception Occured{e}')
        return lst,-1
    else:        
        return lst,totalReversed
    

'''This function takes in an array of 1s and 0s and decides if reaggranging it in which pattern(01 or 10) with minimun number of coin turns '''

def giveMeYourCoins(lst):
    lstDup = lst[:]
    #Call the master functinon to rearrange the coins
    returnLstOrig,numCoinTurnsOrig = rearrangeTheCoins(lst) 
    
    #If the firtst element is 1, replace it with 0 and see how many coins would have to be turned to get the desired pattern
    if lstDup[0] == 1:
        lstDup[0] = 0
    
    #Call the master functinon again to rearrange the coins    
    returnLstAlt,numCoinTurnsDup = rearrangeTheCoins(lstDup) 
    numCoinTurnsDup += 1 #Incerement the var, to account for the first element we turned to 1
    
    if numCoinTurnsDup < numCoinTurnsOrig:
        return returnLstAlt,numCoinTurnsDup
    else:
        return returnLstOrig,numCoinTurnsOrig
    

'''Test the modules'''    
coin_lst = [0,0,1,1,0,1,1]
lst_output,numOfTurns=giveMeYourCoins(coin_lst)    
print(f'Modified new list is: {lst_output}\n Number of coins that were turned are/is: {numOfTurns}')
#Output:
#Modified new list is [0, 1, 0, 1, 0, 1, 0]
#Number of coins that were turned are/is: 3


coin_lst = [1,1,0,1,0,1,1,1]
lst_output,numOfTurns=giveMeYourCoins(coin_lst)    
print(f'Modified new list is: {lst_output}\n Number of coins that were turned are/is: {numOfTurns}')
#Output:
#Modified new list is [0, 1, 0, 1, 0, 1, 0, 1]
#Number of coins that were turned are/is: 2

coin_lst = [1,0,1,0,1,1]
lst_output,numOfTurns=giveMeYourCoins(coin_lst)    
print(f'Modified new list is: {lst_output}\n Number of coins that were turned are/is: {numOfTurns}')
#Output:
#Modified new list is [1, 0, 1, 0, 1, 0]
#Number of coins that were turned are/is: 1

coin_lst = [1,1,0,1,1]
lst_output,numOfTurns=giveMeYourCoins(coin_lst)    
print(f'Modified new list is: {lst_output}\n Number of coins that were turned are/is: {numOfTurns}')
#Output:
#Modified new list is [0, 1, 0, 1, 0]
#Number of coins that were turned are/is: 2

coin_lst = [0,1,0]
lst_output,numOfTurns=giveMeYourCoins(coin_lst)    
print(f'Modified new list is: {lst_output}\n Number of coins that were turned are/is: {numOfTurns}')
#Output:
#Modified new list is [0, 1, 0]
#Number of coins that were turned are/is: 0

coin_lst = [0,1,1,0]
lst_output,numOfTurns=giveMeYourCoins(coin_lst)    
print(f'Modified new list is: {lst_output}\n Number of coins that were turned are/is: {numOfTurns}')
#Output:
#Modified new list is  [0, 1, 0, 1]
#Number of coins that were turned are/is: 2



























    
        