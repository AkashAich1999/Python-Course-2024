# 7. Write a python function to remove a given word from a list ad strip it at the same time.

# Remove a Given Word
# def rem(l, word):
#     for item in l:
#         l.remove(word)
#         return l
    
# l = ["Akash", "Darshit", "Manab", "Mintu", "sh"]

# print(rem(l,"sh"))


def rem(l, word):
    n = []
    for item in l:
        if not(item == word):
            n.append(item.strip(word))
    return n        
    
l = ["Akash", "Darshit", "Manab", "Mintu", "sh"]
m = ["Akash", "Darshit", "Manab", "Mintu", "tu"]
n = ["Akash", "Darshit", "Manab", "Mintu", "an"]

print(rem(l,"sh"))
print(rem(m,"tu"))
print(rem(n,"an"))