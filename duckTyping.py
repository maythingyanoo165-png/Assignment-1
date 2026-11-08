# -*- coding: utf-8 -*-
"""
Created on Sun Nov  8 21:50:05 2026

@author: Double-Y
"""

class Mon :
    def State(self) :
        print("Mon State places.")
        mon={
            "1." : "Thaton",
            "2." : "Mawlamying",
            "3." : "Kyaikkaw"}
        print(mon)
        print("Now,I live in Mon State,Kyaikkaw.")
        
    def Fruit() :
        print("Mon State Fruits.")
        mfru={
            "1." : "Durian",
            "2." : "Banana",
            "3." : "Watermelone"}
        print(mfru)
    
class Shan :
    def State(self) :
        print("Shan state places.")
        shan={
            "1." : "Taung Gyi",
            "2." : "Inn Lay",
            "3." : "Lin Kie"}
        print(shan)
        print("I want to live in Shan State ,Inn Lay in future.")
    def Fruit() :
        print("Shan State Fruits.")
        sfru={
             "1." : "Orange",
             "2." : "Avocado",
             "3." : "Strawberry"}
        print(sfru)  
 
def choice_state(state) :
    state.State()
def choice_fruit(fruit) :
    fruit.Fruit()
    

    
MON=Mon()
SHAN=Shan() 


    
choice_state(MON)
choice_state(SHAN) 
a=int(input("Choice 1 or 2(1. Mon State Fruits and 2.Shan State Fruits.) :")) 
if a==1 :
    mon_fruit=Mon()
    choice_fruit(Mon)
elif a==2 :
    shan_fruit=Shan()
    choice_fruit(Shan)
else :
    print("Invalide choice!")
    


    

    
         

    
    
      
        