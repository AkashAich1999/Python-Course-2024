# class Employee:
#     a = 1
#     def show(self):
#         print(f"The instance attribute a's value is: {self.a}")

# e = Employee()
# e.a = 45

# e.show()

class Employee:
    a = 1
    @classmethod
    def show(cls):
        print(f"The class attribute of a's value is: {cls.a}")

e = Employee()
e.a = 45

e.show()