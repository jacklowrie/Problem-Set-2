import os.path
import csv
from operator import xor
from parse import *
import csv

# DOCUMENTATION
# ========================================
# this function outputs predictions for a given data set.
# NOTE this function is provided only for reference.
# You will not be graded on the details of this function, so you can change the interface if 
# you choose, or not complete this function at all if you want to use a different method for
# generating predictions.

def create_predictions(tree, predict):
    '''
    Given a tree and a url to a data_set. Create a csv with a prediction for each result
    using the classify method in node class.
    '''
    
    test_set, attr = parse(predict, True)
    size = len(test_set)
    for i in range(size):      
        value = tree.classify(test_set[i])
        test_set[i][0] = value
    myfile = open('data/results.csv', 'wb')
    for i in range(len(test_set)):
        wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
        wr.writerow(test_set[i])

