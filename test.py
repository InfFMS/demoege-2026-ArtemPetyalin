'''
a = int(input())
b = bin(a)

if a % 3 == 0:
    c = str(b)[2:] + str(b)[-3:]

else:
    d = bin((a % 3) * 3)
    c = str(b)[2:] + str(d)[2:]

print(c)
e = 0

for i in range(len(c)):
    e += int(c[-i - 1]) * (2 ** i)

print(e)


задание 5
'''
a = 1024*768*(2**30)
b = 800*600*(2**28)
c = (a-b)*100
print(a)
print(b)
print(a-b)
print(c)
print(c / 8 / 1024)

