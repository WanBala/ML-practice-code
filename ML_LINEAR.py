# -*- coding: utf-8 -*-
"""
Created on Fri Nov 24 13:11:54 2017

@author: YU-TING
"""

import numpy as np
import Cross_check

Data=Cross_check.Valid_get('DATA.xlsx',1,1)
Data[Data>70]=0
Data[Data<-70]=0
    
X=Data[:,0]
Y=Data[:,1]
X=np.reshape(X,[-1,1])
Y=np.reshape(Y,[-1,1])
X_train=X[:800,:]
Y_train=Y[:800,:] 
X_test=X[801:,:]
Y_test=Y[801:,:]



class Polynomial_ML:
    def __init__(self,Input_Matrix,label_y):  #輸入Numpy類型矩陣
        assert type(Input_Matrix)==type(np.zeros([1,1])),'輸入只能是Numpy類矩陣'
        assert type(label_y)==type(np.zeros([1,1])),'y輸入只能是Numpy類矩陣'
        self.examples=Input_Matrix.shape[1]
        self.features=Input_Matrix.shape[0]
        self.weights=None
        self.data=np.row_stack((np.ones([1,self.examples]),Input_Matrix))
        self.y=label_y
        
    def Weights_Set(self):        
        Temp=np.random.randn(self.features,1)*0.01
        self.weights=np.row_stack((np.ones([1,1]),Temp))
        
    def Cost(self):
        print(sum(sum((np.dot(self.data.T,self.weights)-self.y)*(np.dot(self.data.T,self.weights)-self.y)))/(2*self.examples))
    
    def Gradient_Descent(self,training_rate):
        Beta=np.dot(self.data.T,self.weights)-self.y
        derivatives=np.dot(self.data,Beta)/self.examples
        self.weights=self.weights-training_rate*derivatives
        
    def Training(self,training_rate,iterations,show_cost):
        for i in range(1,iterations):
            self.Gradient_Descent(training_rate)
            if(i%show_cost==0):
                self.Cost()               
            
        