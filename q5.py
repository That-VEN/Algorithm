#Q1.display number 1 by one wihtout space
text = "3 4 5 6 "
for i in range(len(text)):
    if text[i] != " ":
        print(text[i])

#Q2. sum all number
sum =0
for i in range(len(text)):
    if text[i]!=" ":
        sum+=int(text[i])
print("Total: ",sum)