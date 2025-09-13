print("""

                                              ,           ^'^  _
                                              )               (_) ^'^
                                 .---------. ((        ^'^
                                 )`'`'`'`'`( ||                 ^'^
                                /`'`'`'`'`'`\||           ^'^
                               /`'`'`'`'`'`'`\|
                      ,,,,,,, /`'`'`'`'`'`'`'`\      ,
                     .-------.`|`````````````|`  .   )
                    / .^. .^. \|  ,^^, ,^^,  |  / \ ((
                   /  |_| |_|  \  |__| |__|  | /,-,\||
        _         /_____________\ |")| |  |  |/ |_| \|
       (")         |  __   __  |  '==' '=='  /_______\     _
      (' ')        | /  \ /  \ |   _______   |,^, ,^,|    (")
       \  \        | |--| |--| |  ((--.--))  ||_| |_||   (' ')
     _  ^^^ _      | |__| |("| |  ||  |  ||  |,-, ,-,|   /  /
   ,' ',  ,' ',    |           |  ||  |  ||  ||_| |_||   ^^^
.,,|RIP|,.|RIP|,.,,'==========='==''=='==''=='=======',,....,,,,.,.,,
""")

health = 100

print("Welcome to the Haunted Mansion")
print("You are a distant family member of a rich millionare who has just passed away leaving this mansion to you.")
print("As the newfound owner. you decied to pay a visit to the mansion")
print("The house is dated, creaky, and falling apart. You walk in the front door")
print("you see two doors to your left and right and a door infront of you thats locked")

while(health > 0):
    
    print("Do you want to enter the living room or the dining room?")

    RoomChoice = input("> ")

    if(RoomChoice == "living room"):
        print("""
 ________________________________________________________________________
|: : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : |
|__________ : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : :|
|__]\% % % | : : : : : : : : : : : : : : : : : : : : : : : : : : : : : : |
|___]\% % %|: :______ : : : : : : : : : : : : : : : : : : : : :___: : : :|
|____]\% % | :|======| :_: : : : : : . : : : : : :_: : : : : :/   \: : : |
|_____]\% %|: ||\|||||:/_\: :,: : :.'o'.: : :,: :/_\: : : : :|//   |: : :|
|______]\% | :|======| =|= __#_____|___|_____#__ =|= : : : : | ,*, | : : |
|_______]\%|: |______|: ^ :[___]           [___]: ^ : : : : : \*;*/ : : :|
|________]\| :|__  __| : : [_|_] o  `(,  o [_|_] : : : : :_____(_)_____: |
|_________]\: | .||. |: : :[___] |  ( )  | [___]: : :_!_: ||   .|.   || :|
|__________]==|__||__|====_[_|_]/!\_@@@_/!\[_|_]_===/___\=||____|____||==|
     _                    '====================='     | _                |
    |_)         __.;;.__      _______________         |( |               |
    /_\__      / ;(;;); \    (               )       _|_)|               |
  ~=_|_ _)====/__________\==(\               /)=====(____|========~      |
 ~=|___|LL====|==========|===|               |======LLLLLL=========~     |
~============================|_______________|======================~    |
=============================LLLLLLLLLLLLLLLLL=======================~   |
lc====================================================================~  '
""")

        print("You enter the living room")
        print("As you walk in you see a sleeping pitbull gaurding some gold jewlery")
        print("do you want to steal the jewlery from the pitbull?")

        PitBullChoice = input("> ")

        if(PitBullChoice == "yes"):
            import random
            damage1 = random.randint(10, 20)
            print("You attempt to steal from the pitbull. But it wakes up and bites you!")
            print("You get away but you have lost",damage1,"health")
            health = health - damage1
            print("you have",health,"health remaining")
            print("luckily the pitbull is chained up so he cant chase you")
            print("Do you want to return to the hallway or go to the bathroom")

            LivingRoomChoice = input("> ")

            if(LivingRoomChoice == "hallway"):
                print("you return to the hallway")
            elif(LivingRoomChoice == "bathroom"):
                print("you enter the bathroom")
            else:
                print("invalid choice please chose either hallway or bathroom")
        elif(PitBullChoice == "no"):
            print("you decied to not steal the dogs jewlery")
            print("Do you want to return to the hallway or go to the bathroom")

            LivingRoomChoice1 = input("> ")

            if(LivingRoomChoice1 == "hallway"):
                print("you return to the hallway")
            elif(LivingRoomChoice1 == "bathroom"):
                print("you enter the bathroom")
            else:
                print("invalid choice please chose either hallway or bathroom")
        else:
            print("Invalid choice. Please choose either yes or no.")

    elif(RoomChoice == "dining room"):
        print("""
0================================================0
|'.                    (|)                     .'|
|  '.                   |                    .'  |
|    '.                |O|                 .'    |
|      '. ____________/===\_____________ .'      |
|        :             `\"/`  ______     :     .. |
|        :     mmmmmmm  V   |--%%--|    :   .'|| |
|        :     |  |  |      |-%%%%-|    :  |  || |
|        :     |--|--| @@@  |=_||_=|    :  I  || |
|        :     |__|__|@@@@@ |_\__/_|    :  |  || |
|        :             \|/   ____       :  |  || |
|        :;;       .'``(_)```\__/````:  :  |  || |
|        :||___   :================:'|  :  | 0+| |
|        :||===)  | |              | |  :  |  || |
|        ://``\\___|_|______________|_|__:  I  || |
|      .'/'    \'  | '              | '   '.|  || |
|    .'           |                |       '. || |
|  .'                                        '|| |
|.'                                            '.|
0================================================0
""")
        print("you chose to go into the dining room.")
        print("As you walk in you see a shiny vase on the table.")
        print("Do you want to open the vase?")

        VaseChoice = input("> ")

        if(VaseChoice == "yes"):
             print("You open the vase and find a pile of bones!")
             print("Do you want to return to the hallway or go to the kitchen?")
             NextRoom = input("> ")
             if(NextRoom == "hallway"):
                 print("You enter the hallway")
             elif(NextRoom == "kitchen"):
                 print("""

   .-.    .-.    .-.    .-.  .-.  .-"-.  .-.      .--.      .-.  .--.
  <   |  <   |  <   |   | |  | |  | | |  | |      |()|     /  |  |  |
   )  |   )  |   )  |   | |  | |  | | |  | |      |  |     |  |  |  |
   )()|   )()|   )()|   |o|  | |  | | |  | |      |  |     |  |  |()|
   )()|   )()|   )()|   |o|  | |  | | |  | |      |  |     |  |  |()|
  <___|  <___|  <___|   |\|  | |  | | |  | |      |  |     |  |  |__|
   }  |   || |   =  |   | |  | |  `-|-'  | |      |  |     |  |  |   L
   }  |   || |   =  |   | |  | |   /A\   | |      |  |     |  |  |   J
   }  |   || |   =  |   |/   | |   |H|   | |      |  |     |  |  |    L
   }  |   || |   =  |        | |   |H|   | |     _|__|_    |  |  |    J
   }  |   || |   =  |        | |   |H|   | |    | |   |    |  |  | A   L
   }  |   || |   =  |        | |   \V/   | |    | |   |     \ |  | H   J
   }  |   FF |   =  |        | |    "    | |    | \   |      ,Y  | H A  L
   }  |   LL |    = |       _F J_       _F J_   \  `--|       |  | H H  J
   }  |   LL |     \|     /       \   /       \  `.___|       |  | H H A L
   }  |   \\ |           J         L |  _   _  |              |  | H H U J
   }  |    \\|           J         F | | | | | |             /   | U ".-'
    } |     \|            \       /  | | | | | |    .-.-.-.-/    |_.-'
     \|                    `-._.-'   | | | | | |   ( (-(-(-( )
                                     `-' `-' `-'    `-`-`-`-'
""")
                 print("You enter the kitchen")
                 print("You see a man standing at the other side of the kitchen")
                 print("Do you want to attack the man?")
                 Attack = input("> ")
                 if(Attack == "yes"):
                     print("You start to sproach the man along the way you grab a frying pan and swing it at the man.")
                     print("The man colapseses.")
                     print("You reach down and flip the man over and it turns out it was just a manequinne")
                     print("there is nowhere to go from here so you return to the hallway")
                 elif(Attack == "no"):
                     print("You slowly aproach the man")
                     print("You call out to the man but get no responce")
                     print("As you continue aproaching you realise its just a manequinne")
                     print("there is nowhere to go from here so you return to the hallway")
                 else:
                     print("invalid choice please chose either yes or no")
             else:
                  print("invalid choice please chose either hallway or kitchen")
        elif(VaseChoice == "no"):
            import random
            damage2 = random.randint(30, 50)
            print("You decied not to open the vase.")
            print("As you turn to leave. You hear a cracking sound coming from the corner.")
            print("A dark figure with glowing red eyes launches at you! And knocks you down.")
            print("you lose",damage2,"health.")
            health = health - damage2
            print("you have",health,"health remaining")
            print("Do you want to return to the hallway or go to the kitchen?")
            NextRoom1 = input("> ")
            if(NextRoom1 == "hallway"):
                print("You enter the hallway")
            elif(NextRoom1 == "kitchen"):
                print("""

   .-.    .-.    .-.    .-.  .-.  .-"-.  .-.      .--.      .-.  .--.
  <   |  <   |  <   |   | |  | |  | | |  | |      |()|     /  |  |  |
   )  |   )  |   )  |   | |  | |  | | |  | |      |  |     |  |  |  |
   )()|   )()|   )()|   |o|  | |  | | |  | |      |  |     |  |  |()|
   )()|   )()|   )()|   |o|  | |  | | |  | |      |  |     |  |  |()|
  <___|  <___|  <___|   |\|  | |  | | |  | |      |  |     |  |  |__|
   }  |   || |   =  |   | |  | |  `-|-'  | |      |  |     |  |  |   L
   }  |   || |   =  |   | |  | |   /A\   | |      |  |     |  |  |   J
   }  |   || |   =  |   |/   | |   |H|   | |      |  |     |  |  |    L
   }  |   || |   =  |        | |   |H|   | |     _|__|_    |  |  |    J
   }  |   || |   =  |        | |   |H|   | |    | |   |    |  |  | A   L
   }  |   || |   =  |        | |   \V/   | |    | |   |     \ |  | H   J
   }  |   FF |   =  |        | |    "    | |    | \   |      ,Y  | H A  L
   }  |   LL |    = |       _F J_       _F J_   \  `--|       |  | H H  J
   }  |   LL |     \|     /       \   /       \  `.___|       |  | H H A L
   }  |   \\ |           J         L |  _   _  |              |  | H H U J
   }  |    \\|           J         F | | | | | |             /   | U ".-'
    } |     \|            \       /  | | | | | |    .-.-.-.-/    |_.-'
     \|                    `-._.-'   | | | | | |   ( (-(-(-( )
                                     `-' `-' `-'    `-`-`-`-'
""")
                print("You enter the kitchen")
                print("You see a man standing at the other side of the kitchen")
                print("Do you want to attack the man?")
                Attack1 = input("> ")
                if(Attack1 == "yes"):
                    print("You start to sproach the man along the way you grab a frying pan and swing it at the man.")
                    print("The man colapseses.")
                    print("You reach down and flip the man over and it turns out it was just a manequinne")
                    print("there is nowhere to go from here so you return to the hallway")
                elif(Attack1 == "no"):
                    print("You slowly aproach the man")
                    print("You call out to the man but get no responce")
                    print("As you continue aproaching you realise its just a manequinne")
                    print("there is nowhere to go from here so you return to the hallway")
                else:
                     print("invalid choice please chose either yes or no")
            else:
                print("invalid choice please chose either hallway or kitchen")
        else:
            print("Invalid choice. Please choose either yes or no.")
        
    else:
        print("Invalid choice. Please choose either dining room or living room")

print("you are dead")








    
