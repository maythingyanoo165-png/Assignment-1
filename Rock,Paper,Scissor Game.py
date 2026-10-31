import random

choice=["rock","paper","scissor"]
print("Welcome to rock,paper,scissor Game!")
print("Display game winning rules are following.")
print("Rock Vs Paper -> Papper is winning.")
print("Rock Vs Scissor -> Rock is winning.")
print("Papper Vs Scissor -> Scissor is winning.")
x=100
print("You have",x,"Coins.")
while True:
   c=input("Enter your choice(rock or paper or scissor) or stop :").strip()
   if c=="stop"  :
        print("Thanks for playing game.")
        break
   elif c not in choice:
        print("Please! Retry your choice.")
        continue
   computer=random.choice(choice)
   print("Computer choice:",computer)    
   if c==computer:
    print("It's tie!")
    ans=input("Do you want to play again?(y/n):")
    if ans.lower()=='n':
        print("Thanks for playing game.")
    else:
        continue
   elif ((c=="papper" and computer=="rock") or (c=="rock" and computer=="scissor") or (c=="scissor" and computer=="paper")):
    print("You Win!")
    print("You get 10 Coins.")
    print("Yours currently Coins are" ,x+10, "Coins.")
   
    ans=input("Do you want to play again?(y/n):")
    if ans.lower()=='n':
        print("Thanks for playing game.")
        break
    else:
        continue
   else :
    print("Computer Win!")
    print("You lose 5 Coins.")
    print("Yours currently Coins are",x-10,"Coins.")
      
    ans=input("Do you want to play again?(y/n):")
    if ans.lower()=='n':
        print("Thanks for playing game.")
        break
    else:
        continue
    break




    