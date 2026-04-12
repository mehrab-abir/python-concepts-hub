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
        
    def search(self):
        searchNum = int(input("Enter a number to search: "))
        
        temp = self.head
        
        found = 0
        index = 0
        
        while temp is not None:
            if temp.value == searchNum:
                found = 1
                break
            else:
                temp = temp.next
                index += 1
        
        if found == 1:
            print("Found at index ",index)
        else:
            print("Not found")

s_list = SinglyLinkedList()

nums = list(map(int,input("Enter numbers: ").split()))

for num in nums:
    s_list.push_back(num)

s_list.search()