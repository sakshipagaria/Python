def remove_word(list1,word,num):
    count =0    #count the occurence of the word
    index=0     #count where we are currently
    
    for i in list1:
        index+=1
        if i==word:
            count+=1
            if count ==num:
                list1.pop(index-1)         #indexing starts  from 0
                
                
    return  list1
  l1=["hi","hello","my","he","my","she","we","my"]
  w="my"
  o=2
  print("Original list= ",l1)
  l1=remove_word(l1,w,o)
  print("List")
