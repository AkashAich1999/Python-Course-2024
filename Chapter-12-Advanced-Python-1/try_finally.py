try:
    a = int(input("Hey, Enter a Number: "))
    print(a)

except Exception as e:
    print(e)

finally:    
    print("I am inside finally")   # Executed regardless of error!