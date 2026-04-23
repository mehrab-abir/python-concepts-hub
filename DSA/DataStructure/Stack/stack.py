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

    def pop_back(self):
        if self.head is None:
            raise IndexError("List is already empty")

        # if there is only one node
        if self.head == self.tail:
            self.head = None
            self.tail = None
            self.length -= 1
            return

        # move tail pointer back
        self.tail = self.tail.prev
        self.tail.next = None
        self.length -= 1


    def print_list(self):
        temp = self.head

        while temp is not None:
            print(temp.value, end=" ")
            temp = temp.next
        print()

class Stack:
    def __init__(self):
        self.st = DoublyLinkedList()
        
    def push(self,value):
        self.st.push_back(value)
        
    def pop(self):
        self.st.pop_back()
        
    def top(self):
        return self.st.tail.value
    
    def empty(self):
        return self.st.length == 0
    
    def size(self):
        return self.st.length

d_list = DoublyLinkedList()

nums = list(map(int,input("Enter numbers: ").split()))

for num in nums:
    d_list.push_back(num)

print("The list: ")
d_list.print_list()

stack = Stack()

for num in nums:
    stack.push(num)
    
print("The stack: ")
while not stack.empty():
    print(stack.top())
    stack.pop()
