def int_to_roman(num):
    integer = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5,4,1]
    roman  = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X','IX', 'V', 'IV', 'I']  #define the roman nummeral values to the integer

    roman_num = '' # Variable to store the resulting Roman numeral
    i = 0 # Index for values and symbols lists

    while num > 0:
    #Subtract the largest possible value from num and appen the corresponding symbol
        if num >= integer[i]:
            roman_num += roman[i] # Append the Roman numeral symbol
            num -= integer[i] # Subtract the corresponding value from num
        else:
            i += 1 # Move to the next index if the current value is too large for num
        
    return roman_num

number = int(input(""))
roman_number = int_to_roman(number)
print(roman_number)

