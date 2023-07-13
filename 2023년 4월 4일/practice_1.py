my_list = [(10, 20, 30),(40,50,60),(70,80,90)]
new_value = 100

new_list = [tuple(lst[:-1]) + (new_value,) for lst in my_list]

print(new_list)
# 20202112084 제보민