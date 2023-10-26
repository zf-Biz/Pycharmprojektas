for a in range(1, 101, 1):
    if a == 21:
        break
    print(a)
print('----------')

for a in range(1, 101, 1):
    if a < 11:
        continue
    print(a)
print('----------')

for a in range(1, 101, 1):
    if (a % 2 == 0):
        continue
    if a > 20:
        break
    print(a)