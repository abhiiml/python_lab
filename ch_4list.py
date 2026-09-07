# List operations demo
a = [1, 3, 5, 7, 12, 34]
print("Popped element at index 2:", a.pop(2))
a.insert(2, 2)
print("List after insertion:", a)

# Example: store fruits entered by user
fruits = []
# for i in range(1, 8):
#     fruit = input(f"Enter fruit {i}: ")
#     fruits.append(fruit)
# print("Fruits list:", fruits)

# Set operations demo
s1 = {1, 2, 3, 4}
s2 = {3, 4, 5, 6}
print("Union of s1 and s2:", s1.union(s2))

# Note: In Python, 1 == 1.0 is True, so a set stores only one of them
s = set()
s.add(1)
s.add(1.0)
s.add("1")
print("Set content:", s, "| Length:", len(s), "| Type:", type(s))