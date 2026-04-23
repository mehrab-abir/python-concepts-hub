class SinglyLinkedList:
    class Node:
        def __init__(self,value):
            self.value = value
            self.next = None
    
    def __init__(self):
        self.sentinel = self.Node(None)
        self.head = self.sentinel
        self.tail = self.sentinel
        self.length = 0

    def push_front(self,value):
        newnode = self.Node(value)
        self.length += 1

        newnode.next = self.sentinel.next
        self.sentinel.next = newnode

        if self.tail == self.sentinel:
            self.tail = newnode

    def push_back(self,value):
        newnode = self.Node(value)
        self.length += 1

        self.tail.next = newnode
        self.tail = newnode

    def pop_front(self):
        if self.sentinel.next is None:
            raise IndexError("List is already empty")
        
        self.sentinel.next = self.sentinel.next.next
        
        #if list becomes empty
        if self.sentinel.next is None:
            self.tail = self.sentinel
        self.length -= 1

    def pop_back(self):
        if self.sentinel.next is None:
            raise IndexError("List is empty")

        #if there is only one node - first node's next is none
        if self.sentinel.next.next is None:
            self.sentinel.next = None
            self.tail = self.sentinel
            self.length -= 1
            return
        
        #otherwise
        temp = self.sentinel
        for _ in range(self.length-1):
            temp = temp.next

        temp.next = None
        self.tail = temp
        self.length -= 1

    def insert_at(self, value,index):
        if index < 0 or index > self.length:
            raise IndexError("Index out of range")

        newnode = self.Node(value)

        if index == 0:
            newnode.next = self.sentinel.next
            self.sentinel.next = newnode
            self.length += 1
            return
        
        if index == self.length:
            self.tail.next = newnode
            self.tail = newnode
            self.length += 1
            return
        
        temp = self.sentinel

        for _ in range(index):
            temp = temp.next

        #newnode to be inserted after temp
        newnode.next = temp.next
        temp.next = newnode
        self.length += 1

    def delete_at(self,index):
        if index < 0 or index >= self.length:
            raise IndexError("Index out of range")
        
        if index == 0:
            self.sentinel.next = self.sentinel.next.next

            if self.sentinel.next is None:
                self.tail = self.sentinel
            self.length -= 1
            return
        
        temp = self.sentinel
        for _ in range(index):
            temp = temp.next

        temp.next = temp.next.next

        if temp.next is None:
            self.tail = temp
        self.length -= 1

    def print_list(self):
        if self.sentinel.next is None:
            raise IndexError("List is empty")
        
        temp = self.sentinel.next

        while temp is not None:
            print(temp.value, end=" ")
            temp = temp.next
        print()

s_list = SinglyLinkedList()

nums = list(map(int,input("Enter numbers: ").split()))

for num in nums:
    s_list.push_back(num)

print("The list: ")
s_list.print_list()

# s_list.push_front(10)
# s_list.pop_back()
# s_list.pop_front()
# s_list.insert_at(100,3)
# s_list.insert_at(100,0)
# s_list.insert_at(100,5) #when index == length

print("The list after: ")
s_list.print_list()