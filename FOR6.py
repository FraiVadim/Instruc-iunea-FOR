s1=0
s2=0
s3=1
s4=0
s5=0
s6=3
z=1
n=eval(input(print("dati n: ")))
for i in range(1,n+1,1):
    s1+=i
print ("s1=",s1)
i=0

n=eval(input(print("dati n: ")))
for i in range(1,n+1,1):
    s2+=i*(i+1)
print ("s2=",s2)
i=0

n=eval(input(print("dati n: ")))
for i in range(1,n+1,1):
    z=z*i
i=0
print(z)
x=z
for i in reversed(range(1,n+1,1)):
    z=z/i
    x=x+z
    s3=x-1
print ("s3=",s3)
i=0

n=eval(input(print("dati n: ")))
for i in range(1,n+1,1):   
    s4=s4+((10*i)+2)
print ("s4=",s4)
i=0

n=eval(input(print("dati n: ")))
for i in range(1,n+1,1):
    s5+=i/(i+1)
print ("s5=",s5)
i=0

#s6=1+2+22+23+24+…+2n asa era scris
n=eval(input(print("dati n: ")))
for i in range(2,n+1,1):
    s6+=i+20
print ("s6=",s6)
i=0 