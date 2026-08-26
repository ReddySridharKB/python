# Python String Operations

text = "Hello, World! It's a beautiful day"

print("\n--- Original String ---")
print(text)

# 1. Length
print("\nLength:", len(text))

# 2. Indexing
print("First character:", text[0])
print("Last character:", text[-1])

# 3. Slicing
print("First 5 characters:", text[:5])

# 4. Upper and lower
print("Uppercase:", text.upper())
print("Lowercase:", text.lower())

# 5. Strip spaces
print("Without extra spaces:", text.strip())

# 6. Replace
print("Replace spaces with -:", text.replace("a", "-"))

# 7. Split
words = text.split()
print("Words:", words)

# 8. Join
joined_text = "-".join(words)
print("Joined words:", joined_text)

# 9. Find
search = input("\nEnter a word to find: ")
print("Position:", text.find(search))

# 10. Check if word exists
print("Word exists:", search in text)

# 11. Startswith
print("Starts with 'Hello':", text.startswith("Hello"))

# 12. Endswith
print("Ends with '.':", text.endswith("."))

# 13. Count
character = input("Enter a character to count: ")
print("Character count:", text.count(character))

# 14. f-string
name = input("\nEnter your name: ")
age = int(input("Enter your age: "))

print(f"My name is {name} and I am {age} years old.")