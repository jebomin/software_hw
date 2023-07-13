string_tuple = (('333', '22'), ('1414', '2323'))
int_tuple = tuple((int(x), int(y)) for x, y in string_tuple)
print(int_tuple)