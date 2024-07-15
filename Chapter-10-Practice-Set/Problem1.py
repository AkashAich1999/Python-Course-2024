# 1. Create a class “Programmer” for storing information of few programmers working at Microsoft.

class Programmer:
    company = "Microsoft"
    def __init__(self, name, salary, pin):
        self.name = name
        self.salary = salary
        self.pin = pin

a = Programmer("Akash Aich", 1800000, 12450)
print(a.name, (a.company).rjust(18), a.pin, a.salary)

d = Programmer("Darshit Sorathiya", 1800000, 12451)
print(d.name, (d.company).rjust(11), d.pin, d.salary)

ma = Programmer("Manab Saha", 1800000, 12452)
print(ma.name, (d.company).rjust(18), ma.pin, ma.salary)

mi = Programmer("Mintu Moni Kurmi", 1800000, 12453)
print(mi.name, (d.company).rjust(12), mi.pin, mi.salary)