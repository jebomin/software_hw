s = "a1a2a3a4a5"
numbers = []

for c in s:
    if c in '0123456789':
        numbers.append(int(c))

print(numbers)
#2020112084 제보민