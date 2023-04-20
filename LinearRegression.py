# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def LinearRegression(data1, data2):

    X= data1
    
    Y= data2
    
    y= sum(Y)
    x= sum(X)
    q=0
    for i in range(len(X)):
        q+=X[i]**2
    x2=q
    r=0
    for i in range(len(X)):
        r+= X[i]*Y[i]
    xy= r
    
    a= ((y*x2)-(x*xy))/((len(X)*x2)-(x)**2)
    b= ((len(X)*xy)- (x*y))/((len(X)*x2)-(x)**2)
    y_pred= []
    for i in range(len(X)):
        c= a+ b*X[i]
        y_pred.append(c)
    
    
    plt.scatter(X,Y)
    plt.plot(X,y_pred)
    plt.show()
    
    print("Intercept:", a)
    print("Slope:", b)



    
    
    
    