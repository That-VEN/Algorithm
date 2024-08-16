# Q1.Count odd and even number in text
text = "454639"
countOdd = 0
countEven = 0
for i in range(len(text)):
    if i%2 ==1:
        countOdd +=1
    elif i%2 ==0:
        countEven +=1
print(countOdd)
print(countEven)

# Q2.Sum all number
text = "454639"
sum=0
for i in range(len(text)):
        sum +=int(text[i])
print(sum)

# Q3.Sum only even number
text="454639"
sum = 0
for i in range(len(text)):
    if int(text[i])%2==0:
        sum +=int(text[i])
print(sum)

# Q4. Reverse
text= "454639"
result = ""
lastIndext = len(text)-1
for i in range(len(text)):
        result += text[lastIndext-i]
print(result)

