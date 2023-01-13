n = int(input())
s = 0
tc = []
res = []
for i in range(n):
    a = [int(i) for i in input().split()]
    tc.append(a)
for j in range(n):
    s = s + tc[j][1] - tc[j][0]
    res.append(s)
print(max(res))
