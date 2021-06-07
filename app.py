import signup
import login
import traceback

# The "Home Page" of the application which prompt hackers to either sign up or log in
# If the hacker enters an invalid selection, prompt the hacker to enter their selection again
while(True):
    print("\n-----------------------------\nUnderground Social Media Site\n-----------------------------\n")
    print("Choose which of the following you would like to do:\n1: Signup\n2: Login")

    # Using a try-except block to catch errors when a hacker enters an invalid selection
    try:
        # Prompting the hacker to make a selection
        selection = int(input("\nPlease enter your selection: "))
        # If the hacker wants to sign up, call the signup_hacker function
        # If the hacker successfully signed up, don't show the "Home Page" menu selection again
        if(selection == 1):
            is_hacker_signed_up = signup.signup_hacker()
            if(is_hacker_signed_up == True):
                break
        # If the hacker wants to log in, call the check_hacker_login function
        # If the hacker succesfully logged in, don't show the "Home Page" menu selection again
        elif(selection == 2):
            is_hacker_logged_in = login.check_hacker_login()
            if(is_hacker_logged_in == True):
                break
        else:
            # If the hacker enters a selection other than 1 or 2, prompt the hacker to enter their selection again
            print("\nInvalid selection. Please re-enter your selection.\n")
    # If the hacker enters invalid data, raise the following exceptions, print an error message to the hacker and the traceback
    except ValueError:
        # A ValueError is raised if the hacker enters an incorrect data type, i.e., if the hacker enters a selection that is not an integer data type
        print("\nInvalid data type. Expected a numerical value.")
        traceback.print_exc()
    except:
        # Catching all other errors
        print("\nInvalid selection.\n")
        traceback.print_exc()