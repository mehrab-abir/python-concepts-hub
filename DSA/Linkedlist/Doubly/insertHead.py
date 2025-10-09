class DoublyLinkedList:
    class Node:
        def __init__(self,value):
            self.value = value
            self.next = None
            self.prev = None

    def __init__(self):
            self.head = None
            self.tail = None
            self.length = 0 

    def push_front(self,value):
        newnode = self.Node(value)
        
        if self.head is None:
             self.head = newnode
             self.tail = newnode
        else:
             newnode.next = self.head
             self.head.prev = newnode
             self.head = newnode
        
    def push_back(self, value):
            newnode = self.Node(value)

            if self.tail is None:
                self.head = newnode
                self.tail = newnode
            else:
                self.tail.next = newnode
                newnode.prev = self.tail
                self.tail = newnode    

    def print_list(self):
            temp = self.head

            while temp:
                print(temp.value, end=" ")
                temp = temp.next
            print()    

d_list = DoublyLinkedList()

nums = list(map(int,input("Enter numbers: ").split()))

for num in nums:
    d_list.push_back(num)

print("The Doubly Linked List: ")
d_list.print_list()

newHead = int(input("Enter a value for head: "))

d_list.push_front(newHead)

print("The new list: ")
d_list.print_list()
