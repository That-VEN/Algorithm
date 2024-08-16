text = input(" Enter number: ")
for i in range(len(text)):
    if int(text[i])%2 ==1:
        print("Odd")
    else:
        print("Even")
    