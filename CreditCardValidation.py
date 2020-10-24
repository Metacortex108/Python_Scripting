# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 15:35:42 2020

@author: Manoj

"""
#A valid credit card from ABCD Bank has the following characteristics:

# It must start with a 4,5 or 6.
# It must contain exactly 16 digits.
# It must only consist of digits (0-9).
# It may have digits in groups of 4, separated by one hyphen "-".
# It must NOT use any other separator like ' ' , '_', etc.
# It must NOT have 4 or more consecutive repeated digits.

#Input Format

#The first line of input contains an integer N .
#The next N  lines contain credit card numbers.

#Constraints
#0<N<100

#Output Format

#Print 'Valid' if the credit card number is valid. Otherwise, print 'Invalid'



import re

def creditCardsValidity(cardNum):
    
    isValid = True
    isInvalid = False
    outResults = []
    firstElement = True
    
    try:
        while len(cardNum) > 0:
            #Check 1
            if firstElement:
                textVal = str(cardNum[0])
                firstElementLen = len(textVal)
            
                matches = re.match(r'[\d]', str(cardNum[0]))
                
                if matches and firstElementLen == 1 :
                   outResults.insert(0,isValid)
                else:
                   outResults.insert(0,isInvalid)
            
                firstElement = False
                del cardNum[0]
                
            #Check 2   
            matches = re.match(r'[4-6]',str(cardNum[0])) #can also use (str(cardNum[0]).startswith(('4','5','6)))
            if not matches: #matches will be None i.e False if nothing matched
                outResults.append(isInvalid)
                del cardNum[0] 
                continue
           
            if str(cardNum[0]).find('-') > 0 :
                #Check 5
                matches = re.match(r'\d{4}-\d{4}-\d{4}-\d{4}',str(cardNum[0]))
                if not matches:
                   outResults.append(isInvalid)
                   del cardNum[0] 
                   continue
            
            #Check 6
            pattern = re.compile(r'0000|1111|2222|3333|4444|5555|6666|7777|8888|9999')
            matches=pattern.finditer(str(cardNum[0]).replace('-',''))
            numOfMatches = 0
            for match in matches:
               numOfMatches += 1
            if numOfMatches > 0:
                outResults.append(isInvalid)
                del cardNum[0] 
                continue 
            
            #Check 3&4   
            pattern = re.compile(r'[\d]') #this checks #3
            matches = pattern.finditer(str(cardNum[0]))        
            numOfDigits = 0
            for match in matches:
                numOfDigits += 1 
                
            matches = re.search(r'^[0-9-]+$',str(cardNum[0])) #This checks if all are digits or not i.e. Check #4

            if numOfDigits != 16 or not matches:
                outResults.append(isInvalid)
                del cardNum[0] 
                continue
            else:
                outResults.append(isValid)
                del cardNum[0] 
                continue              
            
            #All checks cleared
            outResults.append(isValid)
            del cardNum[0] 
        
        else:
            for index,value in enumerate(outResults):
                if outResults[index]:
                    print('Valid')
                else:
                    print('InValid')
    except Exception as e:
        print(f'Exception Occured: {e}')


cardsLst=[9,
      '4123456789123456',
      '41S23456789123456',
      '5123-4567-8912-3456',
      '61234-567-8912-3456',
      '4123356789123456',
      '5133-3367-8912-3456',
      '5123 - 3567 - 8912 - 3456']

creditCardsValidity(cardsLst)

#9 Valid
#4123456789123456 : Valid
#41S23456789123456: Invalid. There is a charecter in the string
#5123-4567-8912-3456 : Valid
#61234-567-8912-3456 : Invalid, because the card number is not divided into equal groups of 4
#4123356789123456 : Valid
#5133-3367-8912-3456 : Invalid, consecutive digits 3333  is repeating 4 times.
#5123 - 3567 - 8912 - 3456 : Invalid, because space '  ' and - are used as separators.
             