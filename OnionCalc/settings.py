import json

def Settings_Editor():
    while True:
        try:
            print("""\033[38;5;214m
------------------------------------------------------------------------------------------------
                            Welcome To The OnionCalc Setting Editor
------------------------------------------------------------------------------------------------


\033[0m
""",)
            print("1: Change Modes Visibility")
            print("")
            print("0:  Exit Settings Menu")
            
            Mode = int(input("Select Setting To Change: "))
            
            if Mode == 1:
                print("")
                print("Entering A Number Into The Box Will Enabled The Input, The Example Below Enables All Of The Modes")
                print("Example: 1234560")
                print("Another Example: 13460")

                setting_modes_visibility = list(input("Type In A List Of Modes You Want To Enable: "))
    
                file = open("settings.json", "w")
    
                file.flush()
                
                json.dump(setting_modes_visibility, file)
                file.close()
            elif Mode == 0:
                print("""\033[38;5;214m
------------------------------------------------------------------------------------------------
                            Exiting Settings Menu, Please Reload The Program
------------------------------------------------------------------------------------------------
\033[0m
""",)
                break
        except ValueError:
            print("Invalid Input, Please Try Again")
            
            
        