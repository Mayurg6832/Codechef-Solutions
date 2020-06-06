for i in range(int(input())):
    n,k=map(int,input().split())
    lst=list(map(int,input().split()))
    sm=sum(lst)
    sm1=0
    for i in lst:
        if i<k:
            sm1+=i
        else:
            sm1+=k
    print(sm-sm1)
