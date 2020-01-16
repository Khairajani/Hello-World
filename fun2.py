a=list(map(int,input().split()))
b=sum(a)//len(a)
for i in range(0,len(a)):
    sum=sum+(a[i]-b)**2
print(sum)    
