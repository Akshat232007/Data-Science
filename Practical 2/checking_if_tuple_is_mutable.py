my_tuple = (10, 20, 30)

print("Original tuple:", my_tuple)
try:
    my_tuple[0] = 99
except TypeError:
    print("Error: You cannot change a tuple element! Tuples are immutable.")