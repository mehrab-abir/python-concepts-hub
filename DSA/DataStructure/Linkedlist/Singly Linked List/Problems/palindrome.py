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
        
    def reverseList(self):
        reversed_head = None
        temp = self.head
        
        while temp is not None:
            newnode = self.Node(temp.value)
            
            newnode.next = reversed_head
            reversed_head = newnode
            temp = temp.next
        
        return reversed_head
    
    def isPlaindrome(self,reversedHead):
        i = self.head
        j = reversedHead
        
        palindrome = 1
        
        while i is not None and j is not None:
            if i.value != j.value:
                palindrome = 0
                break
            else:
                i = i.next
                j = j.next
        
        if palindrome == 1:
            print("Palindrome")
        else:
            print("Not palindrome")
        

s_list = SinglyLinkedList()

nums = list(map(int,input("Enter numbers: ").split()))

for num in nums:
    s_list.push_back(num)

reversedHead = s_list.reverseList()
s_list.isPlaindrome(reversedHead)