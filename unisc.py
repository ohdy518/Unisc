o = input("Enter string to encrypt: ")
l = []
m = 0
n = 0
f = ""
for i in o:
    l.append(ord(i))
    f += str(ord(i) ** 2)
for i in l:
    m += i
f += str(m)
m = 0
for i in l:
    m *= i
f += str(m)
m = 0
for i in f:
    m += int(i)
    n *= int(i)
f += str(m)
f += str(n)
f += str(m * n)
m = 0
m = int(f)
f += str(m * (m + 1) - 1 ** int(f[0]))
m = 0
for i in f:
    m += int(f)
f += str(m ** 3)
f += str(m)
print(f)