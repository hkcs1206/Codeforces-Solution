n = int(input())
count = 0
for i in range(n):
    tc = [int(i) for i in input().split()]
    if(tc.count(1)>=2):
        count+=1
print(count)
