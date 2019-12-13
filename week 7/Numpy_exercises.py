#!/usr/bin/env python
# coding: utf-8

# # Numpy exercises
# 

# #### 1. Import the numpy package under the name `np`
# 
# #### Import արեք numpy module-ը np անունով:

# In[1]:


import numpy as np


# #### 2. Create a numpy array of size 10 filled with zeros. 
# 
# #### Ստեղծեք 10 չափի 0-ներով լցված numpy array:

# In[11]:


x = np.zeros(10)
x


# #### 3.  How to get the documentation of the numpy add function? 
# 
# #### Նայեք numpy-ի add ֆունկցիայի դոկումենտացիան:

# In[8]:


help(np.add)


# #### 4.  Create a numpy array of size 10 filled with zeros but the fifth value is 1 
# 
# #### Ստեղծեք 10 չափի 0-ներով լցված numpy array, որի 5րդ արժեքը 1 է:

# In[12]:


x = np.zeros(10)
x[4] = 1
x


# #### 5.  Create a numpy array with values ranging from 10 to 49
# 
# #### Ստեղծեք 10-ից 49 հաջորդական թվերով numpy array:

# In[30]:


x = np.arange(10,49)
x


# #### 6.  Reverse the numpy array ranging from 0 to 50. 
# 
# #### Ստեղծեք 0-ից 50 հաջորդական թվերով numpy array և տպեք այն շրջած ձևով:

# In[50]:


x = np.arange(0,51)
x[::-1]


# #### 7.  Create a 3x3 matrix with values ranging from 0 to 8 
# 
# #### Ստեղծեք 0-ից 8 հաջորդական թվերով 3x3 numpy array

# In[115]:


x = np.arange(0,9).reshape(3,3)
x


# #### 8. Find indices of non-zero elements from \[1,2,0,0,4,0\]
# 
# #### Տրված է \[1,2,0,0,4,0\] numpy array-ը, գտեք ոչ-զրոյական արժեքներով տարրերի կոորդինատները:

# In[76]:


x = [1,2,0,0,4,0]
np.nonzero(x)


# #### 9. Create a 3x3x3 array with random integers from 1 to 20
# 
# #### Ստեղծեք 1-ից 20 պատահական թվերով լցված (3x3x3) չափանի numpy array:

# In[100]:


x = np.random.randint(1,20,(3,3,3))
x


# #### 10. Create a 10x10 array with random values and find the minimum and maximum values 
# 
# #### Ստեղծեք պատահական թվերով լցված (10x10) չափանի numpy array ու տպեք դրա փոքրագույն ու մեծագույն արժեքները:

# In[152]:


x = np.random.rand(10,10)
x


# In[148]:


np.amax(x)


# In[150]:


np.amin(x)


# #### 11. Create a random vector of size 30 and find the mean value 
# 
# #### Ստեղծեք 30 չափանի պատահական թվերով լցված numpy array ու տպեք դրա միջին արժեքը:

# In[158]:


x = np.random.rand(30)
x


# In[162]:


np.mean(x)


# #### 12. Given a 1D array ranging from 0 to 10, print all the elements which are between 3 and 8. 
# 
# #### Ստեղծեք 0-ից 10 հաջորդական թվերով numpy array: Տպեք բոլոր արժեքները, որոնք 3-ից 8 միջակայքում են:

# In[181]:


x = np.arange(0,11)
x[slice(4,8)]   # or x[4:8]


# #### 13. Given a 1D array of 20 random integers from 0 to 10, multiply the values that are less than 5 by 2 and print the resulting array.
# 
# #### Ստեղծեք 1-ից 10 պատահական ամբողջ թվերով լցված 20 չափանի numpy array: Բազմապատկեք 5-ից փոքր արժեք ունեցող տարերրը 2-ով ու տպեք արդյունքում ստացված array-ը:

# In[232]:


x = np.random.randint(0,10,20)
2*x[x<5]


# #### 14. Given the 1D array [1, 5, 6, 2, -2, 23, 45], find the indices of the array elements that are divisible by 2.
# 
# #### Տրված է [1, 5, 6, 2, -2, 23, 45] numpy array-ը, գտեք 2-ի բաժանվող տարրերի կոորդինատները:

# In[234]:


x = np.array([1,5,6,2,-2,23,45])
print(np.where(x%2==0))


# #### 15. Given a 1D array ranging from 0 to 20, print all the elements which are divisible by 3. 
# 
# #### Ստեղծեք 1-ից 20 հաջորդական թվերով լցված numpy array, տպեք բոլոր 3-ի բաժանվող տարրերի արժեքները:

# In[238]:


x = np.arange(0,21)
print(x)
print(x[x%3==0])


# #### 16. Create a 5x5 numpy array with each row values ranging from 0 to 4 
# 
# #### Ստեղծեք 5x5 numpy array, որի ամեն տող իրենից ներկայացնում է 0-ից 4 հաջորդական թվեր:

# In[263]:


x = np.arange(0,5)
np.tile(x,(5,1))


# #### 17. Create a 3x5 numpy array filled with random numbers from 1 to 10.
# 
# #### 17. Ստեղծեք 1-ից 10 պատահական թվերով լցված (3, 5) չափերով numpy array։

# In[285]:


x = np.random.randint(1,11,(3,5))
x


# #### 18. Create a numpy array of size 10 filled with 0s and replace its 5th value with a 3.
# 
# #### 18. Ստեղծեք 10 չափի 0-ներով լցված numpy array ու փոխարինեք դրա 5-րդ արժեքը 3 թվով։

# In[290]:


x = np.zeros(10)
x[4]=3
x


# #### 19. Create a numpy array filled with numbers from 3 to 15 i.e. ([3, 4 … 13, 14])
# 
# #### 19. Ստեղծեք 3-ից 15 թվերից բաղկացած numpy array ([3, 4 … 13, 14])

# In[ ]:


x = np.arange(3,15)
x


# 20. Write a function which gets a numpy array as an input and divides all of the array values by 2 over and over again, until the mean of the array numbers is <=5. Then, once the mean of the array numbers is <=5, the funtion returns the modified numpy array.
# 20. Գրեք ֆունկցիա, որը ստանում է numpy array ու բաժանում է դրա բոլոր արժեքները 2-ի այնքան ժամանակ մինչև որ դրանց միջին արժեքը լինի <=5։ Այնուհետև, հենց միջին արժեքը դառնում է <=5, ֆունկցիան վերադարձնում է փոփոխված numpy array-ը։

# In[108]:


x = np.arange(0,30)
def f(arr):
    while np.mean(arr)>5:
        arr = arr/2
    return np.mean(arr), arr
f(x)

# 21. Write a function which gets a 5x4 numpy array filled with random numbers from 1 to 10 as an inputand returns 4 different numpy arrays which are the columns of the original numpy array. Write another similar function which returns 5 different numpy arrays which are rows of the original numpy array. 

# 21. Գրեք ֆունկցիա, որը ստանում է 1-ից 10 պատահական թվերով լցված 5x4 numpy array ու վերադարձնում է 4 տարբեր numpy array-ներ, որոնք սկզբնական numpy array-ի սյուներն են։ Գրեք նմանատիպ ֆունկցիա, որը վերադարձնում է 5 տարբեր numpy array-ներ, որոնք սկզբնական numpy array-ի տողերն են։
# In[106]:


def col(arr):
    return (arr[...,0],arr[...,1],arr[...,2],arr[...,3])
def row(arr):
    return (arr[0,...],arr[1,...],arr[2,...],arr[3,...],arr[4,...])
print(col(np.random.randint(1,10,(5,4))))
print(row(np.random.randint(1,10,(5,4))))

