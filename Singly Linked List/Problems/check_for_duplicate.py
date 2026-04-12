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

    def checkDuplicate(self):
        freq_array = {}

        temp = self.head
        while temp is not None:
            if temp.value in freq_array:
                freq_array[temp.value] += 1
            else:
                freq_array[temp.value] = 1
            temp = temp.next

        duplicate = 0
        for count in freq_array.values():
            if count > 1:
                duplicate = 1
                break

        if duplicate == 1:
            print("Duplicate exist")
        else:
            print("No duplicate values")

s_list = SinglyLinkedList()

nums = list(map(int,input("Enter numbers: ").split()))

for num in nums:
    s_list.push_back(num)

s_list.checkDuplicate()