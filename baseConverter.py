def askTheUser():
    while True:
        message = input("To convert decimal to binary: Enter 'd2b'\nTo convert binary to decimal: Enter 'b2d'\nTo convert binary to hexadecimal: Enter 'h2b'\nTo simply terminate execution of this program: Enter 'quit'\n> ")
        if message.lower() == 'd2b':
            number = input("\nEnter the number to be converted: ")
            if number == 'quit':
                continue
            print(f"\nNumber to be converted: {number}\nTranslated to Binary Notation: {decimalToBinary(int(number))}")
            break
        elif message.lower() == 'b2d':
            number = input("Enter the number to be converted: ")
            if number == 'quit':
                continue
            print(f"\nNumber to be converted: {number}\nTranslated to Decimal Notation: {binaryToDecimal(int(number))}")
            break
        elif message.lower() == 'h2b':
            number = input("\nPlease beware that the number should be entered in groups of 4-bits. For example - '0100' or '100101001001'.\n\nEnter the number to be converted: ")
            if number == 'quit':
                continue
            if len(number) % 4 != 0:
                print("Please type the binary number in groups of 4-bits. Try again")
                break
            print(f"\nNumber to be converted: {number}\nTranslated to Hexadecimal Notation: {binaryToHex(number)}")
            break
        elif message.lower() == 'quit':
            print("\nThank you for using my converter. Have a great day :)")
            break
        else:
            print("\nInvalid input, please try again!\n")


def decimalToBinary(val):
    constructed = ''
    i = 16
    if val >= 2 ** i:
        return "Number is too large for accurate conversion! Try again with a smaller value."
    while i > 0:
        if val < 2 ** i and val >= 2 ** (i - 1):
            val -= 2 ** (i - 1)
            constructed += '1'
        else:
            constructed += '0'
        i -= 1
    return f"0b{constructed[constructed.index('1')-1:-1]}"
    

def binaryToDecimal(val):
    constructed = 0
    for i in range(len(str(val))):
        if str(val)[-1-i] == '1':
            constructed += 2 ** i
    return constructed


hexNotation = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
def binaryToHex(val):
    val = val + '0'
    hexConstructed = ''
    i = 0
    while i < len(val)-1:
        fourBitDecimalConstructed = 0
        bitwise = val[-5-i:-1-i]
        for j in range(4):
            if bitwise[-1-j] == '1':
                fourBitDecimalConstructed += 2 ** j
        hexConstructed = hexNotation[fourBitDecimalConstructed] + hexConstructed
        i += 4
    return hexConstructed