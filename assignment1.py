x=int(input("Give me your 1st number ="))
y=int(input("Give me your 2nd number ="))

all_x=id(x)
print("location of 1st number =",all_x)
hex_y=hex(y)
print("location of 2nd number =",hex_y)

n1= x + y
print("Answer of addition =",n1)
if x > y :
    n2= x - y
    print("Answer of subration =",n2)
    n3= x * y
    print("Answer of multiplaction =",n3)
    n4= x // y
    print("Answer of division =",n4)
    


else:
    n2=y - x
    print("Answer of subration =",n2)
    n3=x * y
    print("Answer of multiplication =",n3)
    n4= y // x
    print("Answer of division =",n4)


all_n1=id(n1)
print("location of n1 =",all_n1)
all_n2=id(n2)
print("location of n2 =",all_n2)
all_n3=id(n3)
print("location of n3 =",all_n3)
all_n4=id(n4)
print("location of n4 =",all_n4)


hex_n1=hex(n1)
print("location of n1 =",hex_n1)
hex_n2=hex(n2)
print("location of n2",hex_n2)
hex_n3=hex(n3)
print("location of n3",hex_n3)
hex_n4=hex(n4)
print("location of n4 =",hex_n4)    
    
    
    


