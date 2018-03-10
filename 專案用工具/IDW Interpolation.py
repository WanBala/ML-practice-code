# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 12:52:41 2018

@author: YU-TING

我們團隊在進行地下水位分析的時候，有些資料是破損不完整的，如降雨量紀錄資料
在本程式中將不完整的值設定為0
所有程式過程都被我封裝起來
只需要呼叫Idw_Interpolation(Numpy Array,相關係數)就會將0的值提出來進行插值計算

此為反距離插值法

"""


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
import copy
xls_file=pd.ExcelFile('C:\\Users\\YU-TING\\Desktop\\研究\\NEWDATAA.xlsx')
A=xls_file.parse('Sheet')
A_array=np.array(A)


xls_file=pd.ExcelFile('C:\\Users\\YU-TING\\Desktop\\研究\\DATA.xlsx')
B=xls_file.parse('工作表1')
B_array=np.array(B)

X_axis1=np.linspace(0,3653,3653)
X_axis2=np.linspace(0,3531,3531)

del A,B,xls_file



def __Find_losing_point(array_input):
    total=array_input.shape[0]
    point_index=[]
    
    for i in range(total):
        if(array_input[i]==0):
            point_index.append(i)
    
    return point_index

def __Computing_Distance(point_index,array_input):
    distance=[]
    total=array_input.shape[0]

    for i in point_index:
        point_distance=[]
        for j in range(total):
            
            if(j in point_index):
                point_distance.append(0)    
                
            else:
                point_distance.append(abs(i-j))
        distance.append(point_distance)
        
    return distance

def __Computing_Value(point_index,array_input,distance,exp=2):
    distance=np.array(distance,dtype='float64')
    mask=distance==0
    mx=np.ma.masked_array(distance,mask=mask)
    inv_distance=np.power(1/mx,exp)
    inv_distance=inv_distance.data-inv_distance.mask
    total=np.sum(inv_distance,axis=1,keepdims=True)
    W=inv_distance/total
    Value=W.T*array_input
    Value=np.sum(Value,axis=0,keepdims=True)
    return Value

def __Value_Interpolation(Value,point_index,array_input):
    point_index=np.array(point_index)
    Value=Value.T
    number=0
    COPY=copy.deepcopy(array_input)
    for i in point_index:
        COPY[i,0]=copy.deepcopy(Value[number,0])
        number+=1
    return COPY

def Idw_Interpolation(A_array_input,exp=2):
    point_index=__Find_losing_point(A_array)
    distance=__Computing_Distance(point_index,A_array)
    Value=__Computing_Value(point_index,A_array,distance,exp)
    data=__Value_Interpolation(Value,point_index,A_array)
    return data

#-----------------------------------------------------------------
#data=Idw_Interpolation(A_array,2.8)

#plt.scatter(X_axis1,data)
