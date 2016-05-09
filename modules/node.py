# DOCUMENTATION
# =====================================
# Class node attributes:
# ----------------------------
# children - a list of 2 if numeric and a dictionary if nominal.  
#            For numeric, the 0 index holds examples < the splitting_value, the 
#            index holds examples >= the splitting value
#
# label - is None if there is a decision attribute, and is the output label (0 or 1 for
#	the homework data set) if there are no other attributes
#       to split on or the data is homogenous
#
# decision_attribute - the index of the decision attribute being split on
#
# is_nominal - is the decision attribute nominal
#
# value - Ignore (not used, output class if any goes in label)
#
# splitting_value - if numeric, where to split
#
# name - name of the attribute being split on

printed = ''

class Node:
    def __init__(self):
        # initialize all attributes
        self.label = None
        self.decision_attribute = None
        self.is_nominal = None
        self.value = None
        self.splitting_value = None
        self.children = {}
        self.name = None

    def classify(self, instance):
        '''
        given a single observation, will return the output of the tree
        '''
        if(self.label != None):
            return self.label
        elif(self.is_nominal):
            classifier = self.children[instance[self.decision_attribute]]
            return classifier.classify(instance)
        elif(instance[self.decision_attribute]>=self.splitting_value):
            classifier = self.children[1]
            return classifier.classify(instance)
        else:
            classifier = self.children[0]
            return classifier.classify(instance)
         

    def print_tree(self, indent = 0):
        '''
        returns a string of the entire tree in human readable form
        '''
        queue = []
        bfs_str ='';
        queue.append(self)
        while len(queue):
            popped = queue.pop(0)
            bfs_str += (str(popped.splitting_value) + ' ');
            if popped.children is not None:
                for key in popped.children:
                    queue.append(popped.children[key])
        return bfs_str[:-1];


    def print_dnf_tree(self):
        '''
        returns the disjunct normalized form of the tree.
        '''
        return self.dnft('')
    def dnft(self, hidden):
        return 'dnft not implemented'


#test tree for printing (from writeup)

# A = Node()
# A.name = 'A'
# A.is_nominal = False
# A.splitting_value = 1
# 
# Aa = Node()
# Aa.label = 1
# Aa.name = 'Aa'
# A.children.append(Aa)
# 
# B = Node()
# B.name = 'B'
# B.is_nominal = False
# B.splitting_value = 1
# A.children.append(B)
# 
# Ba = Node()
# Ba.name = 'Ba'
# Ba.label = 1
# B.children.append(Ba)
# 
# Bb = Node()
# Bb.name = 'Bb'
# Bb.label = 0
# B.children.append(Bb)
# 
# print A.print_dnf_tree()



