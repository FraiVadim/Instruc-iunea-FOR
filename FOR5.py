#intervalul de la a la b exclusiv
s=0
n=eval(input(print("dati numarul: ")))
for i in range (1,n,1):
    if (i%3==0) or (i%5==0):
        s+=i
print (s)
 