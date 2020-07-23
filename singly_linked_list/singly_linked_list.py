class Node:
    def __init__(self, value=None, next_node=None):
        # the value at this linked list node
        self.value = value
        # reference to the next node in the list
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        # set this node's next_node reference to the passed in node
        self.next_node = new_next


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __str__(self):
        return f"head-{self.head}, tail-{self.tail}, len-{self.length}"

    def print_list(self):
        # empty
        if self.length == 0:
            print(self.__str__(), '\nempty list')
            return

        print(f"head-{self.head.value}, tail-{self.tail.value}, len-{self.length}")
        curr = self.head

        if self.length == 1:
            print(curr.value)
            return

        else:
            i = 1
            while i < self.length +1:
                print(curr.value)
                # if curr == self.tail:
                #     print(curr.value)
                #     return
                curr = curr.get_next()
                i += 1
        

    def add_to_head(self, value):
        # make new node
        new_node = Node(value, self.head)
        if self.length == 0: # or could have if self.head is None and self.tail is None if there is no length attribute
            # empty list head and tail is None
            # original next_node was None, so new_node's next => will also be None
            self.tail = new_node
        # set new_node as head
        self.head = new_node
        self.length += 1

    def add_to_tail(self, value):
        # make new node
        new_node = Node(value)
        # if empty list
        if self.head is None and self.tail is None:
            self.head = new_node
        else: 
            # update old tail's pointer first because if set new_node as tail first then will not know where to point without iterating through whole list
            self.tail.set_next(new_node)
        self.tail = new_node
        self.length += 1

    def remove_head(self):
        # empty LL
        if self.head is None:
            # from tests can see expects None returned if empty list
            return None
        # store removed since test expecting it to be returned
        to_remove = self.head.get_value()
        # list with 1 node
        if self.head == self.tail:
            self.head = None
            self.tail = None
        # list with 2+ nodes
        else:
            self.head = self.head.get_next()
        self.length -= 1
        return to_remove

    def remove_tail(self):
        # empty LL
        if self.tail is None:
            return None

        to_remove = self.tail.get_value()
        print("to_remove",to_remove)

        # # one node
        if self.head == self.tail:
            self.head = None
            self.tail = None
        # # 2+ node
        else:
            prev = self.head # Node obj
            print("prev", prev.value)
            while prev.get_next() is not self.tail:
                prev = prev.get_next() 
            self.tail = prev
            self.tail.set_next(None)
            self.length -= 1
            return prev.get_value()
            
        
    def contains(self, target):
        contained = False
        if self.length == 1:
            if self.head.value == target:
                return True
        curr_node = self.head
        i = 0
        while i < self.length:
            i += 1
            if curr_node.value == target:
                return True
            curr_node = curr_node.get_next()
        return contained

            

    def get_max(self):
        if self.length == 0:
            return None
        
        max = self.head.value
        curr_node = self.head
        while curr_node is not None:
            if curr_node.value > max:
                max = curr_node.value
            curr_node = curr_node.get_next()
        return max


ll = LinkedList()
# # ll.print_list()
ll.add_to_head(3)
# # ll.print_list()
# ll.add_to_head(2)
# # ll.print_list()
# ll.add_to_head(1)
# ll.remove_tail()
ll.print_list()
print(ll.contains(3))

list = LinkedList()
list.add_to_tail(1)
list.add_to_tail(2)
list.add_to_tail(5)
list.add_to_tail(10)
list.print_list()
print(list.contains(10))
print(list.contains(2))
print(list.contains(1000))
