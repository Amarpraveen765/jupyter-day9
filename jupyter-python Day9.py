#!/usr/bin/env python
# coding: utf-8

# ## Data structures
# 
#   * Dictionaries 

# ### Dictionaries
# 
#   * it works on the concept of set unique data
#   * Keys,Values is the unique identifier for a value
#   * each key separated from its values with colon(:)
#   * Each key and value is separated by comma(,)
#   * Dictionary enclosed with curly braces({})
#   

# In[5]:


d1 = {"name":"Gitam"}
print(d1)
d2 = {"name":"Gitam","email":"gitam@gmail.com","address":"Hyderabad"}
print(d2)


# In[8]:


d1["name"]


# In[10]:


d1["email"] = "gitam-python@gmail.com" # update the data
d1["email"]


# In[11]:


del d1["email"] # delete the specific key value


# In[12]:


d1["email"] # error due to removal of the data


# In[13]:


d1 # del d1 will delete the entire dict object


# In[16]:


d2.keys() # returns the list of keys


# In[18]:


d2.values() # returns the list of values


# In[19]:


d2.items() #returns the list of tuples of keys and values


# ### Tuples
# * t1 paranthesis(li square brackets[]
# * Differenve between list and tuples
#       * lists are mutable - can be changed/modified
#              - used to access modify , Add,Delete data
#       * tuples are immutable - cannot be changed 
#              - used to access data only   
# 

# In[21]:


t1 = (1,2,3,4,5,6)
t1
type(t1)


# ### Contact Application
# * add contact 
# * search the content 
# * list all contacts
#      - name1 : phone1
#      - name2 : phone2
# * modify the contact 
# * remove the contact
# * import the contact

# In[25]:


# add contact
contacts = {} # creating a dict object
def addcontact(name,phone):
    if name not in contacts: # conditon to check name only
        contacts[name] = phone
        print("Contact details are added")
    else:
        print("Contact details already exists")
    return
addcontact("anil","9645218542")
addcontact("naveen","8754261534")
addcontact("anil2","7954281453")
addcontact("anil","9645218542")


# In[26]:


contacts


# In[28]:


# search for contact details
def searchcontact(name):
    if name in contacts:
        print(name," : ",contacts[name])
    else:
        print("%s does not exists" % name)
    return
searchcontact("anil")
searchcontact("harsha")
searchcontact("naveen")


# In[29]:


# import some contacts
# merge the contacts with existing one
def importcontact(newcontacts):
    contacts.update(newcontacts)
    print(len(newcontacts.keys()),"Contacts added successfully")
    return
newcontacts = {"dinesh":9964251358,"ajay":9945128455}
importcontact(newcontacts) 


# In[30]:


contacts


# In[32]:


# delete a contact
def deletecontact(name):
    if name in contacts:
        del contacts[name]
        print(name,"deleted successfully")
    else:
        print(name,"not exists")
    return
deletecontact("ajay")


# In[34]:


contacts


# In[36]:


# update the contact details
def deletecontact(name,phone):
    if name in contacts:
        contacts[name] = phone
        print(name,"Updated successfully")
    else:
        print(name,"not exists")
    return
deletecontact("anil",9945213524)
deletecontact("ajay",99452132545) 


# # strings

# In[42]:


# classical version
li = ["python","Programming"]
print("%s %s "% (li[0],li[1]))


# In[43]:


print("{0} {1}".format(li[0] , li[1]))


# In[45]:


li1 = [1,2,3,4]
print("%d %d %d %d " % (li1[0],li1[1],li1[2],li1[3]))


# In[46]:


print("{0} {1} {2} {3} ".format(li1[0],li1[1],li1[2],li1[3]))


# ## Boolean Function (True and False)
#   
#   * islower() --True if the string is lower case/False if the string not in lower case
#   * isupper() --True if the string is upper case/False if the string not in upper case
#   * istitle() --True if the string follows title case/False if the string not follows title case
#   * isalpha() --True if the string contains only alaphabets/False
#   * isnumeric() --True if the string contains only numbers/False
#   * isspace() --True if the string contains only space/False

# In[47]:


s1 = "GITAM"
print(s1.islower())
print(s1.isupper())


# In[49]:


s2 ="Python Programming"
s3 ="python Programming"
print(s2.istitle())
print(s3.istitle())


# In[50]:


s2 ="Application1889"
s3 ="Python Programming"
print(s2.isalpha())
print(s3.isalpha())


# In[51]:


s2 ="1234"
s3 ="Application1889"
print(s2.isnumeric())
print(s3.isnumeric())


# In[52]:


s2 =" "
s3 ="Py th on"
print(s2.isspace())
print(s3.isspace())


# ## String Methods
#    
#     * 1. join() -- Method will concatinates the two stings
#     * 2. split() -- returns the listring seperated by widespaces
#     * 3. replace() -- replaces the specfic word/character wher ever need

# In[62]:


s1 = "Python"
print(" ".join(s1))


# In[63]:


s2 = "python programming"
print(",".join(s2))


# In[64]:


s2 = ["python","programming"]
print(",".join(s2))


# In[65]:


s2 = "python programming"
print(s2.split())


# In[66]:


s2 = "python programming"
print(s2.split("o"))


# In[67]:


s2 = "python programming"
li = s2.split()
print(li)
print(len(li))


# In[68]:


s2 = "python programming"
li = list(s2)
print(li)


# In[69]:


s2 = "python programming"
print(s2.replace("gra","Application"))


# ## Packages and Modules
# #### Packages:
# 
# - A collection of Modules(Single Python file .py) and Subpackages
# 
# #### Module
# 
# - A single Python file containing set functions
# 
# Packages -- > Sub Packages -- > Modules -- > Functions -- > Statements

# In[70]:


# Import the externals packages to Python File
import math
math.floor(123.45)


# In[71]:


from math import factorial as fact
fact(5)


# In[72]:


from math import gcd as gcd
gcd(10,15)


# In[73]:


# Function to generate N random numbers in given range
import random
def randomNNumbers(n,lb,ub):
    for i in range(0,n):
        print(random.randint(lb,ub),end=" ")
    return
randomNNumbers(10,0,100)


# In[74]:


# Create a Simple Game
# Generate 20 random numbers 0 to 500
# Input : Number
# Output : Congrats!!
#          Try once again!!!

def generateNumbers(n,lb,ub):
    li = []
    for i in range(0,n):
        li.append(random.randint(lb,ub))
    return li
def check(n):
    if n in li:
        return "Congrats!!!"
    else:
        return "Try once again!!!"
    return

check(15)


# In[ ]:




