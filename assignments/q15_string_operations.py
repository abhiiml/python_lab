# Question 15: String Operations on "Python Programming"

text = "Python Programming"
print("Initial Text:", text)

# 1) Display Python
print("1) Display Python:", text[0:6])

# 2) Display Programming
print("2) Display Programming:", text[7:])

# 3) Find if Java is there or not; if not, then include Java in between Python programming
if "Java" in text:
    print("3) Java is present")
else:
    text = text.replace("Programming", "Java Programming")
    print("3) After inserting Java:", text)

# 4) Find the length of the new string
print("4) Length of new string:", len(text))

# 5) Count the number of words in the string
print("5) Word count:", len(text.split()))

# 6) Capitalize each word in the string
print("6) Title case:", text.title())

# 7) Remove all the spaces and print the string
text_no_space = text.replace(" ", "")
print("7) Without spaces:", text_no_space)

# 8) Print the frequency of 'A', 'P', 'R' (case-insensitive search)
for ch in ['A', 'P', 'R']:
    count_upper = text.count(ch)
    count_lower = text.count(ch.lower())
    print(f"8) Frequency of '{ch}' (uppercase): {count_upper}, total ({ch}/{ch.lower()}): {count_upper + count_lower}")
