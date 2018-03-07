# -*- coding: utf-8 -*-
"""
Created on Fri Jan 26 21:16:35 2018

@author: YU-TING
"""
import numpy as np
from tensorflow.examples.tutorials.mnist import input_data
import matplotlib.pyplot as plt
#生成對抗網路


class GAN:
    
    def __init__(self):
        self.Data=None
        self.features=None
        self.G_grad={}
        self.G_choose=[]
        self.G_cache={}
        self.G_Layer=None
        self.D_grad={}
        self.D_choose=[]
        self.D_cache={}
        self.D_Layer=None
        self.L_Layer=None
        self.True_cache={}
        self.True_Layer=None

    def G_Weights_Set(self,Layer):
        self.G_Layer=Layer
        for i in range(len(Layer)-1):     
                 self.G_grad['W'+str(i+1)]=np.random.randn(Layer[i+1],Layer[i])*0.01
                 self.G_grad['b'+str(i+1)]=np.zeros([Layer[i+1],1])
                 self.G_choose.append('relu')
        self.G_choose[len(self.G_choose)-1]='sigmoid'        
    
    def D_Weights_Set(self,Layer):
        assert Layer[len(Layer)-1]==1,'輸出機率、最後一層輸出層要是1'
        assert Layer[0]==self.G_Layer[len(self.G_Layer)-1],'G和D是要接起來的 所以G的Ouput必須是D'
        for i in range(len(Layer)-1):     
                 self.D_grad['W'+str(i+1)]=np.random.randn(Layer[i+1],Layer[i])*0.01
                 self.D_grad['b'+str(i+1)]=np.zeros([Layer[i+1],1])
                 self.D_choose.append('relu')
        self.D_choose[len(self.D_choose)-1]='sigmoid'
        
    def Linear_backward(self,This_dZ, A_next,examples):
        dW=(1./examples)*np.dot(This_dZ,A_next.T)
        db=(1./examples)*np.sum(This_dZ, axis=1, keepdims=True)
        return dW,db
    
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
    

    
    def Linear_forward(self,W,b):
        self.L_Layer=np.dot(W,self.L_Layer)+b    
    
    
    
    def G_forward(self,noise_input):
        self.G_cache['A0']=self.L_Layer=noise_input
        for i in range(len(self.G_choose)):
            self.Linear_forward(self.G_grad['W'+str(i+1)],self.G_grad['b'+str(i+1)])
            self.G_cache['Z'+str(i+1)]=self.L_Layer
            self.Act_forward(self.G_choose[i])
            self.G_cache['A'+str(i+1)]=self.L_Layer
            
    def D_forward(self,True_X,set=True):
        if(set==True):
            self.D_cache['A0']=self.L_Layer
            for i in range(len(self.D_choose)):
                self.Linear_forward(self.D_grad['W'+str(i+1)],self.D_grad['b'+str(i+1)])
                self.D_cache['Z'+str(i+1)]=self.L_Layer
                self.Act_forward(self.D_choose[i])
                self.D_cache['A'+str(i+1)]=self.L_Layer
        
        else:
            temp=self.L_Layer
            self.True_cache['A0']=self.L_Layer=True_X            
            for i in range(len(self.D_choose)):
                self.Linear_forward(self.D_grad['W'+str(i+1)],self.D_grad['b'+str(i+1)])
                self.True_cache['Z'+str(i+1)]=self.L_Layer
                self.Act_forward(self.D_choose[i])
                self.True_cache['A'+str(i+1)]=self.L_Layer
            self.L_Layer=temp
 
    def G_loss(self,examples):
        return sum(sum(np.log(1-self.D_cache['A'+str(len(self.D_choose))])))/examples
    
    def D_loss(self,examples):
        indx=len(self.D_choose)
        return -sum(sum(np.log(self.True_cache['A'+str(indx)])+np.log(1-self.D_cache['A'+str(indx)])))/examples
    
    def dG_loss(self,examples):
        return (1/(1-self.D_cache['A'+str(len(self.D_choose))]))/examples
    
    def dD_loss(self,examples):
        index=len(self.D_choose)
        
        return (1/self.True_cache['A'+str(index)]+(1/(1-self.D_cache['A'+str(index)])))/-examples
    
    
    def Sigmoid(self,Input):
        return 1/(1+np.exp(-Input))
    
    def Selu(self,Input):
        a=1.6732632423543772848170429916717
        para=1.0507009873554804934193349852946
        
        B=(Input>0)*Input
        C=B+a*(np.exp(Input))*(Input<=0)-a
        return para*C
    def Act_forward(self,choose):
        if(choose=='sigmoid'):
            self.L_Layer=self.Sigmoid(self.L_Layer)
        elif(choose=='relu'):
            self.L_Layer=self.Relu(self.L_Layer)
        else:
            self.L_Layer=self.Selu(self.L_Layer)
        
            
    def Relu(self,Input):
        
        return Input*(Input>0)   
    
    def D_training(self,noise,True_X,training_rate):
        examples=True_X.shape[1]
        self.G_forward(noise)
        self.D_forward(None)
        self.D_forward(True_X,0)
        dD_loss=self.dD_loss(examples)
        index=len(self.D_choose)
        dZ=dD_loss*(self.Sigmoid(self.D_cache['A'+str(index)])*(1-self.Sigmoid(self.D_cache['A'+str(index)])))
     
        for i in reversed(range(index)):
           
            dW,db=self.Linear_backward( dZ, self.D_cache['A'+str(i)],examples)
            self.D_grad['W'+str(i+1)]=self.D_grad['W'+str(i+1)]-training_rate*dW
            self.D_grad['b'+str(i+1)]=self.D_grad['b'+str(i+1)]-training_rate*db
            dZ=self.Act_backward(self.D_grad['W'+str(i+1)]  , dZ, self.D_cache['A'+str(i)], 'relu') 

    
    def G_training(self,noise,training_rate):
        examples=noise.shape[1]
        dG_loss=self.dG_loss(examples)
        index=len(self.G_choose)
        dZ=dG_loss*np.int64(self.G_cache['A'+str(index)]>0)

        for i in reversed(range(index)):
           
            dW,db=self.Linear_backward( dZ, self.G_cache['A'+str(i)],examples)
            self.G_grad['W'+str(i+1)]=self.G_grad['W'+str(i+1)]-training_rate*dW
            self.G_grad['b'+str(i+1)]=self.G_grad['b'+str(i+1)]-training_rate*db
            dZ=self.Act_backward(self.G_grad['W'+str(i+1)]  , dZ, self.G_cache['A'+str(i)], 'relu') 



    def G_process(self,noise):
        temp=self.L_Layer
        self.L_Layer=noise
        for i in range(len(self.G_choose)):
            self.Linear_forward(self.G_grad['W'+str(i+1)],self.G_grad['b'+str(i+1)])
            
            self.Act_forward(self.G_choose[i])
        output=self.L_Layer
        self.L_Layer=temp
        return output
             
    
    
    
    
    
    
def noise_generate(X_features,numbers):
    a=np.random.uniform(0,1,[X_features,numbers])
    return a

def get_batch(Data,numbers):
    X=Data[np.random.choice(Data.shape[0],numbers,replace=False),:]
    return X
    
#----------------------------------------Test Block-----------------------------------
#noise=noise_generate(2,10)
#Model=GAN()
#True_X=noise_generate(4,10)
#Model.G_Weights_Set([2,8,8,4])
#Model.D_Weights_Set([4,2,2,1])
#Model.D_training(noise,True_X,0.01)
#Model.G_training(noise,0.01)

mnist = input_data.read_data_sets("MNIST_data/", one_hot = True)
x_train = mnist.train.images
y_train = mnist.train.labels
x_test = mnist.test.images
y_test = mnist.test.labels

Model=GAN()
Model.G_Weights_Set([784,1000,1000,1000,784])
Model.D_Weights_Set([784,1000,1000,500,1])
A=np.zeros([784,1])
for i in range(5000):
    True_X=get_batch(x_train,64).T
    noise=noise_generate(784,64)
    for k in range(5):
        Model.D_training(noise,True_X,0.0003)
    print(Model.D_loss(64))
    Model.G_training(noise,0.0003)
    print(Model.G_loss(64))
    print(i)
    
    if(i%100==0):
        F=noise_generate(784,1)
        picture=Model.G_process(F)
        A=np.hstack((A,picture))
        


