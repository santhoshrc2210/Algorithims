'''Prints cord of different functiions'''
#run in codeskulptor

import simpleplot
import math

dataseta=[]
datasetb=[]
datasetc=[]
datasetd=[]
datasete=[]
for i in range(100):
    cord=[]
    y_a=2**2**i
    cord.append(i)
    cord.append(y_a)
    dataseta.append(cord)
    
    cordb=[]
    y_b=2**i**2
    cordb.append(i)
    cordb.append(y_b)
    datasetb.append(cordb)
    
    cordc=[]
    y_c=(i**2)*(math.log(i,2))
    cordc.append(i)
    cordc.append(y_c)
    datasetc.append(cordc)
    
    cordd=[]
    y_d=i
    cordd.append(i)
    cordd.append(y_d)
    datasetd.append(cordd)
    
    corde=[]
    y_e=i**2**i
    corde.append(i)
    corde.append(y_e)
    datasete.append(corde)
    
    print cord,cordb,cordc,cordd,corde
    

