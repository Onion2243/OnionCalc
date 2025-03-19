# Import Different Calculator Section
from Terminal.Calculator_Sections.terminal_section_arthimatic import Arthmatic_Mode
from Terminal.Calculator_Sections.terminal_section_algebra import Algebraic_Mode
from Terminal.Calculator_Sections.terminal_section_geomentry import Geomentry_Mode
from Terminal.Calculator_Sections.terminal_section_triginomentry import Triginomentry_Mode
from Terminal.Calculator_Sections.terminal_section_conversions import Conversions_Mode
from Terminal.Calculator_Sections.terminal_section_past_actions_dictionary import run_past_actions_editor

# Import Needed OnionLibs
from Libraries.OnionMath.functions import OnionMath

"""
Pass a mode_list Parameter to Restrict Available Modes
Instead of allowing all modes, you can pass a list of allowed modes. 
This way, the calculator will only show and accept input for specific options.

TO DO: Add Spacing, Coloring, And Work On Removing The OnionColors Library Since It Is Pointless

CONSIDER: Attempt to figure out how to encrypt the settings file unless an admin password is given,
which is also inside of the settings file, to prevent students or not admin users from editing which modes they can
and cannot use
"""

# Terminal Calculator Function
def TerminalCalculator(modes_avilable_list):

    # Keep The Program Constantly Running Until Specified To Quit
    while True:
            print("""\033[38;5;214m
------------------------------------------------------------------------------------------------
                                OnionCalc Terminal V.0.2.0
------------------------------------------------------------------------------------------------
\033[0m
""",)
            # Spacer
            OnionMath.spacer(1)
            
            for i in range(len(modes_avilable_list)):
                if modes_avilable_list[i] == '1':
                    print("1: Artithmatic Functions")
                    Mode_1_Useable = True
                elif modes_avilable_list[i] == '2':
                    print("2: Algebraic Functions")
                    Mode_2_Useable = True
                elif modes_avilable_list[i] == '3':
                    print("3: Geometric Functions")
                    Mode_3_Useable = True
                elif modes_avilable_list[i] == '4':
                    print("4: Trigonometric Functions")
                    Mode_4_Useable = True
                elif modes_avilable_list[i] == '5':
                    print("5: Conversions Functions")
                    Mode_5_Useable = True
                elif modes_avilable_list[i] == '6':
                    print("6: Exit Calculator")
                    Mode_6_Useable = True
                elif modes_avilable_list[i] == '0':
                    print("0: Past Actions Editor")
                    Mode_0_Useable = True
        
            # Try To Do This, If Given The Incorrect Value (Not An Int), Tell User Not A Valid Input And Retry
            try:
                # Ask User Which Arthimatic Mode They Want To Use
                print("")
                Mode = int(input("Enter The Type Of Mode: "))
        
                # Arthimatic Functions
                if Mode == 1 and Mode_1_Useable == True:
                    Arthmatic_Mode()
                
                # Algebraic Mode
                if Mode == 2 and Mode_2_Useable == True:
                    Algebraic_Mode()
                    
                # Geomentry Mode        
                if Mode == 3 and Mode_3_Useable == True:
                    Geomentry_Mode()
        
                # Triginomentry Mode     
                if Mode == 4 and Mode_4_Useable == True:
                    Triginomentry_Mode()
        
                # Conversion Mode
                if Mode == 5 and Mode_5_Useable == True:
                    Conversions_Mode()
                            
                # Quits The Program If Prompted  
                if Mode == 6 and Mode_6_Useable == True:

                    # Print Thank You Message
                    print("""\033[38;5;214m
------------------------------------------------------------------------------------------------
                            Exiting OnionCalc Terminal V.0.2.0
------------------------------------------------------------------------------------------------
\033[0m
""",)
        
                    # End The Program By Breaking From The While Loop
                    break
        
                # Prints Out Past Calculations
                if Mode == 0 and Mode_0_Useable == True:
                    run_past_actions_editor()
                    
            
            except ValueError:
                # Spacer
                OnionMath.spacer(1)
                
                # Print NOT A VALID INPUT When Given A Invalid Value Type
                print("\033[31mNOT A VALID INPUT, TRY AGAIN\033[0m")
                
                # Spacer
                OnionMath.spacer(1)
                
            # Runs When Keyboard Interuption Happens Like Ctrl+C
            except KeyboardInterrupt:
                # Prints Out Calculator Title When The Program Starts
                print("""\033[38;5;214m
------------------------------------------------------------------------------------------------
                            Exiting OnionCalc Terminal V.0.2.0
------------------------------------------------------------------------------------------------
\033[0m
""",)
                
                # Stops The Calculator
                break
            except UnboundLocalError:
                # Spacer
                OnionMath.spacer(1)

                # Print NOT A VALID INPUT When Given A Invalid Value Type
                print("\033[31mMODE IS NOT ENABLED, PLEASE OPEN THE SETTINGS EDITOR IN ORDER TO ENABLE IT\033[0m")

                # Spacer
                OnionMath.spacer(1)
                