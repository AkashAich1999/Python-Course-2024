# 3. Can we have a set with 18 (int) and '18' (str) as a value in it?
# Yes, We can have. Following is the code to show that:

s = set()
s.add(18)
s.add("18")

print(s)