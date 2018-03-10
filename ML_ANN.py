<<<<<<< HEAD
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 16 10:52:09 2017

@author: YU-TING
"""
import time

#import multiprocessing
import numpy as np
import copy
from tensorflow.examples.tutorials.mnist import input_data
mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)
x_train = mnist.train.images
y_train = mnist.train.labels
x_test = mnist.test.images
y_test = mnist.test.labels
np.random.seed(1)
class ann:
    def __init__(self,Input_Matrix,label_y):
        self.cache={}
        self.grad={}
        self.choose=[]
        self.examples=Input_Matrix.shape[1]
        self.features=Input_Matrix.shape[0]
        self.y=label_y
        self.data=Input_Matrix
        self.L_Layer=0
        self.cache['A0']=self.data
        self.cost=[]
        self.acc=[]
    def Weights_Set(self,L_layer):
        self.choose=[]
        a=[self.features]
        a=a+L_layer
        for i in range(len(a)-1):
            self.grad["W"+str(i+1)]=np.random.randn(a[i+1],a[i])*np.sqrt(2./a[i])
            self.grad["b"+str(i+1)]=np.ones([a[i+1],1])
            self.choose.append('selu')
        self.choose[len(self.choose)-1]='sigmoid'
        
    def Function_chooce(self,L_choose,function):
        for i in L_choose:
            self.choose[i-1]=function
            
    def Sigmoid(self,Input):
        return 1/(1+np.exp(-Input))
    
    def Relu(self,Input):
        Input[Input<0]=0
        return Input   
               
    def Linear_forward(self,W,b):
        self.L_Layer=np.dot(W,self.L_Layer)+b    
            
    def Act_forward(self,choose):
        if(choose=='sigmoid'):
            self.L_Layer=self.Sigmoid(self.L_Layer)
        elif(choose=='selu'):
            self.L_Layer=self.Selu(self.L_Layer)
        
        
        else:
            self.L_Layer=self.Relu(self.L_Layer)
    
    def Selu(self,Input):
        a=1.6732632423543772848170429916717
        para=1.0507009873554804934193349852946
        
        B=(Input>0)*Input
        C=B+a*(np.exp(Input))*(Input<=0)-a
        return para*C

    def Forward_propagation(self):
        self.L_Layer=self.data
        for i in range(len(self.choose)):
            self.Linear_forward(self.grad['W'+str(i+1)],self.grad['b'+str(i+1)])
            self.cache['Z'+str(i+1)]=self.L_Layer
            self.Act_forward(self.choose[i])
            self.cache['A'+str(i+1)]=self.L_Layer
                       
    def Cost(self):
        return sum(sum( (-self.y*np.log(self.L_Layer)-(1-self.y)*np.log(1-self.L_Layer))))/self.examples
    
    
    def Act_backward(self,W_prev,dZ_prev,This_A,choose):
        if(choose=='sigmoid'):
            dA=np.dot(W_prev.T,dZ_prev)
            dZ=dA*(self.Sigmoid(This_A)*(1-self.Sigmoid(This_A)))
            return dZ
    
        elif(choose=='selu'):
            dA=np.dot(W_prev.T,dZ_prev)
            a=1.6732632423543772848170429916717
            para=1.0507009873554804934193349852946
       
            B=This_A>0
            C=B+a*(np.exp(This_A))*(This_A<=0)
            d=C*para
            dZ=dA*d
            return dZ
        
        else:
            dA=np.dot(W_prev.T,dZ_prev)
            dZ=dA*np.int64(This_A>0)
            return dZ    
   
    def Linear_backward(self,This_dZ, A_next):
        dW=1./self.examples*np.dot(This_dZ,A_next.T)
        db=1./self.examples*np.sum(This_dZ, axis=1, keepdims=True)
        return dW,db
    
    def Back_propagation(self,training_rate):
        dZ=self.cache['A'+str(len(self.choose))]-self.y
        for i in reversed(range(len(self.choose))):
            
            dW,db=self.Linear_backward( dZ, self.cache['A'+str(i)])
            self.grad['W'+str(i+1)]=self.grad['W'+str(i+1)]-training_rate*dW
            self.grad['b'+str(i+1)]=self.grad['b'+str(i+1)]-training_rate*db
            dZ=self.Act_backward(self.grad['W'+str(i+1)]  , dZ, self.cache['A'+str(i)],'selu')          
            
           
            
                 
    def training(self,iter_numbers,training_rate,show=False):
        for i in range(iter_numbers):
            self.Forward_propagation()
            self.Back_propagation(training_rate)
            self.cost.append(self.Cost())
            if(i%show==0):
                print(self.Cost())
                self.acc.append(self.test(x_test.T,y_test.T))
                
    
    def test(self,X_test,Y_test):
        self.L_Layer=X_test
        for i in range(len(self.choose)):
            self.Linear_forward(self.grad['W'+str(i+1)],self.grad['b'+str(i+1)])
            self.cache['Z'+str(i+1)]=self.L_Layer
            self.Act_forward(self.choose[i])
            self.cache['A'+str(i+1)]=self.L_Layer          
        Y_answer=Y_test.argmax(0)
        X_answer=self.L_Layer.argmax(0)
        
        ANSWER=X_answer==Y_answer
        ANSWER=np.sum(np.sum(ANSWER))
        print(ANSWER/10000)
        return ANSWER/10000
ML=ann(x_train.T,y_train.T)
ML.Weights_Set([50,50,50,50,10])
time.clock()

ML.training(1000,0.1,20)
time1=time.clock()
ML.test(x_test.T,y_test.T)
selu_cost=copy.deepcopy(np.asarray(ML.cost))
selu_acc=copy.deepcopy(np.asarray(ML.acc))


>>>>>>> ce3f6b55bdf7d737f8b2ec429235f9e221336ff7
