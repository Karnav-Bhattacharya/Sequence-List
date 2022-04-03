a = []

for i in range (1,100):
    if i%2==0:
        a.append(2*(i*i))
    else:
        a.append(i*i)

A = sum(a[:20])
B = sum(a[:40])

print(B-2*A)