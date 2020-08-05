#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 20:21:26 2018

@author: yi-chun
"""


import random
import numpy as np
import math

#comparison of three number
l=3
X=np.array([1, 10, 20])
x=X/sum(X)
T=10000 # times of learning

rate_0=random.random()#initialize learning rate
rate=rate_0
#initialize weight
w=np.zeros(l)


for i in range(0,l,1):
    w[i]=random.random()
    
w=w/sum(w)


# First Input
t=0
exit_flag=False
j=0
#random.randrange(0,l,1)
while t < T and exit_flag==False:
    distance=np.array([abs(x[j]-w[0]),abs(x[j]-w[1]),abs(x[j]-w[2])])
    # x(t_i)-w_j

    minDIS=min(distance) #x(t_i)-w_g

    g=np.argmin(distance)

    Ng=np.array([max(1,g-1),g,min(l,g+1)])

    deltaW=np.zeros(l)


    for i in range(l):
        if i==Ng[0] or i==Ng[1] or i==Ng[2]:
            deltaW=rate*distance
        else:
            deltaW=0
            w=w+deltaW # update weight
            w=w/sum(w) # normalization









    ##########################################
    #   Second Input
    j=1


    distance=np.array([abs(x[j]-w[0]),abs(x[j]-w[1]),abs(x[j]-w[2])])
    # x(t_i)-w_j

    minDIS=min(distance) #x(t_i)-w_g

    g=np.argmin(distance)

    Ng=np.array([max(1,g-1),g,min(l,g+1)])

    deltaW=np.zeros(l)


    for i in range(l):
        if i==Ng[0] or i==Ng[1] or i==Ng[2]:
            deltaW=rate*distance
        else:
            deltaW=0
            w=w+deltaW # update weight
            w=w/sum(w) # normalization



    ##########################################


    j=2


    distance=np.array([abs(x[j]-w[0]),abs(x[j]-w[1]),abs(x[j]-w[2])])
    # x(t_i)-w_j

    minDIS=min(distance) #x(t_i)-w_g

    g=np.argmin(distance)

    Ng=np.array([max(1,g-1),g,min(l,g+1)])

    deltaW=np.zeros(l)


    for i in range(l):
        if i==Ng[0] or i==Ng[1] or i==Ng[2]:
            deltaW=rate*distance
        else:
            deltaW=0
            w=w+deltaW # update weight
            w=w/sum(w) # normalization
            
    rate=rate*(1-t/T)
    D=0
    for d in range(1,l):
        DD=abs(w[d]-w[d-1])-abs(w[l-1]-w[0])
        D=D+DD
    if D==0:
        exit_flag=True # sorting weight
    t=t+1
   
print(w)

j=0
distance1=np.array([abs(x[j]-w[0]),abs(x[j]-w[1]),abs(x[j]-w[2])])
y1=np.argmax(distance1)

j=1
distance2=np.array([abs(x[j]-w[0]),abs(x[j]-w[1]),abs(x[j]-w[2])])
y2=np.argmax(distance2)

j=2
distance3=np.array([abs(x[j]-w[0]),abs(x[j]-w[1]),abs(x[j]-w[2])])
y3=np.argmax(distance3) 



print("三個實數y1,y2,y3的大小順序為：",y1,y2,y3)






