import signup
import login
import traceback

while(True):
    print("\n-----------------------------\nUnderground Social Media Site\n-----------------------------\n")
    print("Choose which of the following you would like to do:\n1: Signup\n2: Login")
    try:
        selection = int(input("\nPlease enter your selection: "))
        if(selection == 1):
            is_hacker_signed_up = signup.signup_hacker()
            if(is_hacker_signed_up != None):
                break
        elif(selection == 2):
            login.check_hacker_login()
            break
        else:
            print("\nInvalid selection. Please re-enter your selection.\n")
    except ValueError:
        # A ValueError is raised if the user enters the correct data type but an inappropriate value
        print("\nInvalid data type. Expected a numerical value.\n")
        traceback.print_exc()
    except:
        print("\nInvalid selection.\n")
        traceback.print_exc()