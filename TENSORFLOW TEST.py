<<<<<<< HEAD
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 13 20:36:55 2018

@author: YU-TING
"""


import Cross_check
import tensorflow as tf

import numpy as np
import time

#剛接觸Tensorflow時練習如何使用



def create_placeholders(n_x,n_y):
    X = tf.placeholder(tf.float32,shape=[n_x,None])
    Y = tf.placeholder(tf.float32,shape=[n_y,None])
    return X,Y

def initialize_parameters():
    W1 = tf.get_variable('W1',[150,1],initializer=tf.contrib.layers.xavier_initializer(seed=1))
    b1 = tf.get_variable('b1',[150,1],initializer=tf.zeros_initializer())
    W2 = tf.get_variable('W2',[150,150],initializer=tf.contrib.layers.xavier_initializer(seed=1))
    b2 = tf.get_variable('b2',[150,1],initializer=tf.zeros_initializer())
    W3 = tf.get_variable('W3',[1,150],initializer=tf.contrib.layers.xavier_initializer(seed=1))
    b3 = tf.get_variable('b3',[1,1],initializer=tf.zeros_initializer())
    parameters = {"W1": W1,
                  "b1": b1,
                  "W2": W2,
                  "b2": b2,
                  "W3": W3,
                  "b3": b3}
    
    return parameters

def forward_propagation(X, parameters):
    W1 = parameters['W1']
    b1 = parameters['b1']
    W2 = parameters['W2']
    b2 = parameters['b2']
    W3 = parameters['W3']
    b3 = parameters['b3']
    Z1 = tf.add(tf.matmul(W1,X),b1)                                          # Z1 = np.dot(W1, X) + b1
    A1 = tf.nn.relu(Z1)                                              # A1 = relu(Z1)
    Z2 = tf.add(tf.matmul(W2,A1),b2)                                              # Z2 = np.dot(W2, a1) + b2
    A2 = tf.nn.relu(Z2)                                              # A2 = relu(Z2)
    Z3 = tf.add(tf.matmul(W3,A2),b3)  
    A3 = tf.nn.sigmoid(Z3)
    
    return A3

def compute_cost(A3, Y):
    logits = tf.transpose(Z3)
    labels = tf.transpose(Y)
    cost = tf.reduce_mean(tf.squared_difference(logits,labels))
    return cost





X, Y = create_placeholders(1,1)
parameters = initialize_parameters()
Z3 = forward_propagation(X, parameters)
cost = compute_cost(Z3, Y)
optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.01).minimize(cost)
init = tf.global_variables_initializer()
time.clock()
with tf.Session() as sess:
    sess.run(init)
    for i in range(500):
        _ , A_cost = sess.run([optimizer,cost],feed_dict={X:X_train.T,Y:Y_train.T})
        if(i%20==0):
            print(A_cost)
print(time.clock())

    





=======
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 13 20:36:55 2018

@author: YU-TING
"""


import Cross_check
import tensorflow as tf

import numpy as np
import time

#剛接觸Tensorflow時練習如何使用



def create_placeholders(n_x,n_y):
    X = tf.placeholder(tf.float32,shape=[n_x,None])
    Y = tf.placeholder(tf.float32,shape=[n_y,None])
    return X,Y

def initialize_parameters():
    W1 = tf.get_variable('W1',[150,1],initializer=tf.contrib.layers.xavier_initializer(seed=1))
    b1 = tf.get_variable('b1',[150,1],initializer=tf.zeros_initializer())
    W2 = tf.get_variable('W2',[150,150],initializer=tf.contrib.layers.xavier_initializer(seed=1))
    b2 = tf.get_variable('b2',[150,1],initializer=tf.zeros_initializer())
    W3 = tf.get_variable('W3',[1,150],initializer=tf.contrib.layers.xavier_initializer(seed=1))
    b3 = tf.get_variable('b3',[1,1],initializer=tf.zeros_initializer())
    parameters = {"W1": W1,
                  "b1": b1,
                  "W2": W2,
                  "b2": b2,
                  "W3": W3,
                  "b3": b3}
    
    return parameters

def forward_propagation(X, parameters):
    W1 = parameters['W1']
    b1 = parameters['b1']
    W2 = parameters['W2']
    b2 = parameters['b2']
    W3 = parameters['W3']
    b3 = parameters['b3']
    Z1 = tf.add(tf.matmul(W1,X),b1)                                          # Z1 = np.dot(W1, X) + b1
    A1 = tf.nn.relu(Z1)                                              # A1 = relu(Z1)
    Z2 = tf.add(tf.matmul(W2,A1),b2)                                              # Z2 = np.dot(W2, a1) + b2
    A2 = tf.nn.relu(Z2)                                              # A2 = relu(Z2)
    Z3 = tf.add(tf.matmul(W3,A2),b3)  
    A3 = tf.nn.sigmoid(Z3)
    
    return A3

def compute_cost(A3, Y):
    logits = tf.transpose(Z3)
    labels = tf.transpose(Y)
    cost = tf.reduce_mean(tf.squared_difference(logits,labels))
    return cost





X, Y = create_placeholders(1,1)
parameters = initialize_parameters()
Z3 = forward_propagation(X, parameters)
cost = compute_cost(Z3, Y)
optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.01).minimize(cost)
init = tf.global_variables_initializer()
time.clock()
with tf.Session() as sess:
    sess.run(init)
    for i in range(500):
        _ , A_cost = sess.run([optimizer,cost],feed_dict={X:X_train.T,Y:Y_train.T})
        if(i%20==0):
            print(A_cost)
print(time.clock())

    





>>>>>>> ce3f6b55bdf7d737f8b2ec429235f9e221336ff7
