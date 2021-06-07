import signup
import login
import traceback

# The "Home Page" of the application which prompt hackers to either sign up or log in
while(True):
    print("\n-----------------------------\nUnderground Social Media Site\n-----------------------------\n")
    print("Choose which of the following you would like to do:\n1: Signup\n2: Login")
    
    # Using a try-except block to catch errors when a hacker enters an invalid entry
    try:
        # Prompting the hackers to make a selection
        selection = int(input("\nPlease enter your selection: "))
        # If the hacker wants to sign up, call the signup_hacker function
        if(selection == 1):
            signup.signup_hacker()
        # If the hacker wants to log in, call the check_hacker_login function
        elif(selection == 2):
            login.check_hacker_login()
        # If the hacker enters a selection other than 1 or 2, prompt the hackers to enter their selection again
        else:
            print("\nInvalid selection. Please re-enter your selection.\n")
            continue
        # After the hacker has selected to sign up or log in, don't prompt the hacker to sign up or log in again
        break
    # If the hacker enters invalid data, raise the following exceptions, print an error message to the hacker and the traceback
    except ValueError:
        # A ValueError is raised if the hacker enters the incorrect data type
        print("\nInvalid data type. Expected a numerical value.")
        traceback.print_exc()
    except:
        # Catching all other errors
        print("\nInvalid selection.\n")
        traceback.print_exc()