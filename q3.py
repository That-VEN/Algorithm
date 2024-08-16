text=input("Enter text: ")
isCapital = False
for i in range(len(text)):
    if text[i]==text[i].upper():
        isCapital = True
if isCapital:
    print("Yes")
else:
    print("NO")
    

                