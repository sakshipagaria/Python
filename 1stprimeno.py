L=[int (i) for i in  input().split()]]
def firstprime():
  for i in L:
    c=0
    for j in range(2,i):
      if(i%j==0):
        c=1
      if(c==0):
        print(i)
        return
      
firstprime()    
