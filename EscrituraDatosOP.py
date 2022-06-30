#!/usr/bin/env python
# coding: utf-8

# In[7]:


import json
import numpy as np
import scipy.signal as sig
import matplotlib.pyplot as plt
import matplotlib.backends.backend_pdf
get_ipython().run_line_magic('matplotlib', 'inline')
import os
import glob
from sklearn import preprocessing

import csv
import pandas as pd

import sys
get_ipython().system('{sys.executable} -m pip install pyautogui')
import pyautogui
import math


# In[ ]:





# In[8]:


#FUNCIONES

def angles (m,c,h):

    a = np.array([m[0],m[1]]) #muñeca
    b = np.array([c[0],c[1]]) #codo
    c = np.array([h[0],h[1]]) #hombro
    bxax = float(a[0]) - float(b[0])
    byay = float(a[1]) - float(b[1])
    bxcx = float(c[0]) - float(b[0])
    bycy = float(c[1]) - float(b[1])
    ba = [bxax, byay]
    bc = [bxcx, bycy]


    angle = np.arctan2(ba[1], ba[0]) - np.arctan2(bc[1], bc[0])

    return (180-np.degrees(angle))

def data_extraction_dch(path):
    for filename in glob.glob(os.path.join(path, '*.json')):
        with open(os.path.join(os.getcwd(), filename), 'r') as f: # open in readonly mode
            data = json.load(f)
            
        fps =json.dumps(data['fps'])
        currentFps.append(float(fps))
        
        time =json.dumps(data['time'])
        currentTime.append(float(time))
        
        
        mystr = json.dumps(data['people'])
        if mystr == "[]":
            continue
        mystr = mystr[2:-2]
        mystr = mystr.split(":")
        myarray2d = mystr[2].split(", ")
        n = 0
        j=0
        finalarray = []
        for i in range(0,17,1):

            steparray=[]
            steparray.append(myarray2d[j])
            j = j+1
            steparray.append(myarray2d[j])
            j = j+1
            steparray.append(myarray2d[j])
            j = j+1
            finalarray.append(steparray)

        #formato xn,yn,cn donde c es el ratio de confianza entre 0 y 1
        #3 brazo dcho
        #6 brazo izq

        valuescododch = finalarray[3]
        valuesmuñecadch = finalarray[4]
        valueshombrodch = finalarray[2]

        angle = angles(valuesmuñecadch, valuescododch, valueshombrodch)
        plottingangles.append(angle)
        


# In[9]:




plottingangles =[]
a = np.array([])
b = np.array([])
c = np.array([])
currentFps=[]
currentTime=[]


path = "C:/Users/pmsie/Downloads/openpose-masterfpschange/openpose-master/PabloFinal2"
data_extraction_dch(path)

rows = []
csvtimes=[]
csvangles=[]

with open('C:/Users/pmsie/Werium/ProMotionCapture/1_2022-06-21_16.17.42_PABLO_MARTIN_SIERRA_Codo - Derecha.csv', newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=';', quotechar='|')
    for row in csvreader:
        rows.append(row)
    for i in range(1,len(rows),1):
        csvtimes.append(float(rows[i][0].replace(",","."))/1000)
        csvangles.append(float(rows[i][1].replace(",",".")))
        
for i in range (0, len(csvangles), 1):
    #ProMotionCapture registra los valores invertidos, es decir, el 0º es lo más alto y "bajar" es el ángulo más alto aka 180º
    csvangles[i] = csvangles[i]*(-1)           


# In[10]:


#PLOT

times = np.arange(float(0),len(plottingangles),float(1))

#Estableciendo el tiempo de frame con el fps obtenido en OpenPose
for i in range (0,len(plottingangles),1):
    times[i]=times[i]/currentFps[i]
    
for i in range (1,len(currentTime),1):
    times[i] = (currentTime[i]-currentTime[1])/10**9

     
#OJO, PROMOTIONCAPTURE TRAS UNA SERIE DE MUESTRAS REESTABLECE EL TIEMPO A 0!!
for i in range(1,len(csvtimes),1):
    if(csvtimes[i]==0):
        print(i)
        csvtimes = csvtimes[0:i-1]
        csvangles = csvangles[0:i-1]
        break

plt.figure(figsize=[16,4])
plt.plot(times, plottingangles, label = 'OpenPose')
plt.plot(csvtimes,csvangles,label= 'Werium')

plt.axhline(y = 150, color = 'y', linestyle = '--', label = '150º')
plt.axhline(y = 140, color = 'r', linestyle = '-', label = '140º')
plt.axhline(y = 0, color = 'g', linestyle = '-', label = '0º')
plt.xlabel("Seconds")
plt.ylabel("Degrees")
plt.legend()
csvangles=csvangles[0:-200]
csvtimes=csvtimes[0:-200]
#HASTA AQUÍ PLOT SIN SHIFT


# In[11]:


#PEAKS

plt.figure(figsize=[16,4])
plt.plot( plottingangles, label = 'OpenPose')
peaks, properties = sig.find_peaks(x = plottingangles, height = 100, distance= 10)
print(len(plottingangles))
print("Peaks found:",peaks)


for peak in peaks:
    plt.axvline(peak, linestyle = '--', color = "g")
    
plt.figure(figsize=[16,4])
plt.plot( csvangles, label = 'Werium')   
peaks2, properties2 = sig.find_peaks(x = csvangles, height = 100, distance= 10)
print(len(csvangles))
print("Peaks found:",peaks2)   

for peak in peaks2:
    plt.axvline(peak, linestyle = '--', color = "k")


# In[12]:


FmaxO=0
FminO=999
FavgO=0
EmaxO=-999
EminO=999
EavgO=0
Fmax=0
Fmin=999
Favg=0
Emax=-999
Emin=999
Eavg=0
suma=0
for peak in peaks:
    suma = suma + plottingangles[peak]
    if(plottingangles[peak]>FmaxO and plottingangles[peak] <190):
        FmaxO=plottingangles[peak]
    if(plottingangles[peak]<FminO):
        FminO=plottingangles[peak]
FavgO=suma/len(peaks)
suma=0
inversePlottingAngles =np.arange(0,len(plottingangles),1)
for i in range(0, len(inversePlottingAngles),1):
    inversePlottingAngles[i]=plottingangles[i]*-1
    
puntoclave=0    
for i in range(0, len(plottingangles),1):
    if(inversePlottingAngles[i]<-30):
        inversePlottingAngles=inversePlottingAngles[i:-1]
        puntoclave=i
        break
        
plt.figure(figsize=[16,4])
plt.plot( inversePlottingAngles, label = 'OpenPose') 
plt.plot( plottingangles, label = 'OpenPose')
peaks3, properties = sig.find_peaks(x = inversePlottingAngles, height = -40, distance= 10)

for peak in peaks3:
    plt.axvline(peak+puntoclave, linestyle = '--', color = "g")
    plt.axvline(peak, linestyle = '--', color = "r")
    suma = suma + plottingangles[peak+puntoclave]
    if(plottingangles[peak+puntoclave]>EmaxO):
        EmaxO=plottingangles[peak+puntoclave]
    if(plottingangles[peak+puntoclave]<EminO):
        EminO=plottingangles[peak+puntoclave]
EavgO=suma/len(peaks3)
suma=0   
for peak in peaks2:
    suma = suma + csvangles[peak]
    if(csvangles[peak]>Fmax):
        Fmax=csvangles[peak]
    if(csvangles[peak]<Fmin):
        Fmin=csvangles[peak]
Favg=suma/len(peaks2) 
suma=0
inverseCSVAngles =np.arange(0,len(csvangles),1)
for i in range(0, len(inverseCSVAngles),1):
    inverseCSVAngles[i]=csvangles[i]*-1
    
for i in range(0, len(inverseCSVAngles),1):
    if(inverseCSVAngles[i]<-30):
        inverseCSVAngles=inverseCSVAngles[i:-1]
        puntoclave=i
        break

plt.figure(figsize=[16,4])
plt.plot( inverseCSVAngles, label = 'Werium') 
peaks4, properties = sig.find_peaks(x = inverseCSVAngles, height = -40, distance= 20)


for peak in peaks4:
    plt.axvline(peak, linestyle = '--', color = "g")
    suma = suma + csvangles[peak+puntoclave]
    if(csvangles[peak+puntoclave]>Emax):
        Emax=csvangles[peak+puntoclave]
    if(csvangles[peak+puntoclave]<Emin):
        Emin=csvangles[peak+puntoclave]
Eavg=suma/len(peaks4)
suma=0   


# In[13]:


#SHIFTING PLOTS

plottinganglesshift = plottingangles[peaks[0]:-1]
timesshift = times[peaks[0]:-1]
for i in range(1, len(timesshift),1):
    timesshift[i]= timesshift[i]-timesshift[0]
    
csvanglesshift = csvangles[peaks2[0]:-1]
csvtimesshift = csvtimes[peaks2[0]:-1]
for i in range(1, len(csvtimesshift),1):
    csvtimesshift[i]= csvtimesshift[i]-csvtimesshift[0]


plt.figure(figsize=[16,4])
plt.plot(timesshift[1:-1], plottinganglesshift[1:-1], label = 'OpenPose Shifted')
plt.plot(csvtimesshift[1:-1],csvanglesshift[1:-1],label= 'Werium Shifted')

plt.legend()
plt.axhline(y = 150, color = 'y', linestyle = '--', label = '150º')
plt.axhline(y = 140, color = 'r', linestyle = '-', label = '140º')
plt.axhline(y = 0, color = 'g', linestyle = '-', label = '0º')
plt.xlabel("Seconds")
plt.ylabel("Degrees")


sig1 =[plottinganglesshift[1:-1],timesshift[1:-1]]
sig2 = [csvanglesshift[1:-1],csvtimesshift[1:-1]]

#GUARDAR PARA CALCULAR CROSS-CORRELATION EN R

with open("C:/Users/pmsie/OneDrive/Documentos/Sig1.txt", 'w') as f:
    for i in range (0, len(sig1[0])-1,1):
        f.writelines([str(sig1[0][i]),",",str(sig1[1][i]),"\n"])

    f.close()

with open("C:/Users/pmsie/OneDrive/Documentos/Sig2.txt", 'w') as f:
    for i in range (0, len(sig2[0])-1,1):
        f.writelines([str(sig2[0][i]),",",str(sig2[1][i]),"\n"])

    f.close()


# In[ ]:





# In[ ]:




