def intersection(list1,list2):
    list=[values for values in l1 if values in l2]              #value is stmnt, and rest is for loop and if condition
    return(list)
  l1=[1,2,3,33,28,4]
  l2=[33,2,1]
  l3=intersection(l1,l2)
  print("Interesection of list1 :{} and list2: {} is {}".format(l1,l2,l3))
