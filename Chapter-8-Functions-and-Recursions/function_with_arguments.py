# Program 1:
def goodDay(name):
    print("Good Day, " + name + "!")

goodDay("Akash Aich")    
goodDay("Darshit Sorathiya")    
goodDay("Manab Saha")    
goodDay("Mintu Moni Kurmi")

# Program 2:
def goodDay(name, ending):
    print("Good Day, " + name + "!")
    print(ending)

goodDay("Akash Aich", "Thank You!")    
goodDay("Darshit Sorathiya", "Thank You!")    
goodDay("Manab Saha", "Thank You!")    
goodDay("Mintu Moni Kurmi", "Thank You!")

# Program 3:
def goodDay(name, ending):
    print("Good Day, " + name + "!")
    print(ending)
    return "Ok!!"

a = goodDay("Akash Aich", "Thank You!")    
print(a)