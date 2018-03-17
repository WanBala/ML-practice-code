# -*- coding: utf-8 -*-
"""
Created on Tue Mar 13 10:37:11 2018

@author: YU-TING

"""
import tensorflow as tf
import numpy as np
from tensorflow.examples.tutorials.mnist import input_data
mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)
x_train = mnist.train.images
y_train = mnist.train.labels
x_test = mnist.test.images
y_test = mnist.test.labels

def Placeholder(n_input,n_out):
    X=tf.placeholder(tf.float32,[n_input,None])
    Y=tf.placeholder(tf.float32,[n_out,None])
    return X,Y

def Input_Reshape(X,shape1,shape2,shape3):
    X1=tf.reshape(X,[-1,shape1,shape2,shape3])
    return X1

def Weights_Generator(Size):
    Filter=tf.Variable(tf.random_normal(Size))
    return Filter


def Conv2d(Input,flr,strides):  
    operate=tf.nn.conv2d(Input,flr,strides=strides,padding='SAME')
    return operate

def Max_Pooling(Input,ksize,strides):
    return tf.nn.max_pool(Input,ksize=ksize,strides=strides,padding='SAME')





X,Y=Placeholder(784,10)
droprate=tf.placeholder(tf.float32)
X1=Input_Reshape(X,28,28,1)

Kernal1=Weights_Generator([5,5,1,32])
Kernal1_Bias=Weights_Generator([32])

h_conv=tf.nn.relu(Conv2d(X1,Kernal1,[1,1,1,1])+Kernal1_Bias)
h_pool=Max_Pooling(h_conv,[1,2,2,1],[1,2,2,1])

Kernal2=Weights_Generator([5,5,32,64])
Kernal2_Bias=Weights_Generator([64])

h_conv2=tf.nn.relu(Conv2d(h_pool,Kernal2,[1,1,1,1])+Kernal2_Bias)
h_pool2=Max_Pooling(h_conv2,[1,2,2,1],[1,2,2,1])

h_pool2_flat=tf.reshape(h_pool2,[7*7*64,-1])

W_fc1=Weights_Generator([1024,7*7*64])
b_fc1=Weights_Generator([1024,1])
h_fc1=tf.nn.relu(tf.matmul(W_fc1,h_pool2_flat)+b_fc1)
h_fc_drop=tf.nn.dropout(h_fc1,droprate)


W_fc2=Weights_Generator([10,1024])
b_fc2=Weights_Generator([10,1])
Out=tf.matmul(W_fc2,h_fc_drop)+b_fc2
A=tf.transpose(Out)



True_labels=tf.transpose(Y)
cost=tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits=A,labels=True_labels))

training=tf.train.AdamOptimizer(0.1).minimize(cost)

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    for i in range(1000):
        batch_x, batch_y = mnist.train.next_batch(1000)
        _,A_cost=sess.run([training,cost],feed_dict={X:batch_x.T,Y:batch_y.T,droprate:0.5})
        if(i%20==0):
            print(A_cost)