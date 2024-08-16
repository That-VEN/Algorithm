for i in range(5):
    text=input("Enter number: ")
    max=0
    min=0
    for i in range(len(text)):
        if text[i]< max:
            max=text[i]
        elif text[i]<min:
            min=text[i]
print("max: ",max)
print("min: ",min)