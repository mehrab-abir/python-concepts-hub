class Student:
    def __init__(self,name,id):
        self.name = name
        self.id = id

    def displayInfo(self):
        print(f"Name: {self.name}, ID: {self.id}")

s1 = Student("Jhon",101)
s2 = Student("Steve",102)

s1.displayInfo()

print("*****************")

s2.displayInfo()


class Phone:
    category = "Electronics" # all instances get it

phone_1 = Phone()
phone_2 = Phone()

print(phone_1.category)
print(phone_2.category)