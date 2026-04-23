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
    
    def print_list(self):
        temp = self.head
        
        while temp is not None:
            print(temp.value, end=" ")
            temp = temp.next
        print()
        
    def selectionSort(self):
        temp = self.head
        
        while temp.next is not None:
            curNode = temp.next
            while curNode is not None:
                if temp.value > curNode.value:
                    temp.value, curNode.value = curNode.value, temp.value
                else:
                    curNode = curNode.next
            temp = temp.next

s_list = SinglyLinkedList()

nums = list(map(int,input("Enter numbers: ").split()))

for num in nums:
    s_list.push_back(num)

s_list.print_list()

s_list.selectionSort()

print("After sorting: ")
s_list.print_list()