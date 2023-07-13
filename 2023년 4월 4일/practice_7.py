arr = [1, 3, 5, 3, 7, 1, 9, 3]

seen = set()
for x in arr:
    if x in seen:
        print(x)
        break
    seen.add(x)
else:
    print("-1")
#2020112084 제보민
#1로 한게 아니라 3으로함