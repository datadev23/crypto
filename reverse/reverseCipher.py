message = "Three can keep a secret, if two of them are dead."
translated = ""

i = len(message) - 1
print(i)

while i >= 0:
    print(translated)
    translated = translated + message[i]
    i = i - 1


print(translated)
