class LinkedList:
    class Node:
        def __init__(self,value):
            self.value = value
            self.next = None
            
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
        
    def push_back(self,value):
        newnode = self.Node(value)
        
        if self.head is None:
            self.head = newnode
            self.tail = newnode
            self.length += 1
            return
        
        self.tail.next = newnode
        self.tail = newnode
    
    def print_list(self):
        if self.head is None:
            raise IndexError("Empty list")
        
        temp = self.head
        while temp is not None:
            print(temp.value, end=" ")
            temp = temp.next
        print()
        
    def deleteValues(self,givenValue):
        if self.head is None:
            raise IndexError("Empty List")
        
        if self.head.value == givenValue:
            self.head = self.head.next
            
        temp = self.head
        while temp is not None and temp.next is not None:
            if temp.next.value == givenValue:
                temp.next = temp.next.next
            else:
                temp = temp.next
                
        #if all nodes were same and that was also given to delete, after the while loop, there will still be one node,,,so
        if self.head is not None and self.head.value == givenValue:
            self.head = self.head.next
            
            if self.head is None:
                self.tail = None
            
            self.length -= 1
        
s_list = LinkedList()

nums = list(map(int,input("Enter values: ").split()))
for value in nums:
    s_list.push_back(value)

print("The list: ")
s_list.print_list()

givenValue = int(input("Enter a value to delete: "))

s_list.deleteValues(givenValue)

print("The list after: ")
s_list.print_list()
        
            