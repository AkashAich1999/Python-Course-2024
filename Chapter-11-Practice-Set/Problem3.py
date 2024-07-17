# 3. Create a class ‘Employee’ and add salary and increment properties to it. 
# Write a method ‘salaryAfterIncrement’ method with a @property decorator with a setter
# which changes the value of increment based on the salary. 

class Employee:
    def __init__(self, salary, increment):
        self._salary = salary
        self._increment = increment

    @property
    def salary(self):
        return self._salary

    @property
    def increment(self):
        return self._increment

    @salary.setter
    def salary(self, value):
        self._salary = value

    @increment.setter
    def increment(self, value):
        self._increment= value

    @property
    def salaryAfterIncrement(self):  
        # n_salary = _salary + _salary * 10/100
        # n_salary = _salary * (1 + 10/100)
        return round((self._salary * (1 + self.increment/100)), 2)

    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self, new_salary):
        # n_salary = _salary * (1 + _increment/100)
        # (1 + _increment/100) = n_salary / _salary
        # _increment = ((n_salary / _salary) - 1) * 100
        self._increment = round((((new_salary / self.salary) - 1) * 100), 2)

e = Employee(50000, 10)          # salary is 50000 and increment is 10%
print(e.salaryAfterIncrement)    # Output: 55000.0

e.salaryAfterIncrement = 60000
print(e.increment)               # Output: 20.0