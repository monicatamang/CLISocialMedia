import options
import traceback

def show_options(hacker_alias, hacker_id):
    while(True):
        try:
            print("\nPlease select one of the following options:\n1: Enter a New Exploit\n2: View My Exploits\n3: Modify My Exploits\n4: View Other Exploits\n5: Exit the Application")
            selection = int(input("\nPlease enter your selection: "))
            if(selection == 1):
                options.enter_new_exploit(hacker_alias, hacker_id)
            elif(selection == 2):
                options.view_my_exploits(hacker_alias, hacker_id)
            elif(selection == 3):
                options.modify_my_exploits(hacker_alias, hacker_id)
            elif(selection == 4):
                options.view_other_exploits(hacker_alias, hacker_id)
            elif(selection == 5):
                print("\nThank you for visiting the Underground Social Media Site!")
                break
            else:
                print("\nInvalid selection. Please enter a valid selection.")
        except ValueError:
            print("\nInvalid data entry. Expected a numerical value.\n")
            traceback.print_exc()
        except:
            print("\nAn error has occurred.\n")
            traceback.print_exc()