#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import scipy.signal as sig
import matplotlib.pyplot as plt
import matplotlib.backends.backend_pdf


# In[33]:


s1= 8.522006938
s2=11.22578937

s3=8.659283558

avg1 = 2.279843397


avg2=3.570262065

    avg3=1.635627415



data = [avg1, avg2, avg3]

std_error1 = s1 / 15
std_error2 = s2/ 10

#define chart 
options = ['Differences of Maximum Flexion', 'Differences of Minimum Flexion','Differences of Average Flexion']
c=['tab:orange', 'tab:green', 'tab:red']

#create chart
plt.figure(figsize=[15,7])
for i in np.arange (-10, 15, 2.5):
    plt.axhline(y = i, color = 'gainsboro', linestyle = '-',zorder=1)
#hacerlo con boxplot
plt.bar(options, #x-coordinates of bars
       height=data, #height of bars
       color = c, #colors
       yerr=[s1,s2,s3], #error bar width
       capsize=4, #length of error bar caps
       zorder=2) 
colors = {'Maximum Flex':'tab:orange', 'Minimum Flex':'tab:green', 'Average Flex':'tab:red'}         
labels = list(colors.keys())
handles = [plt.Rectangle((0,0),1,1, color=colors[label]) for label in labels]
plt.legend(handles, labels)

plt.ylabel("Differences of Flexion between Methods (degrees)")


# In[35]:


s1= 7.417759215
 
s2=6.843014641


s3=7.15110603


avg1 =9.554052277



avg2=11.31010517


avg3=10.7409384




data = [avg1, avg2, avg3]

std_error1 = s1 / 15
std_error2 = s2/ 10

#define chart 
options = ['Differences of Maximum Flexion', 'Differences of Minimum Flexion','Differences of Average Flexion']
c=['tab:orange', 'tab:green', 'tab:red']

#create chart
plt.figure(figsize=[15,7])
for i in np.arange (-10, 15, 2.5):
    plt.axhline(y = i, color = 'gainsboro', linestyle = '-',zorder=1)
plt.bar(options, #x-coordinates of bars
       height=data, #height of bars
       color = c, #colors
       yerr=[s1,s2,s3], #error bar width
       capsize=4, #length of error bar caps
       zorder=2) 
colors = {'Maximum Flex':'tab:orange', 'Minimum Flex':'tab:green', 'Average Flex':'tab:red'}         
labels = list(colors.keys())
handles = [plt.Rectangle((0,0),1,1, color=colors[label]) for label in labels]
plt.legend(handles, labels)

plt.ylabel("Differences of Flexion between Methods (degrees)")


# In[3]:


s1= 13.58322404

s2=7.250240345

avg1 = 135.6245357
avg2=140.6947978




data = [avg1,avg2]

std_error1 = s1 / 10
std_error2 = s2/ 10

#define chart 
options = ['Werium', 'OpenPose']
c=['tab:orange', 'tab:green']

#create chart
plt.figure(figsize=[8,7])
plt.axhline(y = avg2, color = 'tab:red', linestyle = '--',zorder=3)
for i in np.arange (0, 200, 20):
    plt.axhline(y = i, color = 'gainsboro', linestyle = '-',zorder=1)
plt.bar(options, #x-coordinates of bars
       height=data, #height of bars
       color = c, #colors
       yerr=[s1,s2], #error bar width
       capsize=4, #length of error bar caps
       zorder=2) 
colors = {'Werium':'tab:orange', 'OpenPose':'tab:green'}         
labels = list(colors.keys())
handles = [plt.Rectangle((0,0),1,1, color=colors[label]) for label in labels]
plt.legend(handles, labels)

plt.ylabel("Minimum Flexion (dregrees)")


# In[4]:


s1= 12.71834498
s2=7.448410728


avg1 = 143.3037905
avg2=144.9674011




data = [avg1,avg2]

std_error1 = s1 / 10
std_error2 = s2/ 10

#define chart 
options = ['Werium', 'OpenPose']
c=['tab:orange', 'tab:green']

#create chart
plt.figure(figsize=[8,7])
plt.axhline(y = avg2, color = 'tab:red', linestyle = '--',zorder=3)
for i in np.arange (0, 200, 20):
    plt.axhline(y = i, color = 'gainsboro', linestyle = '-',zorder=1)
plt.bar(options, #x-coordinates of bars
       height=data, #height of bars
       color = c, #colors
       yerr=[s1,s2], #error bar width
       capsize=4, #length of error bar caps
       zorder=2) 
colors = {'Werium':'tab:orange', 'OpenPose':'tab:green'}         
labels = list(colors.keys())
handles = [plt.Rectangle((0,0),1,1, color=colors[label]) for label in labels]
plt.legend(handles, labels)

plt.ylabel("Average Flexion (dregrees)")


# In[ ]:





# In[36]:


s1= 4.351766482
s2=8.737303765
avg1 = 2.619271429
avg2=13.9293766




data = [avg1,avg2]

std_error1 = s1 / 15
std_error2 = s2/ 15

#define chart 
options = ['Werium', 'OpenPose']
c=['tab:orange', 'tab:green']

#create chart
plt.figure(figsize=[8,7])
plt.axhline(y = avg2, color = 'tab:red', linestyle = '--',zorder=3) 
for i in np.arange (0, 50, 10):
    plt.axhline(y = i, color = 'gainsboro', linestyle = '-',zorder=1)
plt.bar(options, #x-coordinates of bars
       height=data, #height of bars
       color = c, #colors
       yerr=[s1,s2], #error bar width
       capsize=4, #length of error bar caps
       zorder=2) 
colors = {'Werium':'tab:orange', 'OpenPose':'tab:green'}         
labels = list(colors.keys())
handles = [plt.Rectangle((0,0),1,1, color=colors[label]) for label in labels]
plt.legend(handles, labels)

plt.ylabel("Minimum Extension (dregrees)")


# In[33]:


s1= 3.123664718

s2=9.015588155


avg1 = -7.101485714
avg2=3.521630848




data = [avg1,avg2]

std_error1 = s1 / 10
std_error2 = s2/ 10

#define chart 
options = ['Werium', 'OpenPose']
c=['tab:orange', 'tab:green']

#create chart
plt.figure(figsize=[8,7])
plt.axhline(y = avg2, color = 'tab:red', linestyle = '--',zorder=3)
for i in np.arange (0, 50, 20):
    plt.axhline(y = i, color = 'gainsboro', linestyle = '-',zorder=1)
plt.bar(options, #x-coordinates of bars
       height=data, #height of bars
       color = c, #colors
       yerr=[s1,s2], #error bar width
       capsize=4, #length of error bar caps
       zorder=2) 
colors = {'Werium':'tab:orange', 'OpenPose':'tab:green'}         
labels = list(colors.keys())
handles = [plt.Rectangle((0,0),1,1, color=colors[label]) for label in labels]
plt.legend(handles, labels)

plt.ylabel("Maximum Extension (dregrees)")


# In[35]:


s1= 3.285566247

s2=8.881353701



avg1 = -2.041139872

avg2=8.699798533





data = [avg1,avg2]

std_error1 = s1 / 10
std_error2 = s2/ 10

#define chart 
options = ['Werium', 'OpenPose']
c=['tab:orange', 'tab:green']

#create chart
plt.figure(figsize=[8,7])
plt.axhline(y = avg2, color = 'tab:red', linestyle = '--',zorder=3)
for i in np.arange (0, 50, 20):
    plt.axhline(y = i, color = 'gainsboro', linestyle = '-',zorder=1)
plt.bar(options, #x-coordinates of bars
       height=data, #height of bars
       color = c, #colors
       yerr=[s1,s2], #error bar width
       capsize=4, #length of error bar caps
       zorder=2) 
colors = {'Werium':'tab:orange', 'OpenPose':'tab:green'}         
labels = list(colors.keys())
handles = [plt.Rectangle((0,0),1,1, color=colors[label]) for label in labels]
plt.legend(handles, labels)

plt.ylabel("Average Extension (dregrees)")


# In[ ]:




