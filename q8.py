#Q1. How many nunber 8 in string
text="9394884039"
count=0
for i in range(len(text)):
    if text[i]=="8":
        count+=1
print(count)

#Q2. what is first index of letter 8
isFound=False
for i in range(len(text)):
    if text[i]=="8"and not isFound == True:
        print("index letter 8: ",i)
        isFound = True    