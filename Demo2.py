# Demo2.py

# List
fruits_list = ["apple", "banana", "orange", "pear"]
print("fruits_list:", fruits_list)

# Tuple
fruits_tuple = ("apple", "banana", "orange", "pear")
print("fruits_tuple:", fruits_tuple)

# Set
fruits_set = {"apple", "banana", "orange", "pear"}
print("fruits_set:", fruits_set)

# Accessing Elements
print("Accessing Elements:")
print("fruits_list[0]:", fruits_list[0])
print("fruits_tuple[1]:", fruits_tuple[1])
# Set has no order, so we can't access elements by index

# Adding Elements
print("\nAdding Elements:")
fruits_list.append("grape")
print("fruits_list:", fruits_list)
# Tuple is immutable, so we can't add elements to it
fruits_set.add("grape")
print("fruits_set:", fruits_set)

# Removing Elements
print("\nRemoving Elements:")
fruits_list.remove("orange")
print("fruits_list:", fruits_list)
# Tuple is immutable, so we can't remove elements from it
fruits_set.remove("orange")
print("fruits_set:", fruits_set)

# Length of Collection
print("\nLength of Collection:")
print("len(fruits_list):", len(fruits_list))
print("len(fruits_tuple):", len(fruits_tuple))
print("len(fruits_set):", len(fruits_set))
