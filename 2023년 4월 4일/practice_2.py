my_tuple = (('333', '22'), ('1414', '2323'))
new_tuple = tuple((int(x), int(y)) for x, y in my_tuple)

print(new_tuple)
#2020112084 제보민