import webbrowser 
def engsongs():
        engsong={
            "1." : "https://www.youtube.com/watch?v=XGaMFQ2Oyuw&list=RDXGaMFQ2Oyuw&start_radio=1",
            "2." : "https://www.youtube.com/watch?v=NC_uA2MIy5Y&list=RDNC_uA2MIy5Y&start_radio=1",
            "3." : "https://www.youtube.com/watch?v=R4ISi7uRezc&list=RDR4ISi7uRezc&start_radio=1",
            "4." : "https://www.youtube.com/watch?v=neZAmN9bf1s&list=RDneZAmN9bf1s&start_radio=1",
            "5." : "https://www.youtube.com/watch?v=CTyeb5S0l9w&list=RDCTyeb5S0l9w&start_radio=1"}
        while True : 
           n1=int(input("You : Choice a number for song between 1 to 5 : "))
           if n1==1 :
               print("Bot : Bird of feather.")
               print("      Do you want to know this song overview?")
               b=input("You : ").lower()
               if "yes" in b or "yet" in b or "okay" in b :
                   print("Artist : Billie Eilish\nSongwriters : Billie Elish & Finneas O'Connell\nProducer : FINNEAS\nRelease Date : May 17,2024(Album: Hit Me Hard and Soft)\nGenre : Indie Pop/Synth-Pop")
                   print("Bot : Do you want to know thid song Themes & Meaning? ")
                   b1=input("You : ").lower() 
                   if "yes" in b1 or "yet" in b1 or "okay" in b1 :
                       print("->Deep Devotion : Inspired by the idiom 'Bird of feather flock together,' it explores an unconditional, deep connection with someone.")
                       print("->Everlasting Love : The lyrics express wanting to stay together until the very end('till the day that I die').")
                       print("->Mood : Upbeat and catchy shnth-pop melody comined with emotionally vulnerable lyric.")
                       print("Bot : Do you want to listen this song ?")
                       b2=input("You : ").lower()
                       if b2=="yes" :
                          
                           webbrowser.open(engsong["1."])
                           break
           elif n1==2 :
               print("Bot : Dandeline.")
               print("      Do you want to know this song overview? ")
               d=input("You : ").lower()
               if "yes" in d or "yet" in d or "okay" in d :
                   print("Artist : Ruth B.\nSongwriter : Ruth Berhe(Ruth B.)&Eric Frederic(Ricky Reed)\nRelease Date : April 28,2017(Album: Safe Haven)\nGenre : Pop/Piano Pop")
                   print("Bot : Do you want to know thid song Themes & Meaning? ")
                   d1=input("You : ").lower() 
                   if "yes" in d1 or "yet" in d1 or "okay" in d1 :
                       print("->Hopeful Romance : The song uses the tradition of blowing dandelion seeds and making a wish to portray deep,romantic feelings for a crush.")
                       print("->Pure&Innocent Love : It captures the magical,flutttering feeling of falling in love and wishing for that special person to be yours forever.")
                       print("->Mood : Melodic, dreamy piano accompaniment paired with sweet and catchy vocals.")
                       print("Bot : Do you want to listen this song ?")
                       d2=input("You : ").lower()
                       if d2=="yes" :
                          
                           webbrowser.open(engsong["2."])
                           break
           elif n1==3 :
               print("Bot : Ghost")
               print("      Do you want to know this song overview? ")
               g=input("You : ").lower()
               if "yes" in g or "yet" in g or "okay" in g :
                   print("Artist : Justin Bieber\nSongwriters : Justin Bieber,Jon Bellion,Jordan K.Johson,Stefan Johnson, and Michael Pollack\nRelease Date : September 10,2021(Album : Justice\nGenre : Pop/Synth-pop")
                   print("Bot : Do you want to know thid song Themes & Meaning? ")
                   g1=input("You : ").lower() 
                   if "yes" in g1 or "yet" in g1 or "okay" in g1 :
                       print("->Loss and Grief : The song explores the paingof losing someone you love, whether through death or separation, and coping with the sudden absence of that person in your life.")
                       print("->Enduring Connection : It expresses the feeling that even when someone is gone,their memory and the bond you shared remain like a 'ghost' that provides comfort, longing, and a desire to hokd onto the past.")
                       print("->Mood : Upliftinpg, acoustic-driven pop prlduction paired with emotional, refleective lyrics.")
                       print("Bot : Do you want to listen this song ?")
                       g2=input("You : ").lower()
                       if g2=="yes" :
                           
                           webbrowser.open(engsong["3."])
                           break
           elif n1==4 :  
               print("Bot : Playdate.")
               print("      Do you want to know this song overview? ")
               p=input("You : ").lower()
               if "yes" in p or "yet" in p or "okay" in p :
                   print("Artist : Melanie Martinez\nSongwriters : Melanie Martinez&Jennifer Decilveo\nRelease Date : August 14,2015(Alhum : Cry Baby Deluxe Edition)")
                   print("Bot : Do you want to know thid song Themes & Meaning? ")
                   p1=input("You : ").lower() 
                   if "yes" in p1 or "yet" in p1 or "okay" in p1 :
                       print("->Unerquited Feelings&Attachment : It depicts a relationship where one person feels treated merely as a casual pastime('play date'),yet cannot help falling for the other person anyway.")
                       print("->Pride vs. Vulnerability : The narrator pretends not to care to protect their feelings,while secretly longing for the other person's full attention and affection.")
                       print("->Mood : Catchy, playful beat juxtaposed with bittersweet, hesitant emotional struggle.")
                       print("Bot : Do you want to listen this song ?")
                       p2=input("You : ").lower()
                       if p2=="yes" :
                          
                           webbrowser.open(engsong["4."])
                           break
           elif n1==5 :
               print("Bot : Blue.")
               print("      Do you want to know this song overview? ")
               b=input("You : ").lower()
               if "yes" in b or "yet" in b or "okay" in b :
                   print("Artist : Yung Kai\nSongwriters : Yung Kai(Kia Sun)\nRelease Date : July 12,2024(as an independent single) ")
                   print("Bot : Do you want to know thid song Themes & Meaning? ")
                   b1=input("You : ").lower() 
                   if "yes" in b1 or "yet" in b1 or "okay" in b1 :
                       print("->Endless Devotion&Romantic Longing : The song captures the feeling of falling deeply in love with someone and wanting to spend every single moment by their side. It speaks about finding a sense of peace and home in snother person. ")
                       print("->Warm and Nostalgic Vibe : Driven by gentle acoustic guitar melodies, the track blends a soothing, dreamy atmosphere with heartfelt, emotional lyric about treasuring a special relationship.")
                       print("->Mood : Sweet, romantic, and deeply comforting.")
                       print("Bot : Do you want to listen this song ?")
                       b2=input("You : ").lower()
                       if b2=="yes" :
                           
                           webbrowser.open(engsong["5."])
                           break
                
                     
                                
               else :
                  n1=int(input("You : Choice a number for song between 1 to 5 : "))
                  continue 
def myansongs() :
        myansong={
            "1.": "https://www.youtube.com/watch?v=BfEYxHA-MD4&list=RDBfEYxHA-MD4&start_radio=1",
            "2.": "https://www.youtube.com/watch?v=nv9OGXAnDdY&list=RDnv9OGXAnDdY&start_radio=1",
            "3.":"https://www.youtube.com/watch?v=eMywPJw6PhE&list=RDeMywPJw6PhE&start_radio=1",
            "4.": "https://www.youtube.com/watch?v=rWRFAf6-yQE&list=RDrWRFAf6-yQE&start_radio=1",
            "5.": "https://www.youtube.com/watch?v=cNf0O51365M&list=RDcNf0O51365M&start_radio=1"}
        while True : 
           n2=int(input("You : Choice a number for song between 1 to 5 : "))
           if n2==1 :
               print("Bot : A Phay Nae A May Nay Tae Eain.")
               print("      Do you want to know this song overview?")
               a=input("You : ").lower()
               if "yes" in a or "yet" in a or "okay" in a :
                   print("Artist : Linn Linn\nGener : Myanmar Acoustic/Folk Pop/Rock")
                   print("Bot : Do you want to know thid song Themes & Meaning? ")
                   a1=input("You : ").lower() 
                   if "yes" in a1 or "yet" in a1 or "okay" in a1 :
                       print("->Longing fo Parents and Childhood Home : The song expresses a deep, nostalgic longing for one's parents still live.")
                       print("->The Comfort of Family : It portrays the bittersweet feeling of being away from home, working or struggling in the city, and yearning for the unconditional love, warmth, and peace found only under the parents' roof.")
                       print("->Mood : Emotional, heartfelt, and deeply reflective.")
                       print("Bot : Do you want to listen this song ?")
                       a2=input("You : ").lower()
                       if a2=="yes" :
                           
                           webbrowser.open(myansong["1."])
                           break
                      
           elif n2==2:
               print("Bot : To 1970 .")
               print("      Do you want to know this song overview?")
               t=input("You : ").lower()
               if "yes" in t or "yet" in t or "okay" in t :
                   print("Artist : Thar Ko\nGenre : Myanmar Pop/ Acoustic Ballad")
                   print("Bot : Do you want to know this song Themes & Meaning? ")
                   t1=input("You : ").lower() 
                   if "yes" in t1 or "yet" in t1 or "okay" in t1 :
                       print("->Nostalgia for a bygone Era : The song addresses the year 1970 as a metaphorical destination, expressing a deep longing for the simplicity, warmth, and innocence of past romance and old-school charm.")
                       print("->Timeless Affection & Memory : It refkects on how feelings of love remain unchanged despite the passage of time and shifting eras, blending sweet memories with a subtle, reflective sadmess.")
                       print("->Mood : Mellow, soulful, and deeply nostalgic.")
                       print("Bot : Do you want to listen this song ?")
                       t2=input("You : ").lower()
                       if t2=="yes" :
                          
                           webbrowser.open(myansong["2."])
                           break
                       
           elif n2==3 :
                   print("Bot : 1990.")
                   print("      Do you want to know this song overview?")
                   s=input("You : ").lower()
                   if "yes" in s or "yet" in s or "okay" in s :
                       print("Artist : Shine\nGenre : Myanmar Pop/Acoustic Ballad")
                       print("Bot : Do you want to know thid song Themes & Meaning? ")
                       s1=input("You : ").lower() 
                       if "yes" in s1 or "yet" in s1 or "okay" in s1 :
                           print("->Father-Son bond : The song beautifully portrays the deep emotional connection and bond between a father and his son. Ayoung man in the present 2020s era refkects on amd pays tribute to his father's youth from back around the 1990s.")
                           print("->Comparing Youthful Experiences : When the son faces modern-day hardships, strugggles, and moments of despair, he wonders empathetically : 'How did Dad emdure when he was my age?What dreams was he striving for?' It's a heartfelt questioning and deep understanding of his feather's journey.")
                           print("->Nostalgia for the 1990s : It captures a sense of longing for the simplicity, lifestyle, and mindset of young people during the 1990 era.")
                           print("Bot : Do you want to listen this song ?")
                           s2=input("You : ").lower()
                           if s2=="yes" :
                             
                              webbrowser.open(myansong["3."])
                              break
                           
                                 
           elif n2==4 :
                   print("Bot : Wann Nae Tat tae Chit Thu.")
                   print("      Do you want to know this song overview?")
                   w=input("You : ").lower()
                   if "yes" in w or "yet" in w or "okay" in w :
                       print("Artist/Band : Idiots(Vacals/Songwriting by Raymon)\nGenre : Myanmar Rock / Acoustic Ballad")
                       print("Bot : Do you want to know thid song Themes & Meaning? ")
                       w1=input("You : ").lower() 
                       if "yes" in w1 or "yet" in w1 or "okay" in w1 :
                           print("->Comfort and Reassurance : The song is dedicated to a partner who easily feels down, discouraged, or brought to tears by life's difficulties and hardships. It offers deep emotioname support with the comforting reassurance : 'Rest your head om my shoulder,' promising a constant, protective presence by their side.")
                           print("->Strength and Hope : It emphasizes standing together through the darkest days, emcouraging each other never to let go,and continuing the journey hand-in-hand toward to future.")
                           print("Mood : Deeply comforting, affectionate, and carrying the signature emotional depth of a heartfelt rock ballad.")
                           print("Bot : Do you want to listen this song ?")
                           w2=input("You : ").lower()
                           if w2=="yes" :
                             
                              webbrowser.open(myansong["4."])
                              break
                           
           elif n2==5 : 
                   print("Bot : Chan Khae.")
                   print("      Do you want to know this song overview?")
                   c=input("You : ").lower()
                   if "yes" in c or "yet" in c or "okay" in c :
                       print("Artist / Band : Idiots (Songwriting & Vacals by Raymon /Raymond-Wai Mon Oo)")
                       print("Bot : Do you want to know thid song Themes & Meaning? ")
                       c1=input("You : ").lower() 
                       if "yes" in c1 or "yet" in c1 or "okay" in c1 :
                           print("->Selfless Sacrifice and Letting Go : The song explores the painful decision of walking away from a loved one . Feeling inadequate or seeing oneself as having no ffuture, ghe narrator chooses to step back purely for the sake of the patner's brighter future rather than becoming an obstacle or burden.")
                           print("->Self-Deprecation and Heartbreak : It capture deeply emotional introspection-wondering why the partner should sacrifice for someone who feels they weren't good enough. It speaks sf cutting ties with a heavy heart and accepting the end of the past.")
                           print("->Final Farewell and Hope : It serves as a heartbreaking goodbye song, sfffering a clean break while quietly wishing for a possible reunion in another time or place.")
                           print("->Mood : Melancholic, deeply sorrowful, and carrying the signature emotional intensity of a classic Myanmar rock ballad.")
                           print("Bot : Do you want to listen this song ?")
                           c2=input("You : ").lower()
                           if c2=="yes" :
                               
                               webbrowser.open(myansong["5."])
                               break
                          
                
           else : 
                  n2=int(input("You : Choice a number for song between 1 to 5 : "))
                  continue 
def cortis () :
        cortissongs={
            "1." : "https://www.youtube.com/watch?v=cVMgSbZpm8E&list=RDcVMgSbZpm8E&start_radio=1",
            "2." : "https://www.youtube.com/watch?v=uNZuEDLOjFo&list=RDuNZuEDLOjFo&start_radio=1",
            "3." : "https://www.youtube.com/watch?v=scjk5z2plBg&list=RDscjk5z2plBg&start_radio=1",
            "4." : "https://www.youtube.com/watch?v=NZ5Dn5_77rY&list=RDNZ5Dn5_77rY&start_radio=1",
            "5" : "https://www.youtube.com/watch?v=Q2uhkb8rQqI&list=RDQ2uhkb8rQqI&start_radio=1"}
        while True : 
            n3=int(input("You : Choice a number for song between 1 to 5 : "))
            if  n3==1 :
                print("Bot : What you want.")
                print("      Do you want to know this song overview?")
                cor=input("You : ").lower()
                if "yes" in cor or "yet" in cor or "okay" in cor :
                    print("Artist : Cortis\nGenre : Rap Rock / Paychedelic Rock / Alt-Pop")
                    print("Bot : Do you want to know thid song Themes & Meaning? ")
                    cor1=input("You : ").lower() 
                    if "yes" in cor1 or "yet" in cor1 or "okay" in cor1 :
                        print("->Pursuit of Ambition and Dreams : The song serves as an emergetic anthem about fearlessly pursuing one's desires whether it is success, recognition, freedom, or passion without settling for mediocrity or being held back by limitations.")
                        print("->Youthful Energy and Rebellion : It captures the raw drive of youth, breaking away from conventional expectations to push forward, see the world, and make their own mark on it.")
                        print("->Mood : Energetic, rebellious,blod, and empowering.")
                        print("Bot : Do you want to listen this song ?")
                        cor2=input("You : ").lower()
                        if cor2=="yes" :
                           
                            webbrowser.open(cortissongs["1."])
                            break
            elif  n3==2 :
                print("Bot : Joyride.")
                print("      Do you want to know this song overview?")
                j=input("You : ").lower()
                if "yes" in j or "yet" in j or "okay" in j :
                    print("Artist : Cortis\nGenre : Alternative Rock / Indie Pop / Pop-Rock")
                    print("Bot : Do you want to know thid song Themes & Meaning? ")
                    j1=input("You : ").lower() 
                    if "yes" in j1 or "yet" in j1 or "okay" in j1 :
                        print("->Spontaneous Freedom & Escaping Routine : The song captures the thrill of breaking away from a monotonous routine, stress, and feeling trapped, turning life into an exciting and freeing ride.")
                        print("->Youth Spontaneity & Breaking Rules : It reflects the reckless, daring energy of youth-leaving behind strich rules and expectations('goody-two-shoes' habits), throwing away the map, and speeding up to enjoy the night with friends.")
                        print("->Mood : High-energy, rebellious, thrilling, and uplifting.")
                        print("Bot : Do you want to listen this song ?")
                        j2=input("You : ").lower()
                        if j2=="yes" :
                            
                            webbrowser.open(cortissongs["2."])
                            break
                           
            elif  n3==4 :
                print("Bot : Go!.")
                print("      Do you want to know this song overview?")
                g=input("You : ").lower()
                if "yes" in g or "yet" in g or "okay" in g :
                    print("Artist : Cortis\nGenre : Hip-Hop / Rap Rock / Alt-Pop")
                    print("Bot : Do you want to know thid song Themes & Meaning? ")
                    g1=input("You : ").lower() 
                    if "yes" in g1 or "yet" in g1 or "okay" in g1 :
                        print("->Fearless Momentum & Self-Reliance : The song is a high-energy anthem about pushing forward toward goals without waiting for external validation or permission. It emphasizes charging ahead on one's own terms with green light ahead.")
                        print("->Unstoppable Creativity & Ambition : It showcases a relentless drive to create fresh beats, break out of old molds, and estanlish a mew era of music and self-expression.")
                        print("->Mood : High-energy, confident, driving, and empowering.")
                        print("Bot : Do you want to listen this song ?")
                        g2=input("You : ").lower()
                        if g2=="yes" :
                            
                            webbrowser.open(cortissongs["4."])
                            break
            elif  n3==3 :
                print("Bot : RedRed.")
                print("      Do you want to know this song overview?")
                red=input("You : ").lower()
                if "yes" in red or "yet" in red or "okay" in red :
                    print("Artist : Cortis\nGenre : Rap Rock / Alt-Pop / Alternative")
                    print("Bot : Do you want to know thid song Themes & Meaning? ")
                    red1=input("You : ").lower() 
                    if "yes" in red1 or "yet" in red1 or "okay" in red1 :
                        print("->Passion & High Intensity : The song uses the color red as a symbol for intense passion, raw adrenaline, and overwhelming emotion, driving the energy of the track forward.")
                        print("->Unapologetic Self-Expression : It captures the feeling of standing out boldly, cutting through ghe noise, and refusing to blend into the background.")
                        print("->Mood : Bold, intinse, hihg-energy, and captivating.")
                        print("Bot : Do you want to listen this song ?")
                        red2=input("You : ").lower()
                        if red2=="yes" :
                            webbrowser.open(cortissongs["3."])
                            break
            elif  n3==5 :
                print("Bot : FaShion.")
                print("      Do you want to know this song overview?")
                f=input("You : ").lower()
                if "yes" in f or "yet" in f or "okay" in f :
                    print("Artist : Cortis\nGenre :Hip-Hop / Alternative Pop / Rap Rock")
                    print("Bot : Do you want to know thid song Themes & Meaning? ")
                    f1=input("You : ").lower() 
                    if "yes" in f1 or "yet" in f1 or "okay" in f1 :
                        print("->Redefinging Style & Authenticity : The song subverts traditional luxury standards, proudly embracing vintage finds, thrift culture (such as local spots like Domgmyo), and affordable streetwear to define true personal style on one's own terms.")
                        print("->Confidence & Creative Owership : It emphasizes an unbothered, rebellious attitude-Turning ordinary or unconventional clothing choices into a blod statement with the core message : 'I make them famous, I call that, fashion.'")
                        print("->Mood : Trenddy, energetic, confident, and playfullly rebellious.")
                        print("Bot : Do you want to listen this song ?")
                        f2=input("You : ").lower()
                        if f2=="yes" :
                            webbrowser.open(cortissongs["5."])
                            break
            else :
                n3=int(input("You : Choice a number for song between 1 to 5 : "))
                continue     
def cal():
       n1=int(input("Give me 1st number ="))
       n2=int(input("Give me 2nd number ="))
       n3=input("Give me your function(+,-,*,/) =")
       if n3== "+":
           print("Answer :",n1+n2)
       elif n3=="-" and n1>n2:
           print("Answer : ",n1-n2)
       elif n3=="-" and n1<n2 :
           print("Answer : ",n2-n1)
       elif n3=="*" :
           print("Answer : ",n1*n2)
       elif n3=="/" and n2!= 0 :
           print("Answer : ",n1/n2)
       elif n3=="/" and n2==0 :
           print("Cannot calculate this answer.")
def sta() :
        print("Bot : What can I help you(song or calculate)?")
        y=input("You : ")
        if "song" in y :
            son={
                "1." : "Myanmar Song",
                "2." : "English Song",
                "3." : "Cortis Song"}
            print(son)
            print("Bot : Choice number 1 or 2 or 3)")
            cho=int(input("You : "))
            if cho==1 :
                print("Bot : Myanmar Song.")
                myansongs()
            elif cho==2 :
               print("Bot : English Song.")
               engsongs()
            elif cho==3 :
                print("Bot : Cortis Song.")
                cortis()
        elif "calculate" in y or "calculation" in y :
            cal ()
respond=input("You : ").lower()
if "hi" in respond or "hello" in respond :
        print("Bot : hello ! I'm Areal Bot.Do yo need my help?")
        n=input("You : ").lower()
        if "stop" in n or "break" in n :
            print("Thanks for using!")
        elif "yes" in n :
            print("Bot : I can help you calculation.Do you need help?")
            i=input("You : ").lower()
            if "yes" in i or "help" in i or "okay" in i:
                cal()
                print("Thanks for using!")
            else :
                print("Thanks for using!")
            
else :
        sta()
        print("Thanks for using!")
        
        
        
           
         
            
              
                       
            
                 
           
    
