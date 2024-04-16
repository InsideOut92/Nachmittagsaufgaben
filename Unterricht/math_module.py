import math

x = math.sqrt(16)
print(x)

p = math.ceil(4.00300001)
o = math.floor(3.9979999)

print(p)
print(o)

print("normal gerundet")
p = round(p, 2)
o = round(o, 4)
print(p)
print(o)


print(math.pi)

i = 2
print(type(i))

pre_i = 0

# Python hat KEIN programmiertes Limit bei dieser Schleife
# => bricht ab, weil print() "nur" 4300 Zeichen auf einmal darstellen kann.

while i > pre_i:
    pre_i = i
    i += 1

    if i % 100 == 0:
        print(i)
