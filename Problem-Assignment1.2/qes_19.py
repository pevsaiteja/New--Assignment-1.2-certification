objects = {"python", "coding", "tips", "for", "beginners"}

# Print set.
print(objects)
print(len(objects)) 

# Use of "in" keyword.
if "tips" in objects:
 print("These are the best Python coding tips.")

# Use of "not in" keyword.
if "Java tips" not in objects:
 print("These are the best Python coding tips not Java tips.")

# ** Output
{'python', 'coding', 'tips', 'for', 'beginners'}
5

# *** Lets initialize an empty set
items = set()

# Add three strings.
items.add("Python")
items.add("coding")
items.add("tips") 

print(items)
