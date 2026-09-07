name = input("enter your name: ")
print(f"good afternoon {name}")  # fstring

# find double space
text = input("enter a string: ")
print("double space is at index:", text.find("  "))

sample = "im   going  out today"
print("Original string:", sample)
print("Double space index:", sample.find("  "))

# replace double space with single space
cleaned = sample.replace("  ", " ")
print("After replacing double space:", cleaned)