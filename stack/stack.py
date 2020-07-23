"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

Make sure the Stack tests pass.

3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?

An array uses Python's built-in methods to push and pop items into stack. LinkedList methods are custom built so they may be more or less performant based on customization of how they are built.
"""
# 1. Implement the Stack class using an array as the underlying storage structure.

class Stack:
    def __init__(self):
        self.size = 0
        self.storage = []

    def __len__(self):
        return len(self.storage)

    def push(self, value):
        self.storage.append(value)

    def pop(self):
        if len(self.storage) == 0:
            return None
        return self.storage.pop()



'''
# 2. Re-implement the Stack class, this time using the linked list implementation
from singly_linked_list import LinkedList
class Stack:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()

    def __len__(self):
        return self.storage.length

    def push(self, value):
        self.storage.add_to_head(value)

    def pop(self):
        return self.storage.remove_head()
'''