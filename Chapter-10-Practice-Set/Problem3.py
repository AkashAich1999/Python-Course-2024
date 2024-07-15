# 3. Create a class with a class attribute a; create an object from it and set ‘a’ 
# directly using ‘object.a = 0’. Does this change the class attribute? 
 
class Test:
    a = 11

t = Test()
print(t.a)      # 11  # prints the class attribute because instance attribute is not present.
t.a = 0               # instance attribute is set.
print(t.a)      # 0   # prints the instance attribute because instance attribute is present.

# No, The class attribute did not change
print(Test.a)   # 11 # Prints the class attribute