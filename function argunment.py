def my_function(name,*mark,age,room,country="China",**detail):
    print("----------------------------------------")
    print("Student record")
    print("Name : ",name)
    print("Age : ",age)
    print("Country : ",country)
    print("Room.No : ",room)
    print("Subject1 Marks : ",mark[0])
    print("Subject2 Marks : ",mark[1])
    print("Subject3 Marks : ",mark[2])
    for key,value in detail.items():
        print(key,":" ,value)
    
    total=0
    for m in mark :
        print("",m)
        total =total+m
    print("Total marks : ",total)
    print("Positional argunment : ",name)
    print("Keyword argunment : ",age,",",room)
    print("Default argunment : ",country)
    print("Arbitraty argunment : ",mark)
    print("Arbitraty  keyword argunment : ",detail)
       
a=input("Enter name :")
b=input("Enter age : ")
c=input("Enter country : ")
d=input("Enter room number : ")
m1=int(input("Enter sub1 marks : "))
m2=int(input("Enter sub2 marks : "))
m3=int(input("Enter sub3 marks : "))
add=input("Enter address street : ")
cit=input("Enter city : ")

if c=="" :
    my_function(a,m1,m2,m3,age=b,room=d,country="China",Address=add,City=cit)
else :
    my_function(a,m1,m2,m3,age=b,room=d,country=c,Address=add,City=cit)
        
    
    