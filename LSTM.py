<<<<<<< HEAD
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 27 18:48:17 2018

@author: YU-TING
"""

#LSTM RNN    這個版本只是測試版
import tensorflow as tf
import numpy as np



def create_placeholders(n_x,n_y):
    X = tf.placeholder(tf.float32,shape=[n_x,None])
    Y = tf.placeholder(tf.float32,shape=[n_y,None])
    return X,Y


def initialize_parameters():
    Wf=tf.get_variable('Wf',[1,1],initializer=tf.contrib.layers.xavier_initializer(seed=1))
    bf=tf.get_variable('bf',[1,1],initializer=tf.zeros_initializer())
    Wi=tf.get_variable('Wi',[1,1],initializer=tf.contrib.layers.xavier_initializer(seed=1))
    bi=tf.get_variable('bi',[1,1],initializer=tf.zeros_initializer())
    Wc=tf.get_variable('Wc',[1,1],initializer=tf.contrib.layers.xavier_initializer(seed=1))
    bc=tf.get_variable('bc',[1,1],initializer=tf.zeros_initializer())
    Wo=tf.get_variable('Wo',[1,1],initializer=tf.contrib.layers.xavier_initializer(seed=1))
    bo=tf.get_variable('bo',[1,1],initializer=tf.zeros_initializer())
    ht= tf.get_variable('h1',[1,1],initializer=tf.zeros_initializer())
    Ct= tf.get_variable('c1',[1,1],initializer=tf.zeros_initializer())
    return Wf,bf,Wi,bi,Wc,bc,Wo,bo,ht,Ct




def cell_compute(X,h_pre,C_pre,Wf,bf,Wi,bi,Wc,bc):          #計算記憶條以及三個狀態
    ft=tf.matmul(Wf,h_pre)+tf.matmul(Wf,X)+bf                   #分類時sigmoid
    it=tf.matmul(Wi,h_pre)+tf.matmul(Wi,X)+bi                 #sigmoid
    Ct2=tf.matmul(Wc,h_pre)+tf.matmul(Wc,X)+bc                   #tanh
    Ct=tf.multiply(ft,C_pre)+tf.multiply(it,Ct2)
    
    return Ct

def h_State_compute(X,h_pre,Wo,bo,Ct):
    ot=tf.matmul(Wo,h_pre)+tf.matmul(Wo,X)+bo
    ht=tf.multiply(ot,Ct)                                      #分類時Ct tanh
    
        
    return ht



def compute_cost(A3, Y):
    logits = tf.transpose(A3)
    labels = tf.transpose(Y)
    cost = tf.reduce_mean(tf.squared_difference(logits,labels))
    return cost


X,Y=create_placeholders(1,1)
Wf,bf,Wi,bi,Wc,bc,Wo,bo,ht,Ct=initialize_parameters()

Ct=cell_compute(X,ht,Ct,Wf,bf,Wi,bi,Wc,bc)
ht=h_State_compute(X,ht,Wo,bo,Ct)
cost = compute_cost(ht,Y)
optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.01).minimize(cost)


init = tf.global_variables_initializer()
R=np.reshape(np.array([0,0,0,0,1,0,0,0,1,0,0,0,1,0]),[1,14])
T=np.reshape(np.array([1,2,3,4,5,7,8,9,10,11,12,13,14,16]),[1,14])
with tf.Session() as sess:
    sess.run(init)
    for j in range(500):
        _ , A_cost = sess.run([optimizer,cost],feed_dict={X:R,Y:T})
        
        print(A_cost)







=======
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 27 18:48:17 2018

@author: YU-TING
"""

#LSTM RNN    這個版本只是測試版
import tensorflow as tf
import numpy as np



def create_placeholders(n_x,n_y):
    X = tf.placeholder(tf.float32,shape=[n_x,None])
    Y = tf.placeholder(tf.float32,shape=[n_y,None])
    return X,Y


def initialize_parameters():
    Wf=tf.get_variable('Wf',[1,1],initializer=tf.contrib.layers.xavier_initializer(seed=1))
    bf=tf.get_variable('bf',[1,1],initializer=tf.zeros_initializer())
    Wi=tf.get_variable('Wi',[1,1],initializer=tf.contrib.layers.xavier_initializer(seed=1))
    bi=tf.get_variable('bi',[1,1],initializer=tf.zeros_initializer())
    Wc=tf.get_variable('Wc',[1,1],initializer=tf.contrib.layers.xavier_initializer(seed=1))
    bc=tf.get_variable('bc',[1,1],initializer=tf.zeros_initializer())
    Wo=tf.get_variable('Wo',[1,1],initializer=tf.contrib.layers.xavier_initializer(seed=1))
    bo=tf.get_variable('bo',[1,1],initializer=tf.zeros_initializer())
    ht= tf.get_variable('h1',[1,1],initializer=tf.zeros_initializer())
    Ct= tf.get_variable('c1',[1,1],initializer=tf.zeros_initializer())
    return Wf,bf,Wi,bi,Wc,bc,Wo,bo,ht,Ct




def cell_compute(X,h_pre,C_pre,Wf,bf,Wi,bi,Wc,bc):          #計算記憶條以及三個狀態
    ft=tf.matmul(Wf,h_pre)+tf.matmul(Wf,X)+bf                   #分類時sigmoid
    it=tf.matmul(Wi,h_pre)+tf.matmul(Wi,X)+bi                 #sigmoid
    Ct2=tf.matmul(Wc,h_pre)+tf.matmul(Wc,X)+bc                   #tanh
    Ct=tf.multiply(ft,C_pre)+tf.multiply(it,Ct2)
    
    return Ct

def h_State_compute(X,h_pre,Wo,bo,Ct):
    ot=tf.matmul(Wo,h_pre)+tf.matmul(Wo,X)+bo
    ht=tf.multiply(ot,Ct)                                      #分類時Ct tanh
    
        
    return ht



def compute_cost(A3, Y):
    logits = tf.transpose(A3)
    labels = tf.transpose(Y)
    cost = tf.reduce_mean(tf.squared_difference(logits,labels))
    return cost


X,Y=create_placeholders(1,1)
Wf,bf,Wi,bi,Wc,bc,Wo,bo,ht,Ct=initialize_parameters()

Ct=cell_compute(X,ht,Ct,Wf,bf,Wi,bi,Wc,bc)
ht=h_State_compute(X,ht,Wo,bo,Ct)
cost = compute_cost(ht,Y)
optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.01).minimize(cost)


init = tf.global_variables_initializer()
R=np.reshape(np.array([0,0,0,0,1,0,0,0,1,0,0,0,1,0]),[1,14])
T=np.reshape(np.array([1,2,3,4,5,7,8,9,10,11,12,13,14,16]),[1,14])
with tf.Session() as sess:
    sess.run(init)
    for j in range(500):
        _ , A_cost = sess.run([optimizer,cost],feed_dict={X:R,Y:T})
        
        print(A_cost)







>>>>>>> ce3f6b55bdf7d737f8b2ec429235f9e221336ff7
