with open('inputs/day25.txt') as f:
    pkey1, pkey2 = [int(x) for x in f.read().split('\n')]

c = 0
x = 1
while x != pkey1:
    x = (x * 7) % 20201227
    c += 1
    
print(pkey2**c % 20201227)