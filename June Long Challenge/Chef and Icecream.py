def func():
    for i in range(n):
        if i==0:
            if lst[0]>6:
                return 'NO'
            coin[lst[0]]+=1
        else:
            if lst[i]==10:
                if coin[5]==0:
                    return 'NO'
                else:
                    coin[10]+=1
                    coin[5]-=1
            elif lst[i]==15:
                if coin[10]==0:
                    if coin[5]<2:
                        return 'NO'
                    else:
                        coin[5]-=2
                        coin[15]+=1
                else:
                    coin[10]-=1
                    coin[15]+=1
            else:
                coin[5]+=1
                    
    return 'YES'
            
            
for i in range(int(input())):
    coin={5:0,10:0,15:0}
    n=int(input())
    lst=list(map(int,input().split()))
    print(func())
