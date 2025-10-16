class LinkedList:
    class Node:
        def __init__(self,value):
            self.value = value
            self.next = None
    
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    # Push back
    def push_back(self,value):
        newnode = self.Node(value)
        self.length += 1

        if self.tail is None:
            self.head = newnode
            self.tail = newnode
            return

        self.tail.next = newnode
        self.tail = newnode

    #push front
    def push_front(self,value):
        newnode = self.Node(value)
        self.length += 1

        if self.head is None:
            self.head = newnode
            self.tail = newnode
            return

        newnode.next = self.head
        self.head = newnode

    #pop front
    def pop_front(self):
        if self.head is None:
            raise IndexError("The linked list already empty")
        
        self.head = self.head.next

        if self.head is None:
            self.tail = None

        self.length -= 1

    #pop back
    def pop_back(self):
        if self.head is None:
            raise IndexError("List is already empty")
        
        #if there is only one node
        if self.head.next is None:
            self.head = None
            self.tail = None
            self.length -= 1
            return
        
        temp = self.head
        for i in range(self.length-2):
            temp = temp.next
        
        temp.next = None
        self.tail = temp
        self.length -= 1

    #insert at middle
    def insert_at(self, value, index):
        if index < 0 or index > self.length:
            raise IndexError("Index out of range")
            
        newnode = self.Node(value)

        # insert at front 
        if index == 0:
            newnode.next = self.head
            self.head = newnode
            self.length += 1
            return
        
        #insert at end
        if index == self.length:
            self.tail.next = newnode
            self.tail = newnode
            self.length += 1
            return
        
        #insert at given index
        temp = self.head

        #stop just before the target index, so newnode will be inserted at right after the temp node
        for i in range(index-1):
            temp = temp.next

        newnode.next = temp.next
        temp.next = newnode
        self.length += 1
    
    #delete from a given index
    def delete_at(self,index):
        if index < 0 or index >= self.length:
            raise IndexError("Index out of range")
        
        if index == 0:
            #delete head
            self.head = self.head.next
            
            #if there was only one node
            if self.head is None:
                self.tail = None

            self.length -= 1
            return
        
        temp = self.head

        #stop just before the target node
        for _ in range(index-1):
            temp = temp.next
        
        temp.next = temp.next.next
        self.length -= 1
        

    def print_list(self):
        if self.head is None:
            raise IndexError("List is empty")
        
        temp = self.head

        while temp is not None:
            print(temp.value,end=" ")
            temp = temp.next 
        print()

s_list = LinkedList()

nums = list(map(int,input("Enter Numbers: ").split()))

for num in nums:
    s_list.push_back(num)

print("The list: ")
s_list.print_list()

""" newValue = int(input("Enter a value to insert: "))
index = int(input("Enter index: "))
s_list.insert_at(newValue,index) """

# value = int(input("Enter new value: "))
# s_list.push_front(value)

# s_list.pop_front()
# s_list.pop_back()

index = int(input("Enter index: "))
s_list.delete_at(index)

print("The list after updation: ")
s_list.print_list()


        

        


