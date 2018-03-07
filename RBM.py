# -*- coding: utf-8 -*-
"""
Created on Sun Feb  4 19:05:42 2018

@author: YU-TING
"""

import numpy as np
np_rng = np.random.RandomState(1234)
np.random.seed(1)
class RBM:
    
    def __init__(self,n_input,n_hidden):
        self.n_input=n_input
        self.n_hidden=n_hidden
        self.W=np.random.uniform(-1,1,[n_hidden,n_input])*0.1

        self.b1=np.random.randn(n_input,1)*0.1
        self.b2=np.random.randn(n_hidden,1)*0.1
    
    def sigmoid(self,X):
        return 1/(1+np.exp(-X))
    
    
    def forward(self,X_input):
        forward=np.dot(self.W,X_input)+self.b2
        sigmoid_forward=self.sigmoid(forward)
        return sigmoid_forward
    
    def reconstruct(self,hidden_input):
        back=np.dot(self.W.T,hidden_input)+self.b1
        reconstruct=self.sigmoid(back)
        return reconstruct
    
    def training(self,Data_input,iterations,learning_rate):
        examples=Data_input.shape[1]
        
        for i in range(iterations):
        
            sigmoid_forward=self.forward(Data_input)
            
            hidden_state=sigmoid_forward>np.random.randn(self.n_hidden,examples)
            
            First_associations=np.dot(sigmoid_forward,Data_input.T)
            
            reconstruct=self.reconstruct(hidden_state)
            Reforward=self.forward(reconstruct)
            Second_associations=np.dot(Reforward,reconstruct.T)
            
            dW=(First_associations-Second_associations)/examples
            db1=np.sum((Data_input-reconstruct),axis=1,keepdims=True)/examples
            db2=np.sum((sigmoid_forward-Reforward),axis=1,keepdims=True)/examples
            
            self.W=self.W+learning_rate*dW
            self.b1=self.b1+learning_rate*db1
            self.b2=self.b2+learning_rate*db2
            error = np.sum((Data_input - reconstruct) ** 2)
            print(error)
#------------------------------------------------Test----------------------
X=np.random.uniform(-1,1,[2,8])

            
Model=RBM(6,2)
X = np.array([[1,1,1,0,0,0],[1,0,1,0,0,0],[1,1,1,0,0,0],[0,0,1,1,1,0], [0,0,1,1,0,0],[0,0,1,1,1,0]]).T
Model.training(X,5000,0.01)

    
                