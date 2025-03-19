
# Past Actions List
PastActions = []

def print_past_actions(past_actions):
    for i in range(len(past_actions)):
        print("\033[32m", i + 1, past_actions[i], "\033[0m")
def remove_past_actions(past_actions):
    index_to_remove = int(input("Enter the index of the action to remove: "))
    index_to_remove += 1
    past_actions.remove(index_to_remove)
    print(f"The Index {past_actions[index_to_remove]} was removed")
    


def run_past_actions_editor():
    while True:
        try:
            print("")
            print("1: Display Past Actions List")
            print("2: Remove Action From Past Actions")
            
            print("")
            print("0: Exit")
            print("")
            
            
            Mode = int(input("Choose Mode: "))
            
            if Mode == 1:
                print("")
                print_past_actions(PastActions)
                print("")
            elif Mode == 2:
                print("")
                remove_past_actions(PastActions)
                print("")
            elif Mode == 0:
                print("")
                break
                
        except ValueError:
            # Spacer
            print("")
    
            # Print NOT A VALID INPUT When Given A Invalid Value Type
            print("\033[31mNOT A VALID INPUT, TRY AGAIN\033[0m")
    
            # Spacer
            print("")
        
    