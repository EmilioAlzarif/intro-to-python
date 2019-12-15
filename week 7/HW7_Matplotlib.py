#!/usr/bin/env python
# coding: utf-8

# In[2]:


import matplotlib.pyplot as plt
import numpy as np


# ### P1. Write a Python code to output the following graph. (or a similar one)
# ```
# The productivity values for the 3 groups are the following: 
# 
# g1 = [80, 60, 80, 67, 34]
# g2 = [45, 67, 23, 89, 10]
# g3 = [30, 90, 50, 20, 90]
# ```

# ![image.png](attachment:image.png)

# In[33]:


g = np.array([[80, 60, 80, 67, 34],[45, 67, 23, 89, 10],[30, 90, 50, 20, 90]])
ind = np.arange(5)
b_w= 0.20
t= ['M', 'T', 'W', 'Th', 'F']
plt.bar(ind, g[0], b_w, label='Group1')
plt.bar(ind+b_w, g[1], b_w, label='Group2')
plt.bar(ind+b_w*2, g[2], b_w, label='Group3')

plt.xlabel('Groups')
plt.ylabel('Popularity')
plt.title('Productivity during the week')
plt.legend()
plt.xticks(ind + b_w, t )

plt.show()


# ### P2. Write a Python code to output the following graph. (or a similar one)
# ```
# Draw 25 dots. Generate random x and y coordinates (integers from 1 to 30), random colors and random sizes (integers from 20 to 500) for the dots.
# ```
# 
# ```
# Նկարեք 25 կետեր. Կետերի համար գեներացրեք պատահական x և y կոորդինատներ (1-ից 30 միջակայքում int տիպի թվեր), պատահական գույներ ու պատահական չափսեր (20-ից 500 միջակայքում int տիպի թվեր)։
# ```

# ![image.png](attachment:image.png)

# In[159]:


x = np.random.randint(0,30,50)
y = np.random.randint(0,30,50)

c=np.random.randint(100,400,50)
s=np.random.randint(100,400,50)
plt.title('Colorful dots')
plt.xlabel('X')
plt.ylabel('Y')

plt.scatter(x,y,c,s)

plt.show()

