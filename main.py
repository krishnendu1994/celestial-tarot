# x=10
# y=20
# z=x+y
# w=50
# print("The sum of", x, "and", y, "is", z)

# if x > y and z < w:
#     print(x, "is greater than", y, "and the sum is less than", w)
# elif x < y and z < w:
#     print(x, "is less than", y, "and the sum is less than",w)
# else:
#     print(x, "is equal to", y, "or the sum is", w, "or more")
# i=1
# for j in range(i, 6):
#     print("Iteration", j)
#     for k in range(i, 3):
#         print("Nested Iteration", k)

# for char in "Hello":
#     print("Character:", char)   

# arr = [1, 2, 3, 4, 5]
# assoc = [{ "id": 1 , "name": "John Doe" , "roll": 101 }, { "id": 2 , "name": "Jane Doe" , "roll": 102 }, { "id": 3 , "name": "Jim Doe" , "roll": 103 }, { "id": 4 , "name": "Jill Doe" , "roll": 104 }, { "id": 5 , "name": "Jack Doe" , "roll": 105 }]
# for index in range(len(arr)):
#     print("Array Element at index", index, "is", arr[index])
# assoc = [{ "id": 1 , "name": "John Doe" , "roll": 101 }, { "id": 2 , "name": "Jane Doe" , "roll": 102 }, { "id": 3 , "name": "Jim Doe" , "roll": 103 }, { "id": 4 , "name": "Jill Doe" , "roll": 104 }, { "id": 5 , "name": "Jack Doe" , "roll": 105 }]
# total_elements = len(assoc)
# for index, item in enumerate(assoc):
#     index += 1
#     print("[",index,"] ID:", item["id"], "Name:", item["name"], "Roll No:", item["roll"])
#     if(index == total_elements) :
#         print("No of results:", total_elements)

# def action(a, b=0,m="+"):
#     result = getattr(a, {
#         "+": "__add__",
#         "-": "__sub__",
#         "*": "__mul__",
#         "/": "__truediv__"
#     }[m])(b)
#     print("result of", a, m, b, "is", result)

# # a = int(input("Enter first number: "))
# # b = int(input("Enter second number: "))
# # m = input("Enter operator (+ - * /): ")
# # action(a, b, m)
# action(10, 5, "*")

# name = "kpaul"
# if not name:
#     print("Name is not set")
# else:
#     print("Name is set to", name)

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def greet(self):
#         print("Hello, ",self.name," welcome you to our Website. thanks for confirming age is ", self.age)

# Person1 = Person("kpaul", 25)
# Person1.greet()

# class BankAccount:
#     def __init__(self, account_holder, account_holder_sign="", balance=0):
#         self.account_holder = account_holder
#         self.account_holder_sign = account_holder_sign
#         self.balance = balance
#     def create_account(self, account_holder, account_holder_sign):
#         self.account_holder = account_holder
#         self.account_holder_sign = account_holder_sign
#         self.balance = 0
#         print("Account created successfully for", self.account_holder)
#     def deposit(self, amount, account_holder_sign):
#         if amount > 0:
#             self.balance += amount
#             print("Deposit successful by", self.account_holder, "with sign", account_holder_sign, ". New balance is:", self.balance)
#             return True
#         else:
#             print("Invalid deposit amount.")
#             return False
#     def withdraw(self, amount, account_holder_sign):
#         if amount > 0 and amount <= self.balance:
#             self.balance -= amount
#             print("Withdrawal successful. New balance is:", self.balance)
#             return True
#         else:
#             print("Invalid withdrawal amount.")
#             return False
#     def get_balance(self, account_holder_sign):
#         if account_holder_sign == self.account_holder_sign:
#             print(self.balance)
#             return self.balance
#         else:
#             print("Unauthorized access.")
#             return None

# account = BankAccount("Krishnendu Paul", "KP1994")


# # account.deposit(1000, "KP1994")
# account.deposit(1500, "KP1994")
# account.get_balance("KP1994")


# class Person:
#     def __init__(self, name: str, join_date: str):
#         self.name = name
#         self.join_date = join_date
#     def greet(self):
#         print("Hello, ",self.name," welcome you to our Company.")

# class Employee(Person):
#     def __init__(self,name: str, join_date: str, position: str, salary:float):
#         super().__init__(name, join_date)
#         self.position = position
#         self.salary = salary
#     def display_info(self):
#         self.greet()
#         print("Join Date:", self.join_date)
#         print("Position:", self.position)
#         print("Salary:", self.salary)
# employee1 = Employee("John Doe", "2026-01-15", "Software Engineer", 75000)
# employee1.display_info()

class Dog:
    def __init__(self):
        self.name = "Dog"
    def sound(self):
        self.bark = "Woof! Woof!"
        return self.bark

class Cat:
    def __init__(self):
        self.name = "Cat"
    def sound(self):
        self.bark = "Meow! Meow!"
        return self.bark

dog = Dog()
cat = Cat()

for animal in (dog, cat):
    print(animal.name + " bark", animal.sound())
