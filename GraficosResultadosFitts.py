#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import scipy.signal as sig
import matplotlib.pyplot as plt
import matplotlib.backends.backend_pdf


# In[6]:


s1= 24.06922012

s2=1.469270081
s3=24.31159397

avg1 = 24.54149232


avg2=2.018919071
avg3=22.52257325




data = [avg1,avg2]

std_error1 = s1 / 15
std_error2 = s2/ 15

#define chart 
options = ['Standard Mouse', 'OpenPose']
c=['tab:blue', 'tab:red']

#create chart
plt.figure(figsize=[8,7])
for i in np.arange (0, 50, 5):
    plt.axhline(y = i, color = 'gainsboro', linestyle = '-',zorder=1)
plt.bar(options, #x-coordinates of bars
       height=data, #height of bars
       color = c, #colors
       yerr=[s1,s2], #error bar width
       capsize=4, #length of error bar caps
       zorder=2) 
colors = {'Standard Mouse':'tab:blue', 'OpenPose':'tab:red'}         
labels = list(colors.keys())
handles = [plt.Rectangle((0,0),1,1, color=colors[label]) for label in labels]
plt.legend(handles, labels)

plt.ylabel("IP (bits/s)")


# In[19]:


s1= 0.027045444


s2=0.120395981

s3=24.31159397

avg1 = 0.008928571



avg2=0.1625

avg3=22.52257325




data = [avg1,avg2]

std_error1 = s1 / 15
std_error2 = s2/ 15

#define chart 
options = ['Standard Mouse', 'OpenPose']
c=['tab:blue', 'tab:red']

#create chart
plt.figure(figsize=[8,7])
for i in np.arange (0, 0.3, 0.05):
    plt.axhline(y = i, color = 'gainsboro', linestyle = '-',zorder=1)
plt.bar(options, #x-coordinates of bars
       height=data, #height of bars
       color = c, #colors
       yerr=[s1,s2], #error bar width
       capsize=4, #length of error bar caps
       zorder=2) 
colors = {'Standard Mouse':'tab:blue', 'OpenPose':'tab:red'}         
labels = list(colors.keys())
handles = [plt.Rectangle((0,0),1,1, color=colors[label]) for label in labels]
plt.legend(handles, labels)

plt.ylabel("Error rate (%)")


# In[11]:


s1= 249.2639329


s2=530.7636685

s3=24.31159397

avg1 = 1740.035714



avg2=3388.482143

avg3=22.52257325




data = [avg1,avg2]

std_error1 = s1 / 15
std_error2 = s2/ 15

#define chart 
options = ['Standard Mouse', 'OpenPose']
c=['tab:blue', 'tab:red']

#create chart
plt.figure(figsize=[8,7])
for i in np.arange (0, 4500, 500):
    plt.axhline(y = i, color = 'gainsboro', linestyle = '-',zorder=1)
plt.bar(options, #x-coordinates of bars
       height=data, #height of bars
       color = c, #colors
       yerr=[s1,s2], #error bar width
       capsize=4, #length of error bar caps
       zorder=2) 
colors = {'Standard Mouse':'tab:blue', 'OpenPose':'tab:red'}         
labels = list(colors.keys())
handles = [plt.Rectangle((0,0),1,1, color=colors[label]) for label in labels]
plt.legend(handles, labels)


plt.ylabel("MT (ms)")


# In[18]:


s1= 0.316976344


s2=0.141091691

s3=24.31159397

avg1 = 1.688257143



avg2=0.625207143

avg3=22.52257325




data = [avg1,avg2]

std_error1 = s1 / 15
std_error2 = s2/ 15

#define chart 
options = ['Standard Mouse', 'OpenPose']
c=['tab:blue', 'tab:red']

#create chart
plt.figure(figsize=[8,7])
for i in np.arange (0, 3, 0.5):
    plt.axhline(y = i, color = 'gainsboro', linestyle = '-',zorder=1)
plt.bar(options, #x-coordinates of bars
       height=data, #height of bars
       color = c, #colors
       yerr=[s1,s2], #error bar width
       capsize=4, #length of error bar caps
       zorder=2) 
colors = {'Standard Mouse':'tab:blue', 'OpenPose':'tab:red'}         
labels = list(colors.keys())
handles = [plt.Rectangle((0,0),1,1, color=colors[label]) for label in labels]
plt.legend(handles, labels)


plt.ylabel("TP (bits/s)")


# In[ ]:




