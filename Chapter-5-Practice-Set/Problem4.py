# 4. What will be the length of following set s: 
# s = set() 
# s.add(20) 
# s.add(20.0) 
# s.add('20') # length of s after these operations?

s = set()
s.add(20) 
s.add(20.0) 
s.add('20')

print(s)        # {'20', 20}
print(len(s))   # 2

# Intersting: Answer is 2 and not 3.
# 1 == 1.0 (is True & not False in Python)