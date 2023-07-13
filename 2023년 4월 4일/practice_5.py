a = {'item1': 45.50, 'item2': 35, 'item3': 41.30, 'item4': 55, 'item5': 24}

sorted_a = sorted(a.items(), key=lambda x: x[1], reverse=True)

for i in range(3):
    print('(\'{}\' : {})'.format(sorted_a[i][0], sorted_a[i][1]), end=' ')
#2020112084 제보민