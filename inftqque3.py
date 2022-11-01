#palindrom

def check_palindrome(word):
    x=word[::-1]
    if x==word:
        return True
    else:
        return False
    #Remove pass and write your logic here

status=check_palindrome("sakshi")
if(status):
    print("word is palindrome")
else:
    print("word is not palindrome")
