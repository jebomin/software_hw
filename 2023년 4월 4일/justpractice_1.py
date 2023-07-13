# Define the list of tuples
my_list = [('item1', 10.5), ('item2', 11.8), ('item3', 9.1), ('item4', 7.3)]

# Define a function that returns the float element of a tuple
def get_float(t):
    return t[1]

# Sort the list of tuples by the float element using the defined function
my_list.sort(key=get_float)

# Print the sorted list of tuples
print(my_list)