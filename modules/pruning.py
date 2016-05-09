from node import Node
from ID3 import *
from operator import xor

# Note, these functions are provided for your reference.  You will not be graded on their behavior,
# so you can implement them as you choose or not implement them at all if you want to use a different
# architecture for pruning.

def reduced_error_pruning(root,training_set,validation_set, depth, parent):
    '''
    take the a node, training set, and validation set and returns the improved node.
    You can implement this as you choose, but the goal is to remove some nodes such that doing so improves validation accuracy.
    '''

    if root.label != None or validation_set == []: 
        return root 

    
    new_node = Node()
    new_node.label = mode(validation_set)
    if validation_accuracy(new_node, validation_set)>= validation_accuracy(root, validation_set):
        index = parent.children.index(root)
        parent.children[index] = new_node
        return parent
    if root.is_nominal: 
        splits = split_on_nominal(validation_subset, root.decision_attribute)
    
        for i in range(len(root.children)):
            
            if root.decision_attribute == i:
                reduced_error_pruning(root.children[i], splits[i], depth + 1, root)
            
    else: 
        splits = split_on_numerical(validation_set, root.decision_attribute, root.splitting_value)
        
        reduced_error_pruning(root.children[0],training_set, splits[0], depth + 1,root)
        
        reduced_error_pruning(root.children[1],training_set, splits[1], depth + 1,root)
            
    return root
# 


def validation_accuracy(tree,validation_set):
    '''
    takes a tree and a validation set and returns the accuracy of the set on the given tree
    '''
    if validation_set!=[]:
        correct = [1 if tree.classify(x) == x[0] else 0 for x in validation_set]
        total_correct = sum(correct, 0)
        total = len(correct)
    
        return float(total_correct) / total
    return 0

        
