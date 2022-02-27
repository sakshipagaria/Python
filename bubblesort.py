def bubble(a):
    n=len(a)
    
    for i in range(n):
        for j in range(0,n-i-1):
            if(a[j]>a[j+1]):
                tmp=a[j]
                a[j]=a[j+1]
                a[j+1]=tmp
                
                
a=[2,3,6,1,4]
bubble(a)

for i in a:
    print(i)
    
