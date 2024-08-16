#Q1.Remove space and keep redsult ="3456"
text ="3 4 5 6"
result=""
for i in range(len(text)):
    if text[i]!=" ":
        result+=text[i]
print(result)

#Q2. Multiple each letter by 2 result ="6 8 10 12"
result=0
string=""
for i in range(len(text)):
    if text[i]!=" ":
        result=int(text[i])*2
        string+=str(result)+" "
print(string)