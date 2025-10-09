class DoublyLinkedList:
    class Node:
        def __init__(self,value):
            self.value = value
            self.next = None
            self.prev = None

    def __init__(self):
        self.head = None
        self.tail = None

    def push_front(self,value):
        newnode = self.Node(value)

        if self.head is None:
            self.head = newnode
            self.tail = newnode
        else:
            newnode.next = self.head
            self.head.prev = newnode
            self.head = newnode

    def push_back(self,value):
        newnode = self.Node(value)

        if self.tail is None:
            self.head = newnode
            self.tail = newnode
        else:
            self.tail.next = newnode
            newnode.prev = self.tail
            self.tail = newnode
    
    def pop_front(self):
        if self.head is None:
            raise IndexError("The list already empty")
        
        self.head = self.head.next

        if self.head is None:
            self.tail = None
        
        self.head.prev = None
    
    def print_list(self):
        if self.head is None:
            raise IndexError("The list is empty")

        temp = self.head

        while temp:
            print(temp.value, end=" ")
            temp = temp.next
        print()

d_list = DoublyLinkedList()

nums = list(map(int,input("Enter numbers: ").split()))

for num in nums:
    d_list.push_back(num)

print("The list:")
d_list.print_list()

d_list.pop_front()

print("The list after pop_front():")
d_list.print_list()