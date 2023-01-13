tc = [int(i) for i in input().split()]
if(sum(tc)%5==0 and sum(tc)!=0 ):
    print(int(sum(tc)/5))
elif(sum(tc)==0):
    print(-1)
else:
    print(-1)
