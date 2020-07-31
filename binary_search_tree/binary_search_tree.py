"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BinarySearchTree class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BinarySearchTree class.
"""
class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    
    def insert(self, value):
    # if value <= self.value:
        if value <= self.value:
            if self.left is None:
                self.left = BinarySearchTree(value)
            else: 
                self.left.insert(value)

        elif value > self.value:
            if self.right is None:
                self.right = BinarySearchTree(value)
            else:
                self.right.insert(value)


    # Return True if the tree contains the value
    # False if it does not
    # sometimes 
    def contains(self, target):
        contained = False
        if target == self.value:
            return True

        if target < self.value:
            if self.left:
                if target == self.left.value:
                    contained = True
                else:
                    self.left.contains(target)
            else:
                return contained

        if target > self.value:
            if self.right:
                if target == self.right.value:
                    contained = True
                else:
                    self.right.contains(target)
            else:
                return False
        return contained
            
        # same path as insert node but then compare it to target
            # equal return contained = true
            # < we go left
            # > we go right
            # not in tree
        pass

    # Return the maximum value found in the tree
    def get_max(self):
        # go right until right is None
        pass

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        curr_node = self
        fn(curr_node.value)
        stack = [] # nodes you need to backtrack to
        while curr_node.left:
            curr_node = self.left


    '''
    # ** Recursion- uses built in memory to remember which nodes we need to backtrack to 
        # base case when left and right are none
        # recursive case
        fn(self.value)
        if self.left is not None: #if self.left exists
            self.left.for_each(fn)
        if self.right is not None:
            self.right.for_each(fn)
    '''


    # STRETCH
    # when deleted node has 2 children- then the largest of the 2 children becomes the parent of the other sibling
    def delete(self, value):
        # search like we did in contains()

        # scenarios:
        # node no children:
            # update parent left/right
        # 
        pass

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self):
        # as far left as tree goes, parent, right REPEAT
        if self:
            if self.left:
                # go left with recursion
                self.left.in_order_print()
            print(self.value)

            if self.right:
                # go right with recursion
                self.right.in_order_print()
            print(self.value)


            
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self):
        # use queue
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self):
        # use stack
        pass

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self):
        # parent, left to end, back up to right then left
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self):
        # left, right, parent
        pass

bst = BinarySearchTree(5)
bst.insert(2)
print(bst.value, '= 5?')
print(bst.left.value, '= 2?')
bst.insert(3)
print(bst.left.right.value, '= 3?')
bst.insert(7)
print(bst.right.value, '= 7?')
print(bst.contains(5), '= True?')
print(bst.contains(7), '= True?')
print(bst.contains(8),'= False?')
# bst.insert(6)
# print(bst.left.right.value, ' = 3?')
# print(bst.right.left.value,' = 6?')





#=================================================
"""
This code is necessary for testing the `print` methods
"""
# bst = BinarySearchTree(1)

# bst.insert(8)
# bst.insert(5)
# bst.insert(7)
# bst.insert(6)
# bst.insert(3)
# bst.insert(4)
# bst.insert(2)

# bst.bft_print()
# bst.dft_print()

# print("elegant methods")
# print("pre order")
# bst.pre_order_dft()
# print("in order")
# bst.in_order_print()
# print("post order")
# bst.post_order_dft()  
