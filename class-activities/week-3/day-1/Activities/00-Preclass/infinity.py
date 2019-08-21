formular = input("Which math problem you want to solve?")
k = int(input("what is your k value?"))

result=0
if formular == "A":   
    for i in range(k):
        result = result+(1/(2**i))
elif formular == "B":
    if (k>0):
        for i in range(k):
            i+=1
            result = result+(1/i)
    else:
        result=0
print ("--------------------------------------") 
print (result)  