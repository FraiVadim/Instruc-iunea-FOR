#in problema nu e precizat inclusiv b sau exclusiv , eu am facut inclusiv
a=eval(input(print("dati a: ")))
b=eval(input(print("dati b: ")))
for i in range (a,b,2):
    if i%2==0:
        print (i+1)
    else:
        print (i)

 