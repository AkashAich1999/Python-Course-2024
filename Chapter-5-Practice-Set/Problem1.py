# 1. Write a program to create a dictionary of Hindi words with values as their English translation. Provide user with an option to look it up!
  
words = {
    "Jaal": "Water",
    "jaal": "Water",
    "Vayu": "Air",
    "vayu": "Air",
    "Prithvi": "Earth",
    "prithvi": "Earth",
    "Agni": "Fire",
    "agni": "Fire",
    "Akash": "Sky",
    "akash": "Sky"
} 

print("Type any one among the 5:")
print("1. Jaal\t\t 2. Vayu\t 3. Prithvi\t 4. Agni\t 5. Akash\n")
word = input("Enter the word you want meaning of: ")
print(words[word])