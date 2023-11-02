import numpy as np
import random
from pprint import pprint

def read_data(path) : 
    f = open(path, "r")
    data_set = []
    tmp = []
    label = []
    raw_text = f.read()
    raw_text = raw_text.split()
    random.shuffle(raw_text)
    for line in raw_text :   
        aux = line.strip().split(',') 
        tmp.append([float(x) for x in aux[:-1]])
        label.append(aux[-1])
    f.close()
    data_set.append(tmp)
    data_set.append(label)
    return data_set

def split_data(data_set) :
    learning_set = []
    test_set = []
    learning_atributes = []
    learning_labels = []
    test_atributes = []
    test_labels = []
    for i in range(len(data_set[0])) :
        if i < 120 :
            learning_atributes.append(data_set[0][i])
            learning_labels.append(data_set[1][i])
        else :
            test_atributes.append(data_set[0][i])
            test_labels.append(data_set[1][i])
        learning_set.append(learning_atributes)
        learning_set.append(learning_labels)
        test_set.append(test_atributes)
        test_set.append(test_labels)
    return learning_set, test_set

def sigmoid(x) :
    y = 1 / (1 + np.exp(-x))
    return y

def sigmoid_derivative(x) :
    return x * (1 - x)

def error__(x, y):
    return (np.square(x - y)) / 2

def forward_propagation(X, Y, dict2) :
    dict = {}
    w12 = dict2["w12"]
    b1 = dict2["b1"]
    w23 = dict2["w23"]
    b2 = dict2["b2"]
    X = np.asarray(X)
    X = X.reshape(4,1)
    net1 = np.dot(w12, X) + b1
    a1 = sigmoid(net1)  #ascuns
    net2 = np.dot(w23, a1) + b2
    a2 = sigmoid(net2)  #output
    error = 1/2 * np.sum(Y - a2)**2
    dict["a1"] = a1
    dict["a2"] = a2
    dict["error"] = error
    dict["net1"] = net1
    dict["net2"] = net2
    return dict


data = read_data("iris.data")
learningSet, testSet = split_data(data)

weights = {}
weights["w12"] = np.random.uniform(-0.2, 0.2, (4, 4))
weights["b1"] = np.ones((4, 1))
weights["w23"] = np.random.uniform(-0.2, 0.2, (3, 4))
weights["b2"] = np.ones((3, 1))
learn_rate = 0.1

pprint(forward_propagation(learningSet[0][0], 0, weights))