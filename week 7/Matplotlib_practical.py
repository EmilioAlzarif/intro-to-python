#!/usr/bin/env python
# coding: utf-8

# ### P1. Write a Python code to output the following graphs. (or similar ones)

# In[86]:


get_ipython().system('pip install matplotlib')


# In[87]:


import matplotlib.pyplot as plt
import numpy as np


# ![Screen%20Shot%202019-01-05%20at%2010.56.36%20AM.png](attachment:Screen%20Shot%202019-01-05%20at%2010.56.36%20AM.png)

# In[123]:


x = [0,0,50]
y = [0,0,160]
plt.plot(x,y)
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('Draw a line')

plt.show()


# ![Screen%20Shot%202019-01-05%20at%2010.58.22%20AM.png](attachment:Screen%20Shot%202019-01-05%20at%2010.58.22%20AM.png)

# In[122]:


x = [1,2,3]
y = [2,4,1]
plt.plot(x,y)
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('Sample graph!')

plt.show()


# ![Screen%20Shot%202019-01-05%20at%2011.05.37%20AM.png](attachment:Screen%20Shot%202019-01-05%20at%2011.05.37%20AM.png)

# In[121]:


x = [10,20,30]
y = [20,40,10]
x2 = [10,20,30]
y2 = [40,10,30]

plt.plot(x,y,label = 'line1-width-3',  color = 'blue', linewidth = 3)
plt.plot(x2,y2, label = 'line2-width-5',  color = 'red', linewidth = 5)
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('two or more lines')
plt.legend()

plt.show()


# ![Screen%20Shot%202019-01-05%20at%2011.04.00%20AM.png](attachment:Screen%20Shot%202019-01-05%20at%2011.04.00%20AM.png)

# In[120]:


x = [10,20,30]
y = [20,40,10]
x2 = [10,20,30]
y2 = [40,10,30]

plt.plot(x,y,label = 'line1-dotted',  color = 'blue', linewidth = 3, linestyle = 'dotted')
plt.plot(x2,y2, label = 'line2-dashed',  color = 'red', linewidth = 4, linestyle = 'dashed')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('Different styles')
plt.legend()

plt.show()


# ![Screen%20Shot%202019-01-05%20at%2011.07.01%20AM.png](attachment:Screen%20Shot%202019-01-05%20at%2011.07.01%20AM.png)

# In[119]:


x = [1,4,5,6,7]
y = [2,6,3,6,3]
plt.plot(x,y,  color = 'r',marker = 'o', linewidth = 3, linestyle = 'dashdot')
plt.scatter(x,y, color = 'b', s=250)
plt.title("Display Marker")
plt.show()


# ### P2. Create a file with the following content: 

# ```
# test.txt
# 1 2
# 2 4
# 3 1
# ```

# ### Create the following graph using the data from the file.

# ![Screen%20Shot%202019-01-05%20at%2011.09.40%20AM.png](attachment:Screen%20Shot%202019-01-05%20at%2011.09.40%20AM.png)

# In[116]:


x, y = np.loadtxt('test.txt', delimiter = ',', unpack = True)
plt.plot(x, y)
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title('Loaded from file')
 

plt.show()


# ### P3. Get the following graph given:

# ```
# x = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
# popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]
# ```

# ![image.png](attachment:image.png)

# In[118]:


x = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]
plt.bar(x,popularity, color='b')
plt.xlabel('Languages')
plt.ylabel('Popularity')
plt.title('Popularity of Programming Language \n oct17  ')
plt.show()


# #### Make modifications to get the following graph instead

# ![image.png](attachment:image.png)

# In[127]:


x = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]
colors= ['r', 'black', 'g', 'b', 'y', 'c']
plt.bar(x,popularity, color = colors)
plt.xlabel('Languages')
plt.ylabel('Popularity')
plt.title('Popularity of Programming Language \n oct17  ')
plt.show()


# ### P4. Create the following pie chart.

# ![image.png](attachment:image.png)

# In[142]:


x = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]
colors= ['b', 'orange', 'g', 'r', 'purple', 'sienna']
plt.pie(popularity, labels = x, colors = colors, shadow = True, startangle = 140, explode =(0.1,0,0,0,0,0), autopct="%1.1f%%")
plt.show()


# ### P5. Write a Python program to draw a scatter graph taking a random distribution in X and Y and plotted against each other. You should get something like this.

# ![image.png](attachment:image.png)

# In[7]:


help(np.random)


# In[145]:


import numpy as np
import matplotlib.pyplot as plt
x = np.random.randn(150)
y = np.random.randn(150)
plt.scatter(x, y)
plt.show()

