sentence = input("Enter a sentence: ")

words = len(sentence.split())
characters = len(sentence)

lowercase = sentence.lower()
uppercase = sentence.upper()
underscores = sentence.replace(" ", "_")

print("Number of words:", words)
print("Number of characters:", characters)
print("Lowercase:", lowercase)
print("Uppercase:", uppercase)
print("Spaces replaced with underscores:", underscores)
