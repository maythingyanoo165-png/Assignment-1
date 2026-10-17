n1=int(input("Give me 1st number ="))
n2=int(input("Give me 2nd number ="))
n3=input("Give me your function(+,-,*,/) =")

all_n1=id(n1)
print("location of 1st number =",all_n1)
hex_n1=hex(n1)
print("location of 1nd number =",hex_n1)

all_n2=id(n2)
print("location of 2nd number =",all_n2)
hex_n2=hex(n2)
print("location of 2nd number =",hex_n2)



def add(n1,n2):
    print(n1+n2)
    
def sub(n1,n2):
    if n1>n2:
        print(n1-n2)
    elif n1<n2 :
        print(n2-n1)
        
def mul(n1,n2) :
    print(n1*n2)
    
def div(n1,n2) :
    if n2 !=0: 
        print(n1/n2)
    elif n2==0 :
        print("Cannot divided by 0")
        
        
    
if n3 == "+":
    add(n1,n2)
    
elif n3 =="-":
    sub(n1,n2)
    
elif n3=="*" :
    mul(n1,n2)
    
elif n3=="/" :
    div(n1,n2)

    

    

    
