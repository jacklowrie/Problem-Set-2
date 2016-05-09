import random
from ID3 import *
from operator import xor
from parse import parse
import matplotlib.pyplot as plt
import os.path
from pruning import validation_accuracy
import math

# NOTE: these functions are just for your reference, you will NOT be graded on their output
# so you can feel free to implement them as you choose, or not implement them at all if you want
# to use an entirely different method for graphing

def get_graph_accuracy_partial(train_set, attribute_metadata, validate_set, numerical_splits_count, depth, pct):
    '''
    get_graph_accuracy_partial - Given a training set, attribute metadata, validation
    set, numerical splits count, and percentage, this function will return the validation 
    accuracy of a specified (percentage) portion of the training setself.
    '''
    #make the subset
    train_subset_size = int(math.floor(pct*len(train_set)))
    train_subset = random.sample(train_set, train_subset_size)
    random.shuffle(train_subset)

    #make the tree, determine accuracy
    tree = ID3(train_subset, attribute_metadata, numerical_splits_count, depth)
    accuracy = validation_accuracy(tree, validate_set)   
    print accuracy

    return accuracy

def get_graph_data(train_set, attribute_metadata, validate_set, numerical_splits_count, depth, iterations, pcts):
    '''
    Given a training set, attribute metadata, validation set, numerical splits count, 
    iterations, and percentages, this function will return an array of the averaged graph
    accuracy partials based off the number of iterations.
    '''
    data_points = []

    for pct in pcts:
    	#run get_graph_accuracy_partial() over iterations
    	iterated_accuracy = []
    	for x in range(iterations):
    		iterated_accuracy.append(get_graph_accuracy_partial(train_set, attribute_metadata, validate_set, numerical_splits_count, depth, pct))
    	
    	#average the results and add to final array
    	avg_accuracy = sum(iterated_accuracy)/len(iterated_accuracy)
    	data_points.append(avg_accuracy)


    print data_points
    return data_points

# get_graph will plot the points of the results from get_graph_data and return a graph
def get_graph(train_set, attribute_metadata, validate_set, numerical_splits_count, depth, iterations, lower, upper, increment):
    '''
    get_graph - Given a training set, attribute metadata, validation set, numerical 
    splits count, depth, iterations, lower(range), upper(range), and increment, this 
    function will graph the results from get_graph_data in reference to the drange 
    percentages of the data.
    '''
    return get_graph_data(train_set, attribute_metadata, validate_set, numerical_splits_count, depth, iterations, [0.1, 0.2, 0.3, 0.4, 0.5])
    # #set up percentages
    # pcts = []
    # x = lower
    # while x <= upper:
    # 	pcts.append(x)
    # 	x += increment
    # print pcts

    # #get plotting points
    # data = get_graph_data(train_set, attribute_metadata, validate_set, numerical_splits_count, depth, iterations, pcts)
    
    # #set up the graph
    # plt.plot(pcts, data)
    # plt.ylabel('accuracy')
    # plt.xlabel('training subset size')
    # plt.show()



    