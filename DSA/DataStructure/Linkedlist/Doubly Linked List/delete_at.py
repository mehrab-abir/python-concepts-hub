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
        self.length += 1

    def push_back(self,value):
        newnode = self.Node(value)

        if self.tail is None:
            self.head = newnode
            self.tail = newnode
        else:
            self.tail.next = newnode
            newnode.prev = self.tail
            self.tail = newnode
        self.length += 1
    
    def pop_front(self):
        if self.head is None:
            raise IndexError("The list already empty")
        
        self.head = self.head.next

        if self.head is None:
            self.tail = None
        
        self.head.prev = None
        self.length -= 1

    def pop_back(self):
        if self.head is None:
            raise IndexError("The list is empty")
        
        self.tail = self.tail.prev

        if self.tail is None:
            self.head = None
        
        self.tail.next = None
        self.length -= 1

    def delete_at(self,index):
        if index < 0 or index >= self.length:
            raise IndexError("Index out of range")
        
        temp = self.head

        for _ in range(index):
            temp = temp.next

        if temp.prev is None and temp.next is None:
            #the only node, delete it (head)
            self.head = None
            self.tail = None
        elif temp.prev is None:
            #target node is head, delete head
            self.head = self.head.next
            self.head.prev = None
        elif temp.next is None:
            #target node is tail, delete tail
            self.tail = self.tail.prev
            self.tail.next = None
        else:
            #delete the target node that is somewhere in middle
            temp.prev.next = temp.next
            temp.next.prev = temp.prev 

        self.length -= 1
    
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

deleteIndex = int(input("Which index to delete: "))
d_list.delete_at(deleteIndex)

print("The list after deleting index 3:")
d_list.print_list()
