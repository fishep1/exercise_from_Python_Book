num = []
for i in range(1, 1000001):
    num.append(i)
print(min(num))
print(max(num))
print(sum(num))

num1 = []
for i in range(1, 21, 2):
    num1.append(i)
print(num1)


num2 = []
for i in range(3, 30):
    if i % 3 == 0:
        num2.append(i)
print(num2)

num3 = []
for i in range(1,11):
    num3.append(i**3)
print(num3)

num4 = [i**3 for i in range(1, 11)]
print(num4)