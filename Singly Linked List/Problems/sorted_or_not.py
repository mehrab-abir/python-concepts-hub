class SinglyLinkedList:
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
        self.length += 1
        
    def isSorted(self):
        temp = self.head
        
        sorted = 1
        
        while temp.next is not None:
            if temp.value > temp.next.value:
                sorted = 0
                break
            else:
                temp = temp.next
                
        if sorted == 1:
            print("Sorted")
        else:
            print("Not sorted")

s_list = SinglyLinkedList()

nums = list(map(int,input("Enter numbers: ").split()))

for num in nums:
    s_list.push_back(num)

s_list.isSorted()