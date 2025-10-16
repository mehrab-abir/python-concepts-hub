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
        self.length += 1

    def push_front(self,value):
        newnode = self.Node(value)

        if self.head is None:
            self.head = newnode
            self.tail = newnode
            self.length += 1
            return
        
        newnode.next = self.head
        self.head.prev = newnode
        self.head = newnode
        self.length += 1

    def pop_front(self):
        if self.head is None:
            raise IndexError("List is already empty")
        
        self.head = self.head.next

        #if there was only one node
        if self.head is None:
            self.tail = None

        self.head.prev = None
        self.length -= 1

    def pop_back(self):
        if self.head is None:
            raise IndexError("List is already empty")
        
        self.tail = self.tail.prev

        #if there was only one node
        if self.tail is None:
            self.head = None

        #now, self.tail is in just before the tail node, so its next has to be null
        self.tail.next = None

    def insert_at(self,value,index):
        if index < 0 or index > self.length:
            raise IndexError("Index out of range")
        
        newnode = self.Node(value)

        if index == 0:
            newnode.next = self.head
            self.head.prev = newnode
            self.head = newnode
            self.length += 1
            return
        
        if index == self.length:
            self.tail.next = newnode
            newnode.prev = self.tail
            self.tail = newnode
            self.length += 1
            return

        temp = self.head
        for _ in range(index):
            temp = temp.next

        #now, temp is at the index, newnode to be inserted right before of the temp
        temp.prev.next = newnode
        newnode.prev = temp.prev
        newnode.next = temp
        temp.prev = newnode
        self.length += 1

    def delete_at(self, index):
        if self.head is None:
            raise IndexError("List is already empty")
        
        if index < 0 or index >= self.length:
            raise IndexError("Index out of range")
        
        #if index is of the first node - delete head
        if index == 0:
            self.head = self.head.next

            if self.head is None:
                self.tail = None
            self.length -= 1
            return

        temp = self.head
        for _ in range(index):
            temp = temp.next
        
        #now, temp is at the node we wanna delete

        # if temp is at the last node/tail - delete last node 
        if temp.next is None:
            self.tail = self.tail.prev
            self.tail.next = None
            self.length -= 1
            return
        
        temp.prev.next = temp.next
        temp.next.prev = temp.prev
        self.length -= 1

    def print_list(self):
        temp = self.head

        while temp is not None:
            print(temp.value, end=" ")
            temp = temp.next
        print()

d_list = DoublyLinkedList()

nums = list(map(int,input("Enter numbers: ").split()))

for num in nums:
    d_list.push_back(num)

print("The list: ")
d_list.print_list()


""" value = int(input("Enter a new value: "));
d_list.push_front(value) """

# d_list.pop_front()
# d_list.pop_back()

# insert at a given index 
value = int(input("Enter a new value: "))
index = int(input("Enter index: "))
d_list.insert_at(value, index)

# delete from a given index
""" index = int(input("Enter index to delete: "))
d_list.delete_at(index) """

print("The list after updation: ")
d_list.print_list()


