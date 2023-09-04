# class A:
#     def say_hello(self):
#         print("Hello")
#
#
# class B(A):
#     def say_goodbye(self):
#         print("Goodbye")
#
#
# parent = A()
# child = B()
#
# child.say_hello()

class Parent:
    def __init__(self, lname, address, job):
        self.lastname = lname
        self.address = address
        self.job = job

    def say_hello(self):
        print("Hello")


class Child(Parent):
    def __init__(self, lname, address, uni, job=None):
        super().__init__(lname, address, job)
        self.university = uni

    def say_goodbye(self):
        print("Goodbye")


valed = Parent("Ahmadi", "Ekbatan", "Teacher")
farzand = Child("Mohammadi", "Ekbatan", "Sharif")
print(farzand.job)
