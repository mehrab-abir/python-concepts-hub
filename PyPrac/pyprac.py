"""firstName = input("Enter your first name: ")
lastName = input("Enter your last name: ")
age = int(input("Enter your age: "))

if age < 18:
    print(f"Sorry {firstName}, you are too young to enter this site.")
else:
    print(f"Welcome, {firstName + lastName}! Enjoy.")"""


print("************************************")

""" base = int(input("Enter the value of base: "))
height = int(input("Enter the value of height: "))

area = 0.5*base * height

print(f"Area of the triangle is : {area}") """

print("************************************")

"""someText = "Lorem IpsuM DoloR Set AmetE"

upperCase = someText.upper()

print(upperCase)

print(someText.lower())"""

"""sscGPA = float(input("SSC GPA: "))
hscGPA = float(input("HSC GPA: "))

if (sscGPA == 5.00) and (hscGPA == 5.00):
    print("You will get 100% Scholarship.")
elif(sscGPA >=4.00) and (hscGPA == 5.00):
    print("You will get 80% Scholarship")
elif(sscGPA == 5.00) and (hscGPA >= 4.00):
    print("You will get 70% Scholarship")
elif(sscGPA >= 4.00) and (hscGPA >= 4.00):
    print("You will get 50% Scholarship")
else:
    print("No scholarship is available for you")"""

""" year = int(input("Enter the year: "))

if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year") """


""" country = ['Bangladesh', 'India', 'Pakistan','Nepal','Bhutan']

asia1, asia2, asia3, asia4, asia5 = country

print(asia2)

country.insert(4, 'Srilanka')

print(country) """

""" names = ['Mustak', 'Abir', 'Argho','Sakib','Ibrahim','Shahriar','Adityo']

for name in names:
    print(name)

id = 1

while id <=10:
    print(f"ID {id}")
    id = id +1 """

""" numberList = list(range(0,101,5))
print(numberList) 

x = list(range(0,5))
print(x)
"""

""" def numbers():
    num = 1
    while num <= 10:
        print(num)
        num = num + 1
print("These are some other stuffs")

numbers() """ 


#check string
text = "Python is a Popular Programming Language"

searchItem = input("Search: ")

# text_lowerCase = text.lower()
# print(text_lowerCase)

if searchItem.lower() in text.lower():
    print(f"Results found: {searchItem.lower()}")
else:
    print(f"Results: Nothing found")


""" letters = "Bangladesh is our country"

print(letters.replace("Bangladesh", "Canada")) """


