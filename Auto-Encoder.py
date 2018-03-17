<<<<<<< HEAD
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 26 11:05:53 2018

@author: YU-TING


"""
import numpy as np
from tensorflow.examples.tutorials.mnist import input_data
import matplotlib.pyplot as plt
#AutoEncoder

class AE:
    def __init__(self,Input_Matrix):
        self.Data=Input_Matrix
        self.examples=Input_Matrix.shape[1]
        self.features=Input_Matrix.shape[0]
        self.condition=[]
        self.Layer=[]
        self.grad={}
        self.cache={}
        self.cache['A0']=Input_Matrix
        self.Tag=None
        self.size=None
        self.L_Layer=Input_Matrix

    def Weights_Set(self,Layer):
        assert Layer[0]==self.features,'第一層對不齊R'
        assert len(Layer)%2==1, '拜託別輸入偶數'
        self.size=Layer
        self.Tag=(len(Layer)-1)//2
        for i in range(len(Layer)-1):     
                 self.grad['W'+str(i+1)]=np.random.randn(Layer[i+1],Layer[i])*0.1
                 self.grad['b'+str(i+1)]=np.zeros([Layer[i+1],1])
                 if(i>=(len(Layer)//2)):
                     self.condition.append('Decoder')
                 else:
                     self.condition.append('Encoder')
                                   

    def Encode_Forward(self):
        self.L_Layer=self.Data
        for i in range(self.Tag):
            self.Linear_forward(self.grad['W'+str(i+1)],self.grad['b'+str(i+1)])
            self.cache['Z'+str(i+1)]=self.L_Layer
            self.Act_forward('sigmoid')
            self.cache['A'+str(i+1)]=self.L_Layer
                       
    def Decode_Forward(self):
        for i in range(self.Tag,2*self.Tag):
            self.Linear_forward(self.grad['W'+str(i+1)],self.grad['b'+str(i+1)])
            self.cache['Z'+str(i+1)]=self.L_Layer
            self.Act_forward('sigmoid')
            self.cache['A'+str(i+1)]=self.L_Layer
                       
    def Sigmoid(self,Input):
        return 1/(1+np.exp(-Input))
    
    def Relu(self,Input):
        Input[Input<0]=0
        return Input   
    
    def Act_forward(self,choose):
        if(choose=='sigmoid'):
            self.L_Layer=self.Sigmoid(self.L_Layer)
        else:
            self.L_Layer=self.Relu(self.L_Layer)
        
    def Linear_forward(self,W,b):
        self.L_Layer=np.dot(W,self.L_Layer)+b    
    
    
    def Linear_backward(self,This_dZ, A_next):
        dW=1./self.examples*np.dot(This_dZ,A_next.T)
        db=1./self.examples*np.sum(This_dZ, axis=1, keepdims=True)
        return dW,db
    
    def Act_backward(self,W_prev,dZ_prev,This_A,choose):
        if(choose=='sigmoid'):
            dA=np.dot(W_prev.T,dZ_prev)
            dZ=dA*(self.Sigmoid(This_A)*(1-self.Sigmoid(This_A)))
            return dZ
    
        else:
            dA=np.dot(W_prev.T,dZ_prev)
            dZ=dA*np.int64(This_A>0)
            return dZ

    def Cost(self):
        C=sum(sum((self.L_Layer-self.Data)**2))/(2*self.examples)
        print(C)

    def dCost(self):
        Beta=self.L_Layer-self.Data
        derivatives=(self.L_Layer*Beta)/self.examples     
        return derivatives

    def Back_propagation(self,training_rate):
        dCost=self.dCost()
        dA=dCost
        dZ=dA*(self.Sigmoid(self.cache['A'+str(len(self.condition))])*(1-self.Sigmoid(self.cache['A'+str(len(self.condition))])))
        
        for i in reversed(range(2*self.Tag)):
            
            dW,db=self.Linear_backward( dZ, self.cache['A'+str(i)])
            self.grad['W'+str(i+1)]=self.grad['W'+str(i+1)]-training_rate*dW
            self.grad['b'+str(i+1)]=self.grad['b'+str(i+1)]-training_rate*db
            dZ=self.Act_backward(self.grad['W'+str(i+1)]  , dZ, self.cache['A'+str(i)], 'sigmoid')          
     
    def Forward(self):
        self.Encode_Forward()
        self.Decode_Forward()
#-----------------------------------------Test Block-----------------------
mnist = input_data.read_data_sets("MNIST_data/", one_hot = True)
x_train = mnist.train.images
y_train = mnist.train.labels
x_test = mnist.test.images
y_test = mnist.test.labels
data=np.reshape(x_train[1,:],[28,28])

plt.imshow(data)





>>>>>>> ce3f6b55bdf7d737f8b2ec429235f9e221336ff7
