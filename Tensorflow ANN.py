# -*- coding: utf-8 -*-
"""
Created on Mon Jan 15 13:37:46 2018

@author: YU-TING
"""

import tensorflow as tf

def create_placeholder(input_feature,output_feature):
    X=tf.placeholder(tf.float32,shape=[input_feature,None])
    Y=tf.placeholder(tf.float32,shape=[output_feature,None])
    return X,Y

def initialize_parameters(Learning_size,input_feature):
    size=[input_feature]
    size.extend(Learning_size)
    parameters={}
    with tf.variable_scope("Variable") as scope:
        scope.reuse_variables()
        for i in range(len(size)-1):
            parameters['W'+str(i+1)]=tf.get_variable('W'+str(i+1),
                      [size[i+1],size[i]],initializer=tf.contrib.layers.xavier_initializer())
            parameters['b'+str(i+1)]=tf.get_variable('b'+str(i+1),
                      [size[i+1],1],initializer=tf.contrib.layers.xavier_initializer())
        
    return parameters

def Forward_propagation(input_Matrix,parameters):
    Z=tf.add(tf.matmul(parameters['W1'],input_Matrix),parameters['b1'])
    for i in range(len(parameters)//2-1):
        Z=tf.nn.relu(Z)
        Z=tf.add(tf.matmul(parameters['W'+str(i+2)],Z),parameters['b'+str(i+2)])
    
    return Z

def compute_cost(Z,Y):
    label_Y=tf.transpose(Y)
    predict=tf.transpose(Z)
    Cost=tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits=predict,labels=label_Y))
    return Cost

def ANN_training(input_Matrix, output_Matrix, Learning_size, iterations, training_rate):
    X,Y=create_placeholder(input_Matrix.shape[0],output_Matrix.shape[0])
    parameters=initialize_parameters(Learning_size,input_Matrix.shape[0])
    Z=Forward_propagation(input_Matrix,parameters)
    Cost=compute_cost(Z,output_Matrix)
    optimizer=tf.train.GradientDescentOptimizer(learning_rate= training_rate).minimize(Cost)
    init = tf.global_variables_initializer()
    with tf.Session() as sess:
        sess.run(init)
        for i in range(iterations):
            _, A_cost=sess.run([optimizer,Cost],feed_dict={X:input_Matrix,Y:output_Matrix})
            if(i%10==0):
                print(A_cost)
    
from tensorflow.examples.tutorials.mnist import input_data
mnist = input_data.read_data_sets("MNIST_data/", one_hot = True)
x_train = mnist.train.images
y_train = mnist.train.labels
x_test = mnist.test.images
y_test = mnist.test.labels

ANN_training(x_train.T,y_train.T,[50,50,10],200,0.1) #第三參數是以list形式傳入各層神經元數，第四參數為迭帶次數，第五參數為學習速率
        
    
