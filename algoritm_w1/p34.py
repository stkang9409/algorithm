total_h = 0
people_h = []
for _ in range(9):
    person_h = int(input())
    total_h += person_h
    people_h.append(person_h)

target = total_h - 100
people_h.sort()
i, j = 0, 8
while i != j:
    if people_h[i]+people_h[j] < target:
        i += 1
    elif people_h[i]+people_h[j] > target:
        j -= 1
    else:
        people_h.pop(i)
        people_h.pop(j-1)
        break

for i in people_h:
    print(i)
