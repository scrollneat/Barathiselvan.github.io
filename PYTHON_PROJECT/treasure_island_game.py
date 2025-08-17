print('''
*************************************************************************************************************************
  ,d                                                                       
  88                                                                       
MM88MMM 8b,dPPYba,  ,adPPYba, ,adPPYYba, ,adPPYba, 88       88 8b,dPPYba,  
  88    88P'   "Y8 a8P_____88 ""     `Y8 I8[    "" 88       88 88P'   "Y8  
  88    88         8PP""""""" ,adPPPPP88  `"Y8ba,  88       88 88          
  88,   88         "8b,   ,aa 88,    ,88 aa    ]8I "8a,   ,a88 88          
  "Y888 88          `"Ybbd8"' `"8bbdP"Y8 `"YbbdP"'  `"YbbdP'Y8 88          
                                                                                           
                             ,adPPYba, 
                            a8P_____88 
                            8PP""""""" 
                            "8b,   ,aa 
                             `"Ybbd8"'  
                                                               
                                                               
88           88                                 88  
""           88                                 88  
             88                                 88  
88 ,adPPYba, 88 ,adPPYYba, 8b,dPPYba,   ,adPPYb,88  
88 I8[    "" 88 ""     `Y8 88P'   `"8a a8"    `Y88  
88  `"Y8ba,  88 ,adPPPPP88 88       88 8b       88  
88 aa    ]8I 88 88,    ,88 88       88 "8a,   ,d88  
88 `"YbbdP"' 88 `"8bbdP"Y8 88       88  `"8bbdP"Y8  

************************************************************************************************************************
''')

print("Welcome to Treasure Island.Your mission is to find the treasure")
print("\nYou got two path in front of you which one do you want to take? left or right?:")

path = input("\nType left or right:\n").lower()

if (path == "left"):
    print("\nNow You have reached the lake. Take your Choice Now Swim or Find a Boat?")
    path2 = input("Type swim or boat:\n").lower()
    if path2 == "swim":
        print("\nGAME OVER!\nDeath By Crocodiles!")
    elif path2 == "boat":
        print("\nYour Treasure and your Death Awaits behind those doors. Pick the right door to Treasure\n")
        path3 = input("Which Door you want to Pick Red or Green or Yellow:\n").lower()
        
        if path3 == "red":
            print("\nGAME OVER!\nDeath By Fire!")
        elif path3 == "green":
            print("\nGAME OVER!\nDeath By Poisonous Gas!")
        elif path3 == "yellow":
            print("\nYou are the new Billionaire. \nYou found the Treasure and Cleared the Game!\nUse your Treasure Wisely")
        else:
            print("\nYou have typed the wrong input")
    else:
        print("\nYou have typed the wrong input")
elif path == "right":
    print("\nGAME OVER!\n\nYour have Entered Contaminated Zone, You will die in the hands of Zombies")
else:
    print("\nYou have typed the wrong input")







