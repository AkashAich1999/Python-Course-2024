# Walrus Operator:
# Introduced in Python 3.8 onwards.
# Allows us to assign a value to a variable within an expression.

# Example 1:
a = True
print(a := False)

# Example 2:
numbers = [1, 2, 3, 4, 5]
while(n := len(numbers)) > 0:
    print(numbers.pop())
print(numbers)    

# Example 3:

# foods = list()
# while True:
#     food = input("What food do you like ?: ")
#     if food == "quit":
#         break
#     foods.append(food)
# print(foods) 

foods = list()
while(food := input("What food do you like ?: ")) != "quit":
    foods.append(food)
print(foods)    

# Example 4:
if(n := len([1, 2, 3, 4, 5])) > 3:
    print(f"Life is too long ({n} elements, expected <= 3)")