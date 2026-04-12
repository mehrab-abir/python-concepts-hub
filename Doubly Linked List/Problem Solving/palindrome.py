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
        
    def push_back(self,value):
        newnode = self.Node(value)
        
        if self.head is None:
            self.head = newnode
            self.tail = newnode
            self.length += 1
            return
        
        self.tail.next = newnode
        newnode.prev = self.tail
        self.tail = newnode
        
    def isPalindrome(self):
        
        if self.head is None:
            raise IndexError("List is empty")
        
        if(self.head.next is None):
            print("Input at least two values to check palindrome")
            return
        
        i = self.head
        j = self.tail
        
        palindrom = 1
        while i is not None and j is not None and i != j and j != i.prev:
            if i.value != j.value:
                palindrom = 0
                break
            else:
                i = i.next
                j = j.prev
                
        if palindrom == 1:
            print("Palindrome")
        else:
            print("Not plaindrome")
    
    def print_list(self):
        if self.head is None:
            raise IndexError("Empty list")
        
        temp = self.head
        while temp is not None:
            print(temp.value, end=" ")
            temp = temp.next
        print()
        
d_list = DoublyLinkedList()

nums = list(map(int,input("Enter values: ").split()))
for value in nums:
    d_list.push_back(value)

print("The list: ")
d_list.print_list()

d_list.isPalindrome()
        
            