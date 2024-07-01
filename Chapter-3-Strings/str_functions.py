name = "Akash Aich"

print(len(name))                # 10
print(name.endswith("ash"))     # False
print(name.endswith("ich"))     # True
print(name.startswith("ak"))    # False
print(name.startswith("Ak"))    # True

print(name.capitalize())        # Akash aich

print(name.count("A"))          # 2
print(name.count("d"))          # 0
print(name.find("sh"))          # 3
print(name.find("ss"))          # -1 (If Not Found, find() returns -1)

r = "stuck"
print(r.replace("st","l"))      # luck

r = "He is a very very good boy"
print(r.replace("very",":"))    # He is a : : good boy