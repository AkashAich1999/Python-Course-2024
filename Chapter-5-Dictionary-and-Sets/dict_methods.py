marks = {
    "Akash": 90,
    "Darshit": 95,
    "Manab": 93,
    0: "Akash Aich"
}

print(marks)

# Method 1
print(marks.items())

# Method 2
print(marks.keys())

# Method 3
print(marks.values())

# Method 4
marks.update({"Akash": 99, "Darshit": 100})
print(marks)

# Method 5
print(marks.get("Akash"))

# Method 6
print(marks.get("Akash"))
print(marks["Akash"])

print(marks.get("Akash1"))  # Prints None
print(marks["Akash1"])      # Returns An Error (KeyError)