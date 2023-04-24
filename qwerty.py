keyboard = '`1234567890-=qwertyuiop[]\\asdfghjkl;\'zxcvbnm,./'

while True:
    string = input().strip()
    if string == '':
        break
    decoded_line = ''
    for char in string:
        if char == ' ':
            decoded_line += ' '
        else:
            index = keyboard.index(char.lower())
            decoded = index - 1
            decoded = keyboard[decoded]
            if char.isupper():
                decoded = decoded.upper()
            decoded_line += decoded
    print(decoded_line)
