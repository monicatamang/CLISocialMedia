import mariadb
import dbconnect
import traceback
import options_menu

# Creating a function that signs up hackers
def signup_hacker():
    # Connecting to the database and creating a cursor
    conn = dbconnect.open_db_connection()
    cursor = dbconnect.create_db_cursor(conn)

    # If the connection to the database is successful but the cursor was not created, try to close the cursor and database connection, don't run the next lines of code
    if(conn == None or cursor == None):
        print("An error in the database has occured.")
        dbconnect.close_cursor(cursor)
        dbconnect.close_db_connection(conn)
        return

    # Using a try-except block to catch errors when a hacker signs up for an account
    try:
        print("\nSignup")
        print("------\n")

        # Prompting the hacker to enter their username and password
        hacker_signup_alias = input("Create a username: ")
        hacker_signup_password = input("Create a password: ")

        # If the hacker does not enter anything for the username or password field, print an error message to the hacker and prompt them to enter a username and password again
        # If not, store their username and password to the database and commit the changes
        if(hacker_signup_alias == "" or hacker_signup_password == ""):
            print("\nInvalid signup information. Please enter valid credentials to create an account.")
        else:
            cursor.execute("INSERT INTO hackers(alias, password) VALUES(?, ?)", [hacker_signup_alias, hacker_signup_password])
            conn.commit()

            # Checking to see if their information is stored into the database and if it is, print a welcome message to the hacker and show them the list of options. The hacker will not be prompted to create an account again
            # If their username and password was not stored into the database, print an error message to the hacker
            if(cursor.rowcount == 1):
                print(f"\nWelcome, @{hacker_signup_alias}. Your Hacker ID is {cursor.lastrowid}")
                options_menu.show_options(hacker_signup_alias, cursor.lastrowid)
                return
            else:
                print("\nFailed to create an account.")
    # If errors occurs during this process, raise the following exceptions, print an error message to the hacker and the traceback
    except mariadb.IntegrityError:
        # An IntegrityError is raised if there is a constraint failure. In this case, a unique key is set on every username, and if the integrity of the contraint is not respected, it will cause an error
        print(f"\n@{hacker_signup_alias} is already taken. Please enter another username.\n")
        traceback.print_exc()
    except mariadb.DataError:
        # A DataError exception is raised if there are issues with processing data. In this case, the username and password is set to have a maximum of 20 characters in length, if a hacker exceeds this limit, an error will occur
        print("\nYour username or password has exceed the limit of 20 characters. Please re-enter your information.\n")
        traceback.print_exc()
    except mariadb.OperationalError:
        # An OptionalError exception is raised for things that are not in control of the programmer such as an unexpected connection failure, server hutting down, etc.
        print(f"\nFailed to connect to the database. Unable to create an account.\n")
        traceback.print_exc()
    except mariadb.ProgrammingError:
        # A ProgrammingError exception is raised if there are errors made by the programmer such as incorrect SQL syntax, getting data from a table that is not found, etc.
        print("\nInvalid SQL syntax. Please refer to the documentation.\n")
        traceback.print_exc()
    except mariadb.NotSupportedError:
        # A NotSupportedError exception is raised if a programmer writes code that is not supported by a certain method such as a MariaDB syntax error
        print("\nInvalid MariaDB syntax. Please refer to the documentation.\n")
        traceback.print_exc()
    except mariadb.DatabaseError:
        # A DatabaseError exception is raise for all errors that are related to the database
        print(f"\nAn error has occured in the database. Failed to create an account.\n")
        traceback.print_exc()
    except mariadb.InterfaceError:
        # An InterfaceError exception is raised if there are errors found in python or the database client
        print("An interface error has occured. Please check the documentation for Python or the database client.")
        traceback.print_exc()
    except:
        # Catching all other errors
        print("\nAn error has occured. Failed to sign up for an account.\n")
        traceback.print_exc()

    # Closing the cursor and the database connection
    closing_cursor = dbconnect.close_cursor(cursor)
    closing_db = dbconnect.close_db_connection(conn)

    # If the cursor or database connection failed to close, print an error message
    if(closing_cursor == False or closing_db == False):
        print("\nFailed to close cursor and database connection.")