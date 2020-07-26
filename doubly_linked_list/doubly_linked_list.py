"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
class ListNode:
    def __init__(self, value, prev=None, next_node=None):
        self.prev = prev
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def get_prev(self):
        return self.prev

    def set_next(self, new_next):
        # set this node's next_node reference to the passed in node
        self.next_node = new_next

    def __str__(self):
        return f"node info: val={self.value}, prev={self.prev}, next_node={self.next_node}"

            
"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length
    
    def __str__(self):
        return f"head-{self.head}, tail-{self.tail}, len-{self.length}"

    def print_list(self):
        # empty
        if self.length == 0:
            print(self.__str__(), '\nempty list')
            return

        print(f"head-{self.head.value}, tail-{self.tail.value}, len-{self.length}")
        curr = self.head
        i = 0
        # while i <= self.length:
        while i <= self.length:
            i += 1
            if curr.get_next():
                print(curr.value)
                curr = curr.get_next()
            if curr == self.tail:
                print(curr.value)
                return
       
    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """
    def add_to_head(self, value):
        new_node = ListNode(value, None, self.head)
        print('add to head ->  new_node', new_node.value)
        if self.length == 0:
            self.tail = new_node
            # new_node.next_node = self.head
        self.head = new_node
        self.length += 1
        
        
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        # none
        if self.head is None:
            return None
        to_remove = self.head.value
        # one
        if self.head == self.tail:
            self.head, self.tail = None
        else:
            new_head = self.head.next_node
            self.head = new_head
            new_head.prev = None
        self.length -= 1
        return to_remove


    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """

    def add_to_tail(self, value):
        new_node = ListNode(value)
        print('add to tail ->  new_node', new_node.value)
        if not self.tail and not self.head:
            self.tail = new_node
            self.head = new_node
        else:
            self.tail.next_node = new_node
            new_node.next = None
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
            
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        # none
        if self.length == 0:
            return None
        # one
        if self.length == 1:
            self.head, self.tail = None
            return

        to_remove = self.tail
        new_tail = self.tail.prev
        print(self.tail.value, new_tail.value)

        self.length -= 1
        return to_remove

            
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        pass
        
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        pass

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        pass

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        pass

dll = DoublyLinkedList()
dll.print_list()
dll.add_to_tail(3)
dll.print_list()
dll.add_to_head(2)
dll.print_list()
dll.add_to_head(1)
dll.print_list()
dll.add_to_tail(4)
dll.print_list()
dll.remove_from_head()
dll.print_list()

# dll.delete(dll.head)
# print(dll.head.value, 1)
# print(dll.tail.value, 6)
# print(len(dll), 2)

# dll.delete(dll.head)
# print(dll.head.value, 6)
# print(dll.tail.value, 6)
# print(len(dll), 1)