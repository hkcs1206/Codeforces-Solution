def convert(list):
     
    # Converting integer list to string list
    s = [str(i) for i in list]
     
    # Join list items using join()
    res = int("".join(s))
     
    return(int(res))
n = int(input())
if(n>0):
    print(n)
else:
    ls = list(str(n))
    if(int(ls[-1])>int(ls[-2])):
        ls.pop(-1)
        print(convert(ls))
    else:
        (ls.pop(-2))
        print(convert(ls))
