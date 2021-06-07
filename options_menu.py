import create_exploit
import owner_exploits
import modify_exploits
import other_exploits
import traceback

# Creating a function that shows the hacker the options menu after signing up or logging in
def show_options(hacker_alias, hacker_id):
    # Once the hacker has selected an option, continue running the application
    while(True):
        # Using a try-except block that catches errors when a hacker enters their selection
        try:
            # Showing the hacker the list of options to choose from
            print("\nPlease select one of the following options:\n1: Enter a New Exploit\n2: View My Exploits\n3: Modify My Exploits\n4: View Other Exploits\n5: Exit the Application")

            # Prompting the hacker to enter their selection
            selection = int(input("\nPlease enter your selection: "))

            # If the hacker wants to create a new exploit, call the function with the hacker's username and id
            if(selection == 1):
                create_exploit.enter_new_exploit(hacker_alias, hacker_id)
            # If the hacker wants to view their own exploits, call the function with the hacker's username and id
            elif(selection == 2):
                owner_exploits.view_my_exploits(hacker_alias, hacker_id)
            # If the hacker wants to edit their exploits, call the function with the hacker's username and id
            elif(selection == 3):
                modify_exploits.modify_my_exploits(hacker_alias, hacker_id)
            # If the hacker wants to view other exploits, call the function with the hacker's id
            elif(selection == 4):
                other_exploits.view_other_exploits(hacker_id)
            # If the hacker wants to leave the site, print a message and break the loop
            elif(selection == 5):
                print("\nThank you for visiting the Underground Social Media Site!")
                break
            # If the hacker enters a number that is not between 1 and 5, print a message and prompt the hacker to enter their selection again
            else:
                print("\nInvalid selection. Please enter a valid selection.")
        # If the hacker enters an invalid selection, raise the following exceptions, print and message to the hacker and the traceback
        except ValueError:
            # A ValueError exception is raised if the hacker enters a value that is not an integer data type
            print("\nInvalid data entry. Expected a numerical value.\n")
            traceback.print_exc()
        except:
            # Catching all other exceptions
            print("\nAn error has occurred.\n")
            traceback.print_exc()