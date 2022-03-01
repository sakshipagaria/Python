L = [int(i) for i in input().split()]
print(uniqueE(L))

res=[]
def uniqueE(LL):
  for i in LL:
    if(LL.count(i)==1):
      if i not in res:
        res.append(i)
  res.sort()
  return res
