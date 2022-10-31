def create_largest_number(number_list):
    number_list.sort()
    number_list.reverse()
    op=''
    for i in number_list:
        op+=str(i)
    return int(op)
    #remove pass and write your logic here

number_list=[23,45,67]
largest_number=create_largest_number(number_list)
print(largest_number)
