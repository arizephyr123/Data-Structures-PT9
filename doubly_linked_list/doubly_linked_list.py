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
        new_node = ListNode(value)
        # print('add to head ->  new_node', new_node.value, 'self.head', self.head, 'self.tail', self.tail)
        if self.length == 0:
            self.tail = new_node
        new_node.next_node = self.head
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
            self.head = None
            self.tail = None
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
        # print('add to tail ->  new_node', new_node.value, 'self.head', self.head, 'self.tail', self.tail)
        print('add to tail ->  new_node', new_node.value)
        if not self.tail and not self.head:
            print('add to tail **If NOt 1->  len', self.length)
            self.tail = new_node
            self.head = new_node
            self.length += 1
            print('add to tail **If NOt 2->  len', self.length)
        else:
            print('add to tail **ELSE 1->  len', self.length)
            new_node.next_node = None
            new_node.prev = self.tail
            self.tail.next_node = new_node
            self.tail = new_node
            self.length += 1
            print('add to tail **ELSE 2->  len', self.length)
            
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        print("self.head remove from tail", self.head, 'len- ', self.length)
        # none
        if self.length == 0:
            return None

        elif self.length == 1:
            to_remove = self.tail.value
            print("to_remove **ELIF", to_remove)
            self.length = 0
            self.head = None
            self.tail = None
            return to_remove

        else:
            to_remove = self.tail.value
            print("to_remove **ELSE", to_remove)
            self.length -= 1
            self.tail = self.tail.prev
            return to_remove

            
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        self.add_to_head(node.value)
        self.delete(node)

        
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        if self.length == 0:
            self.length -= 1
        self.add_to_tail(node.value)
        self.delete(node)
    

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        print('delete ->  len', self.length)
        if self.head is None and self.tail is None:
            print('delete **EMPTY ->  len', self.length)
            return None

        elif node.prev == None:
            print('delete **PREV NONE ->  len', self.length)
            self.remove_from_head()

        elif node.next_node == None:
            self.remove_from_tail()

        else:
            to_delete = node.value

            old_before = node.prev
            old_after = node.next_node
            old_before.next_node = old_after
            old_before.prev = old_before




    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        # empty list
        if self.head is None:
            return None
        curr_node = self.head
        curr_max = self.head.value
        while curr_node is not None:
            if curr_node.value > curr_max:
                curr_max = curr_node.value
            curr_node = curr_node.next_node
        
        return curr_max

node = ListNode(1)
dll = DoublyLinkedList(node)
# print(dll.head.value, " ? 1")
# dll.add_to_head(10)
dll.print_list()
# print(dll.head.value, "? 10")
# print(dll.head.next_node.value, "? 1")
# print(len(dll), "? 2")

dll.add_to_head(40)
print(dll.tail.value, "-> 1 ? ~ 1")
print(dll.head.value, "-> 40 ? ~ 2")

dll.move_to_end(dll.head)
print(dll.tail.value,"-> 40 ? ~ 3")
print(dll.tail.prev.value,"-> 1 ? ~ 4")
print(len(dll),"-> 2 ? ~ 5")

dll.add_to_tail(4)
dll.move_to_end(dll.head.next_node)
print(dll.tail.value, "-> 40 ? ~ 6")
print(dll.tail.prev.value, "-> 4 ? ~ 7")
print(len(dll),"-> 3 ? ~ 8")


# dll.remove_from_tail()
# print(dll.head, " ? None ->1")
# print(dll.tail, " ? None ->2")
# print(len(dll), "? 0 ->3")
# dll.add_to_tail(33)
# print(dll.head.value, "? 33 ->4")
# print(dll.tail.value, "? 33 ->5")
# print(len(dll), "? 1 ->6")
# print(dll.remove_from_tail(), "? 33 ->7")
# print(len(dll), "? 0 ->8")
# dll.add_to_tail(68)
# print(len(dll), "? 1 ->9")
# print(dll.remove_from_tail(), "? 68 ->10")
# print(len(dll), "? 0 -11>")

'''
dll.print_list()
dll.add_to_tail(3)
dll.print_list()
dll.add_to_head(2)
dll.print_list()
dll.add_to_head(1)
dll.print_list()
dll.add_to_tail(4)
dll.print_list()
# print('remove from head')
# dll.remove_from_head()
# dll.print_list()
# print('remove from tail')
# dll.remove_from_tail()
# dll.print_list()
print('move to front')
dll.move_to_front(dll.tail)
dll.print_list()
print('move to end')
dll.move_to_end(dll.head)
dll.print_list()
print('get max')
print(dll.get_max())
dll.print_list()
# print('delete')
# dll.delete(dll.head)
# dll.print_list()

# dll.delete(dll.head)
# print(dll.head.value, 1)
# print(dll.tail.value, 6)
# print(len(dll), 2)

# dll.delete(dll.head)
# print(dll.head.value, 6)
# print(dll.tail.value, 6)
# print(len(dll), 1)
'''