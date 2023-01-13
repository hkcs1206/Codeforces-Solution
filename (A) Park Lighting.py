n = int(input())
for i in range(n):
    a,b = map(int,input().split())
    if((a*b)%2==0):
        print(int(a*b/2))
    else:
        print(a*b//2 + 1)
