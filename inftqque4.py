string counter

def encode(message):
    message= message+'0'
    cnt=1
    op=''
    for i in range(len(message)):
        if message[i]=='0':
            break
        elif message[i]==message[i+1]:
            cnt += 1
        else:
            op+=str(cnt)+message[i]
            cnt=1
    return op
encoded_message=encode("KKKKSSBBTKK")
print(encoded_message)
