a = ['Red', 'Green', 'White', 'Black', 'Yellow', 'Pink', 'Blue']
b = ['Red', 'Green', 'Black', 'White', 'Yellow', 'Indigo', 'Blue']
answer = []
for i in a:
    if i not in b:
        answer.append(i)

for i in b:
    if i not in a:
        answer.append(i)
    
print(answer)
#2020112084 제보민