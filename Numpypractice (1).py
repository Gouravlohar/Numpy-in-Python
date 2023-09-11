#!/usr/bin/env python
# coding: utf-8

# # Dealing with NumPy

# In[1]:


import numpy as np
myarr= np.array([2,6,3,5])
myarr


# this is one dimensional array

# In[2]:


myarr.dtype


# In[3]:


myarr.shape


# In[4]:


myarr


# In[5]:


myarr[2]


# In[6]:


myarr[2]=45


# In[7]:


myarr


# In[8]:


myarr1= np.array([[2,6,3,5]])


# this is 2 dimensional aaray

# In[9]:


myarr1


# In[10]:


myarr1[0,2]


# In[11]:


myarr1[0,2]=22


# In[12]:


myarr1#it will print array


# # Conversion from other Python structures

# In[13]:


lstarray=np.array([[2,5,7,5,8],[7,9,7,5,1]])


# In[14]:


lstarray


# In[15]:


lstarray.dtype


# In[16]:


lstarray.shape


# In[17]:


lstarray.size


# In[18]:


np.array({2,6,5,4})


# **Array Creation from Dictonary**

# In[19]:


lstarray1=np.array({2,7,8,9,57,5})


# In[20]:


lstarray1


# In[21]:


lstarray1.size


# In[22]:


lstarray.shape


# In[23]:


lstarray1.shape


# # Intrinsic numpy array array creation objects (e.g., arange, ones, zeros, etc.)

# In[24]:


zero=np.zeros((2,5))


# In[25]:


zero


# In[26]:


rng=np.arange(15)


# In[27]:


rng


# In[28]:


one=np.ones((2,5))


# In[29]:


one


# In[30]:


rng=np.arange(1,10,2)#last one is jumpindex=2


# In[31]:


rng


# In[32]:


rng=np.arange(2)


# In[33]:


rng


# In[34]:


rng1=np.arange(101)


# In[35]:


rng


# In[36]:


rng1


# In[37]:


rng1=np.arange(1,101,2)


# In[38]:


rng1


# In[39]:


rng1=np.arange(99)


# In[40]:


rng1


# In[41]:


np.arange(3,33)


# **linespace:- it will create a array with same line space it 1st and 2nd number will give the exact range of the number and the third one will give you how many number do you want to print**

# In[42]:


lnsp=np.linspace(1,5,3)


# In[43]:


lnsp


# In[44]:


lnsp=np.linspace(1,5,10)


# In[45]:


lnsp


# **empty will give your desired empty array with random values of so you can change as per your need in row and column**

# In[46]:


emp=np.empty((2,6))


# In[47]:


emp


# **emptylike makes a copy of your old array and make it empty so that u can change as per your need**

# In[48]:


emplike=np.empty_like(lnsp)


# In[49]:


emplike


# **np.identity will give you identity matrix of 0,1**

# In[50]:


ide=np.identity(20)


# In[51]:


ide


# In[52]:


ide.shape


# **now there is 2 more method is present np.reshape and np.ravel**

# **reshape will convert a 1d array into matrix form but u have to give the correct multiplication like 44(in 1d)=2x22(in 2d)**

# In[53]:


arr=np.arange(44)


# In[54]:


arr


# In[55]:


arr=arr.reshape(44,1)


# In[56]:


arr


# **ravel will convert 2d into 1d**

# In[57]:


arr.ravel()


# In[58]:


arr.shape


# In[59]:


arr=arr.ravel()


# In[60]:


arr.shape


# In[61]:


arr.shape


# **matrix operation /axis**

# In[62]:


x=[[1,3,5],[5,8,2],[4,2,3]]


# In[63]:


ar=np.array(x)


# In[64]:


ar


# In[65]:


ar.sum(axis=0) #it will  add the column wise here there is 3 column (axis=0)


# In[66]:


ar.sum(axis=1)# it will add the row (axis=1)


# In[67]:


ar.T #to transpose a matrix capital T is used


# In[68]:


for i in ar:
    print(i)


# In[69]:


for i in ar.flat:
    print(i)        #flat will give you a single single line


# In[70]:


a=np.array([1,47,5,8,66])


# In[71]:


a.argmax()#argmax will give u a index where the maximum value is present


# In[72]:


a.argmin()#argmax will give u a index where the minimum value is present


# In[73]:


a.argsort()#argsort will give you a sorted array but in index form means which index is an sorted manner


# In[74]:


ar


# In[75]:


ar.argmax()


# In[76]:


ar.argmin()


# In[77]:


ar.argmax(axis=0)


# In[78]:


ar.argmax(axis=1)


# In[79]:


ar.argmin(axis=0)


# In[80]:


ar.argmin(axis=1)


# In[81]:


ar.argsort()


# In[82]:


ar.reshape((9,1))


# In[83]:


ar.ravel()


# In[84]:


ar.reshape((3,3))


# # MATRIX OPERATION

# In[85]:


mat1=np.arange(9)


# In[86]:


mat1


# In[87]:


mat1=mat1.reshape((3,3))


# In[88]:


mat2=np.arange(9,18)


# In[89]:


mat2


# In[90]:


mat2=mat2.reshape((3,3))


# In[91]:


mat1+mat2


# In[92]:


mat1*mat2


# In[93]:


mat1-mat2


# In[94]:


np.sqrt(mat1)#square of elements


# **To check why numpy is used instead of simple python array**

# In[ ]:


import sys


# In[ ]:


py_s= [2,78,5,8]


# In[ ]:


np_s= np.array(py_s)


# In[ ]:


sys.getsizeof(1)*len(py_s)#simple python list is taking 112 bytes memory


# In[ ]:


np_s.itemsize*np_s.size#numpy array is using 16 bytes of memory


# **to know more about numpy methods and attributes:- https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html**
