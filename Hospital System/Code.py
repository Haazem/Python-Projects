#Define Useful Function

from tkinter import E

from numpy import true_divide


def STR(): return list(input())
def INT(): return int(input())
def MAP(): return map(int, input().split())
def LIST(): return list(map(int, input().split()))
def STRING(): return input()

'''
#Map and Lambda Function Problem

#lambda
cube = lambda x : x ** 3 
                
def fibonacci(n):
    ans = [0 , 1]
    #create fibo
    for i in range(2 , n):
        ans.append(ans[i - 1] + ans[i - 2])
    return ans[0 : n]

n = INT()

print(list(map(cube , fibonacci(n))))

'''


'''
#Validating Email Addresses With a Filter Problem

def check_user(s):
    #check user
    ok = True
    for i in str(s):
        if i.isdigit()==False and i.isalpha()==False:
            if i != '_' and i != '-':
                ok = False
                break
            
    return ok 
        
def check_website(s):
    #check website
    ok = True
    for i in str(s):
        if (i.isalpha() == False):
            if (i.isdigit() == False):
                ok = False
                break
    return ok

def check_extension(s):
    #check extension
    ok = True
    for i in str(s):
        if (i.isalpha() == False ):
            ok = False
            break
        
    if (ok == False or len(s) > 3):
        return False
    return True
    
    
def fun(s):
    #user
    #website 
    #extension
    
    user = ""
    website = ""
    extension = ""
    temp = ""
    j = 0 
    for i in range(len(s)):
        if s[i] == '@':
            j = i
            user = temp 
            temp = ""
            break
        else :
            temp +=s[i]
            
    for i in range(j+1 , len(s)):
        if s[i] == '.':
            website = temp 
            temp = ""
            j = i 
            break
        else :
            temp += s[i]
        
    for i in range(j + 1 , len(s)):
        extension += s[i]
    
    #print(user , website , extension)
         
    if len(user) == 0 or len(website) == 0 or len(extension) == 0 :
        return False
    else:
        user_valid = check_user(user)
        website_valid = check_website(website)
        extension_valid = check_extension(extension)    

        #print(user_valid  , website_valid , extension_valid)
        if (user_valid and website_valid and extension_valid):
            return True
        return False
   
        
def filter_mail(emails):
    return list(filter(fun , emails))

n = INT()
emails = []
for i in range(n):
    s = STRING()
    emails.append(s)
    #print(fun(s))
    
print(filter_mail(emails))

'''

'''
#Python Functionals
from fractions import Fraction
from functools import reduce

def product(fracs):
    m = 1 
    for i in fracs:
        m*= i 
        
    return m.numerator , m.denominator
        

fracs = []
for _ in range(int(input())):
        fracs.append(Fraction(*map(int, input().split())))

print(*product(fracs))

'''








