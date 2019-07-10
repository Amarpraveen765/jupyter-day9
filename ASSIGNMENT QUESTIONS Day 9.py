#!/usr/bin/env python
# coding: utf-8

# In[11]:


# 1.python program to print the fibonacci series in the reverse order
def reverseFibonacci(n):
    a = 0 
    b = 1 
    f = [a,b]
    for i in range(2, n):   
        c= a + b
        f.append(c)
        a = b
        b = c
    for i in range(n - 1, -1 , -1):   
        print(f[i],end=" ")
n = int(input("enter a number"))        
reverseFibonacci(n) 


# In[ ]:


# 2. The program must accept N integers as the input. 
#The program must print the sum of non repeated integers as the output. 
# If there is no non repeated integer then the program must print -1 as the output.
def add(n):
    a=[]
    s=0
    for i in range(n):
        a.append(int(input()))
    for i in range(n):
        c=0
        for j in range(n):
            if i!=j:
                if a[i]==a[j]:
                    c+=1
        if c==0:
            s=s+a[i]
    return s
add(int(input("no of values")))


# In[ ]:


#3. The program must accept two string values S1 and S2. The program must print the pattern as shown in the 

#Example Input/Output sections.

#Boundary Condition(s):

#1 <= Length of S1, S2 <= 100

#Example Input/Output 1:

#Input:

#bad water

#Output: bw aa dt *e *r
def comb(a,b):
    if len(a)<len(b):
        n=len(b)
    else:
        n=len(a)
    for i in range(n):
        if i not in range(len(a)) and i in range(len(b)):
            print("*",b[i])
        elif i in range(len(a)) and i not in range(len(b)): 
            print(a[i],"*")
        else:
            print(a[i],b[i])
a=str(input("enter a string "))
b=str(input("enter a string "))
comb(a,b)


# In[ ]:


#4. The program must accept a string S as the input. 
#The program print the longest word from the string S as the output. 
#If two or more longest words are of same length then consider the first one.
def large(a,b):
    if len(a)>=len(b):
        return a
    elif len(a)==len(b):
        return a
    else:
        return b
    return
s=str(input("enter str:"))
s=s.split()
large(s[0],s[1])


# In[ ]:


# 5. Your program need to accept a string (alphanuermic) includes white spaces also. 
#The program must print the output in the following way.
def alpha(a):
    a=a.split()
    for i in range (len(a)):
        if a[i].istitle()==True:
            print(a[i].upper(),end= " ")
    return
n=str(input("enter str:"))
alpha(n
     )


# In[ ]:


# 6 The program must accept an integer N as the input. The program must print the Nth term in the series as the output.
def findNthTerm(n): 
    if n % 2 == 0: 
        n //= 2
        print(3 ** (n - 1)) 
    else: 
        n = (n // 2) + 1
        print(2 ** (n - 1)) 
if __name__=='__main__':
    N = 3
    findNthTerm(N) 
    N = 21
    findNthTerm(N)


# In[15]:


# 7 The program must accept an integer N the input. 
#The program must print the desired pattern as shown in the
def pattern(n):
    for i in range(len(n)):
        n[i]=int(n[i])
    for i in range(len(n)):
        print("|",end="")
        for j in range(n[i]):
            print("*",end="")
        print("")
    return
x=input("enter num")
pattern(list(x))


# In[ ]:


#8. Your Program has to read one string as well as one character and 
#you need to remove the all the occurance of the character.

#HebeonTech,e -- HbonTch
def delete(n,target):
    c=0
    for i in range(len(n)):
        if n[i]==target:
            c+=1
    print(n.replace(target,"",c))
n=str(input("enter a string"))
target=str(input("enter a char"))
delete(n,target)


# In[ ]:


# 9. Your Program need to accept two strings and generate the output in merging of both strings.
def comb(a,b):
    c=a+b
    return c 
a=str(input("enter a string "))
b=str(input("enter a string "))
comb(a,b)


# In[ ]:


# 10. Series Generations 1, 3, 9, 27, 81, ...
a = int(input("enter the end of series"))
s = 1
i = 1
while(s <= a):
    print(s,end=",")
    s =s*3
    


# In[ ]:


# 11. Series Generations:-  1, 2, 4, 8, 16, 32, 64, 128, 256, ...
n = int(input("enter the end of series"))
sum = 1
i = 1
while(sum <= n):
    
    print(sum,end=" ")
    sum =sum * 2
    


# In[ ]:


# 12. Series Generations:-  1 3 8 15 27 50 92 169 311
n = int(input("enter the end of series"))
s=0
a=1
b=3
c=4
print(a,b,end=" ")
while(s <= n):
    s = a+b+c
    print(s,end=" ")
    a = b
    b = c
    c = s

            
    


# In[ ]:


# 13. Series Generations:-  2 15 41 80 132 197 275 366 470 587
n = int(input("enter the end of series"))
s=0
a=2
i=1
b=0
print(a,end=" ")
while(s <= n):
    b =(13*i)
    s = a + b
    print(s,end=" ")
    a = s
    i=i+1


# In[12]:


#14. Series Generations:-  1! + 2! + 3! + 4! + 5! + ... + n!
def fact(a):
    f=1
    for i in range (1,a+1):
        f*=i
    return f   
def series(m):
    s=0
    for x in range (1,n+1):
        s=s+fact(x)
    return s
n=int(input("enter n"))
series(n)


# In[8]:


#15 Series Generations:-  1,9,17, 33,49,73,97
import math
def seriesgen3(n):
    s= 1
    i=2
    while i<=n+1:
        a=math.ceil(i/2)
        s=s+8*(a-1)
        print(s,end=" ")
        i=i+1
    return 
seriesgen3(10)


# In[ ]:




