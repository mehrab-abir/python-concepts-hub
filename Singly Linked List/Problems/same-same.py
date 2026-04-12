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

s_list_1 = SinglyLinkedList()
s_list_2 = SinglyLinkedList()

nums = list(map(int,input("Enter numbers for list 1: ").split()))
for num in nums:
    s_list_1.push_back(num)

values = list(map(int,input("Enter numbers for list 2: ").split()))
for num in values:
    s_list_2.push_back(num)
    
""" print(s_list_1.length)
print(s_list_2.length) """

if s_list_1.length != s_list_2.length:
    print("Not same")
else:
    temp_1 = s_list_1.head
    temp_2 = s_list_2.head
    
    same = 1
    
    while temp_1 is not None:
        if temp_1.value != temp_2.value:
            same = 0
            break
        else:
            temp_1 = temp_1.next
            temp_2 = temp_2.next
            
    if same == 1:
        print("Same")
    else:
        print("Not same")