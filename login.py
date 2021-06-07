import mariadb
import dbconnect
import traceback
import options_menu

# Creating a function that logs in the hacker
def check_hacker_login():
    # Connecting to the database and creating a cursor
    conn = dbconnect.open_db_connection()
    cursor = dbconnect.create_db_cursor(conn)

    # If the connection to the database is successful but the cursor was not created, try to close the cursor and database connection, don't run the next lines of code
    if(conn == None or cursor == None):
        print("An error in the database has occured.")
        dbconnect.close_cursor(cursor)
        dbconnect.close_db_connection(conn)
        return

    # Using a try-except block to catch errors when a hacker enters their login credentials
    try:
        print("\nLogin")
        print("-----\n")

        # Prompting the hacker to enter their username and password
        hacker_login_alias = input("Please enter your username: ")
        hacker_login_password = input("Please enter your password: ")

        # Getting the hacker's id, alias and password and checking to see if it matches their credentials stored in the database
        cursor.execute("SELECT * FROM hackers WHERE alias = ? AND password = ?", [hacker_login_alias, hacker_login_password])
        database_login_info = cursor.fetchall()

        # If a match is found, it means the hacker has succesfully logged in and will be shown all of the options. The hacker will not be asked to log in again 
        # If a match is not found, print an error message to the hacker and prompt them to re-enter their username and password
        if(cursor.rowcount == 1):
            print(f"\nWelcome back, @{hacker_login_alias}.")
            # Passing the hacker's username and id so that it can be used to create new exploits, view exploits and modify exploits
            options_menu.show_options(hacker_login_alias, database_login_info[0][0])
            return
        else:
            print("\nThe username and password do not match our records. Please re-enter your login information.")
    # If any errors occurs during the time the hacker is logging in, raise the following exception, print an error message to the user and the traceback
    except mariadb.OperationalError:
        # An OptionalError exception is raised for things that are not in control of the programmer such as an unexpected connection failure, server hutting down, etc.
        print(f"\nFailed to connect to the database. Unable to retrieve @{hacker_login_alias}'s login information.\n")
        traceback.print_exc()
    except mariadb.ProgrammingError:
        # A ProgrammingError exception is raised if there are errors made by the programmer such as incorrect SQL syntax, getting data from a table that is not found, etc.
        print("\nInvalid SQL syntax.\n")
        traceback.print_exc()
    except mariadb.NotSupportedError:
        # A NotSupportedError exception is raised if a programmer writes code that is not supported by a certain method such as a MariaDB syntax error
        print("\nInvalid MariaDB syntax.\n")
        traceback.print_exc()
    except mariadb.DatabaseError:
        # A DatabaseError exception is raise for all errors that are related to the database
        print(f"\nAn error has occured in the database. Failed to retrieve @{hacker_login_alias}'s login information.\n")
        traceback.print_exc()
    except:
        # Catching all other errors
        print("\nAn error has occured. Failed to log in.\n")
        traceback.print_exc()

    # Closing the cursor and the database connection
    closing_cursor = dbconnect.close_cursor(cursor)
    closing_db = dbconnect.close_db_connection(conn)

    # If the cursor or database connection failed to close, print an error message
    # If the cursor or database connection successfully closed, print a success message
    if(closing_cursor == False or closing_db == False):
        print("Failed to close cursor and database connection.")
    else:
        print("Cursor and database connection was successfully closed.")