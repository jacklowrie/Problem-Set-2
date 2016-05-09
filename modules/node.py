# DOCUMENTATION
# =====================================
# Class node attributes:
# ----------------------------
# children - a list of 2 nodes if numeric, and a dictionary (key=attribute value, value=node) if nominal.  
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

dnf_str = ''
first_str =''

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
        if self.label != None:
            return self.label
        else:
            if self.is_nominal:
                return self.children[instance[self.decision_attribute]].classify(instance)
            else:
                if instance[self.decision_attribute] >= self.splitting_value:
                    return self.children[1].classify(instance)
                else:
                    return self.children[0].classify(instance)

    def print_tree(self, level=0):
        '''
        returns a string of the entire tree in human readable form
        '''
        pass
             

    def print_dnf_tree(self):
        '''
        returns the disjunct normalized form of the tree.
        '''
        caseList = []
        totStr = ''
        
        for i in self.print_dnf_tree_helper(""):
            newStr = "(" + i + ")"
            caseList.append(newStr)
            
        for x in xrange(0,len(caseList)):
            if x == 0:
                totStr+= caseList[x]
            else:
                caseList[x] = "\n|| " + caseList[x]
                totStr+= caseList[x]
                
        return totStr
            

    def print_dnf_tree_helper(self, linked):
        '''
        returns the disjunct normalized form of the tree.
        '''
        if self.label != None:
            if self.label == 1:
                return [linked[4:]]
            else:
                return []
        totSum = []
        if self.is_nominal:
            for (x,y) in self.children.items():
                temp = linked + " && " + str(self.name) + " = " + str(self.splitting_value)
                totSum += y.print_dnf_tree_helper(temp)
            return totSum
        for (x,y) in [("<", self.children[0]), (">=", self.children[1])]:
            temp = linked + " && " + str(self.name) + " " + x + " " + str(self.splitting_value)
            totSum += y.print_dnf_tree_helper(temp)
        return totSum
        
    
        