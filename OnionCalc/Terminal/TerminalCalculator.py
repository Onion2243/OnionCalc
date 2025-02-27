# Import Different Calculator Section
from Terminal.Calculator_Sections.terminal_section_arthimatic import Arthmatic_Mode
from Terminal.Calculator_Sections.terminal_section_algebra import Algebraic_Mode
from Terminal.Calculator_Sections.terminal_section_geomentry import Geomentry_Mode
from Terminal.Calculator_Sections.terminal_section_triginomentry import Triginomentry_Mode
from Terminal.Calculator_Sections.terminal_section_conversions import Conversions_Mode

# Import The Past Actions Dictionary
from Terminal.Calculator_Sections.terminal_section_past_actions_dictionary import PastActions

# Import Needed OnionLibs
from Libraries.OnionColors.onioncolors import onioncolors
from Libraries.OnionMath.functions import OnionMath

# Terminal Calculator Function
def TerminalCalculator():
    
    # Prints Out Calculator Title When The Program Starts
    print(onioncolors.text_color("orange"),"""
        ------------------------------------------------------------------------------------------------
                                        ALGEBRAIC CALCULATOR V.0.1.0
        ------------------------------------------------------------------------------------------------
        \033[0m
        """,)

    # Keep The Program Constantly Running Until Specified To Quit
    while True:
            # Spacer
            OnionMath.spacer(1)
            
            # Print Choices
            print("1: Artithmatic Functions")
            print("2: Algebraic Functions")
            print("3: Geomentry")
            print("4: Triginomentry")
            print("5: Conversion")
            print("6: Quits Program")
        
            # Spacer Print
            OnionMath.spacer(2)
        
            print("0: Show Your Past Calculations")
        
            # Spacer Print
            OnionMath.spacer(1)
        
            # Try To Do This, If Given The Incorrect Value (Not An Int), Tell User Not A Valid Input And Retry
            try:
                # Ask User Which Arthimatic Mode They Want To Use
                Mode = int(input("Enter The Type Of Mode: "))
        
                # Arthimatic Functions
                if Mode == 1:
                    Arthmatic_Mode()
                
                # Algebraic Mode
                if Mode == 2:
                    Algebraic_Mode()
                    
                # Geomentry Mode        
                if Mode == 3:
                    Geomentry_Mode()
        
                # Triginomentry Mode     
                if Mode == 4:
                    Triginomentry_Mode()
        
                # Conversion Mode
                if Mode == 5:
                    Conversions_Mode()
                            
                # Quits The Program If Prompted  
                if Mode == 6:

                    # Print Thank You Message
                    OnionMath.thank_you_message()
        
                    # End The Program By Breaking From The While Loop
                    break
        
                # Prints Out Past Calculations
                if Mode == 0:
                    # Spacer
                    OnionMath.spacer(1)
                    
                    # Prints Out The Past Actions List
                    print("\033[92mPast Calculations: " + str(PastActions) + "\033[0m")
                    
                    # Spacer
                    OnionMath.spacer(1)
            
            except ValueError:
                # Spacer
                OnionMath.spacer(1)
                
                # Print NOT A VALID INPUT When Given A Invalid Value Type
                print("\033[31mNOT A VALID INPUT, TRY AGAIN\033[0m")
                
                # Spacer
                OnionMath.spacer(1)
                
            # Runs When Keyboard Interuption Happens Like Ctrl+C
            except KeyboardInterrupt:
                # Print Thank You Message, Number Is Included In Order To Bypass An Error With Self
                OnionMath.thank_you_message(1)
                
                # Stops The Calculator
                break