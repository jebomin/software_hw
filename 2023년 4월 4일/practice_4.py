dic1 = {'a': 100, 'b': 200, 'c': 300}
dic2 = {'a': 200, 'b': 100, 'd': 400}

dic3 = {}

for key in dic1.keys():
    if key in dic2:
        dic3[key] = dic1[key] + dic2[key]
    else:
        dic3[key] = dic1[key]

for key in dic2.keys():
    if key not in dic1:
        dic3[key] = dic2[key]

print(dic3)
#2020112084 제보민