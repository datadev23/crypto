message = "This is a message"

# key

key = 13

mode = "encrypt"

LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

translated = ""


message = message.upper()

print(message)


for symbol in message:
    print symbol
    


    if symbol in LETTERS:
        num = LETTERS.find(symbol)
     
        if mode == "encrypt":
            print("encrypt");
            num = num + key

        if num >= len(LETTERS):
            num = num - len(LETTERS)
        elif num <= 0:
            num = num + len(LETTERS)    

        translated = translated + LETTERS[num]
    else:
        translated = translated + symbol



print(translated)
