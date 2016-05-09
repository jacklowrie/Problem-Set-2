from node import Node
from ID3 import *
from operator import xor

# Note, these functions are provided for your reference.  You will not be graded on their behavior,
# so you can implement them as you choose or not implement them at all if you want to use a different
# architecture for pruning.

def reduced_error_pruning(root,training_set,validation_set):
    '''
    take the a node, training set, and validation set and returns the improved node.
    You can implement this as you choose, but the goal is to remove some nodes such that doing so improves validation accuracy.
    '''
    # Your code here
    return prune(root, validation_set, 0)

    
def prune(root, validation_subset, depth):
    if root.label != None: #leaf
        pass
    elif int(depth * random()) >= 2: 
        root.label = mode(validation_subset)
        root.children = None
    elif root.is_nominal: #Nominal
        i = 1
        temp = split_on_nominal(validation_subset, root.decision_attribute)
        
        for child in root.children:
            validation_subset = temp[i]
            pruning(root.children[child], validation_subset, depth + 1)
            i += 1
            
    else: #Numeric
        temp = split_on_numerical(validation_subset, root.decision_attribute, root.splitting_value)
        
        validation_subset = temp[0] 
        pruning(root.children[0], validation_subset, depth + 1)
        
        validation_subset = temp[1]
        pruning(root.children[1], validation_subset, depth + 1)
            
    return root
# 


def validation_accuracy(tree,validation_set):
    '''
    takes a tree and a validation set and returns the accuracy of the set on the given tree
    '''
    # Your code here
    correct = [1 if tree.classify(x) == x[0] else 0 for x in validation_set]
    total_correct = sum(correct, 0)
    total = len(correct)

    return float(total_correct) / total

        
