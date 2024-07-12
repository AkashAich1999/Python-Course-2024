# readlines()
f = open("file2.txt")

lines = f.readlines()   # Returns a List

print(lines, type(lines))

f.close()

# readline()
g = open("file2.txt")

line1 = g.readline()
print(line1, type(line1))

line2 = g.readline()
print(line2, type(line2))

line3 = g.readline()
print(line3, type(line3))

line4 = g.readline()
print(line4, type(line4))
print(line4 == "")

g.close()


h = open("file2.txt")
l = h.readline()
while(l != ""):
    print(l, type(l))
    l = h.readline()
h.close()    