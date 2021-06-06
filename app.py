import mariadb
import dbconnect
import traceback
import re

def view_other_exploits(hacker_login_alias, hacker_login_id):
    conn = open_db_connection()
    cursor = open_cursor(conn)

    try:
        cursor.execute("SELECT h.alias, e.content FROM cli_social_media.hackers h INNER JOIN cli_social_media.exploits e ON e.hacker_id = h.id WHERE h.id != ?", [hacker_login_id])
        other_exploits = cursor.fetchall()
        if(len(other_exploits) == 0):
            print("\nNo posts found.\n")
        else:
            print("\nOther Exploits")
            print("--------------")
            for exploit in other_exploits:
                print(f"\nExploit Written by @{exploit[0]}\n")
                print(f"{exploit[1]}\n")
                print("------------------------------")
    except mariadb.IntegrityError:
        print(f"\nErrors found in database contraints. Failed to retrieve @{hacker_login_alias}'s exploits.\n")
        traceback.print_exc()
    except mariadb.OperationalError:
        print(f"\nFailed to connect to the database. Unable to retrieve @{hacker_login_alias}'s exploits\n")
        traceback.print_exc()
    except mariadb.ProgrammingError:
        print("\nInvalid SQL syntax.\n")
        traceback.print_exc()
    except mariadb.NotSupportedError:
        print("\nInvalid MariaDB syntax.\n")
        traceback.print_exc() 
    except mariadb.DataError:
        print("\nInvalid data being passed to the database.\n")
        traceback.print_exc()
    except mariadb.DatabaseError:
        print(f"\nAn error has occured in the database. Failed to retrieve @{hacker_login_alias}'s exploits.\n")
        traceback.print_exc()
    except:
        print("\nAn error has occurred.\n")
        traceback.print_exc()

    close_db_and_cursor(cursor, conn)

def modify_my_exploits(hacker_login_alias, hacker_login_id):
    conn = open_db_connection()
    cursor = open_cursor(conn)

    print("\nPlease choose which exploit you would like to modify.")

    while(True):
        try:
            cursor.execute("SELECT e.id, h.alias, e.content, h.id, e.hacker_id FROM hackers h INNER JOIN exploits e ON e.hacker_id = h.id WHERE h.id = ?", [hacker_login_id])
            my_exploits = cursor.fetchall()
            if(len(my_exploits) == 0):
                print("\nNo posts found.\n")
            else:
                print("\nMy Exploits")
                print("-----------")
                for exploit in my_exploits:
                    print(f"\nExploit #{exploit[0]} by @{exploit[1]}\n")
                    print(f"{exploit[2]}\n")
                    print(f"Hacker ID: {exploit[3]}\n")
                    print("------------------------------\n")

            exploit_selection = int(input("Please enter the exploit number of the exploit you would like to modify: "))
            
            print(f"\nModifying Exploit #{exploit_selection} by @{hacker_login_alias}")
            print("------------------------------ \n")
            new_exploit_string = input("Enter text here: \n\n")
            if(new_exploit_string == ""):
                print("Invalid entry. Please re-enter your entry.")
            else:
                new_exploit_escape = re.sub(r"\'", r"\\'", new_exploit_string)
                cursor.execute("SELECT content FROM exploits e WHERE e.id = ? AND e.hacker_id = ?", [exploit_selection, hacker_login_id])
                old_exploit = cursor.fetchall()
                
                cursor.execute("UPDATE exploits SET content = ? WHERE content = ?", [new_exploit_escape, old_exploit[0][0]])
                conn.commit()

                print(f"\n@{hacker_login_alias}'s exploit was successfully updated.")
                break
        except IndexError:
            print(f"\n@{hacker_login_alias} is not authorized to modify Exploit #{exploit_selection}.\n")
            traceback.print_exc()
        except ValueError:
            print("\nInvlaid data entry. Expected a numerical type. Please re-enter the exploit number.\n")
            traceback.print_exc()
        except mariadb.OperationalError:
            print(f"\nErrors in method of retrieving @{hacker_login_alias}'s exploits.\n")
            traceback.print_exc()
        except mariadb.ProgrammingError:
            print(f"\nUnable to escape metacharacters in @{hacker_login_alias}'s exploit. Failed to upload @{hacker_login_alias}'s exploit to the database.\n")
            traceback.print_exc()
        except mariadb.NotSupportedError:
            print("\nInvalid MariaDB syntax.\n")
            traceback.print_exc() 
        except mariadb.DataError:
            print("\nInvalid data being passed to the database.\n")
            traceback.print_exc()
        except mariadb.DatabaseError:
            print(f"\nAn error has occured in the database. Failed to retrieve @{hacker_login_alias}'s exploits.\n")
            traceback.print_exc()
        except:
            print(f"\nAn error occured. Failed to upload @{hacker_login_alias}'s exploit.\n")
            traceback.print_exc()
    
    close_db_and_cursor(cursor, conn)

def view_my_exploits(hacker_login_alias, hacker_login_id):
    conn = open_db_connection()
    cursor = open_cursor(conn)

    try:
        cursor.execute("SELECT e.id, h.alias, e.content, h.id FROM hackers h INNER JOIN exploits e ON e.hacker_id = h.id WHERE h.id = ?", [hacker_login_id])
        my_exploits = cursor.fetchall()
        if(len(my_exploits) == 0):
            print("\nNo posts found.\n")
        else:
            print("\nMy Exploits")
            print("-----------")
            for exploit in my_exploits:
                print(f"\nExploit #{exploit[0]} by @{exploit[1]}\n")
                print(f"{exploit[2]}\n")
                print(f"Hacker ID: {exploit[3]}\n")
                print("------------------------------")
    except mariadb.IntegrityError:
        print(f"\nErrors found in database contraints. Failed to retrieve @{hacker_login_alias}'s exploits.\n")
        traceback.print_exc()
    except mariadb.OperationalError:
        print(f"\nErrors in method of retrieving @{hacker_login_alias}'s exploits.\n")
        traceback.print_exc()
    except mariadb.ProgrammingError:
        print("\nInvalid SQL syntax.\n")
        traceback.print_exc()
    except mariadb.NotSupportedError:
        print("\nInvalid MariaDB syntax.\n")
        traceback.print_exc() 
    except mariadb.DataError:
        print("\nInvalid data being passed to the database.\n")
        traceback.print_exc()
    except mariadb.DatabaseError:
        print(f"\nAn error has occured in the database. Failed to retrieve @{hacker_login_alias}'s exploits.\n")
        traceback.print_exc()

    close_db_and_cursor(cursor, conn)

def enter_new_exploit(hacker_login_alias, hacker_login_id):
    conn = open_db_connection()

    cursor = open_cursor(conn)

    while(True):
        try:
            print(f"\nNew Exploit by @{hacker_login_alias}")
            print("------------------------------ \n")
            exploit_content_string = input("Enter text here: \n\n")
            if(exploit_content_string == ""):
                print("Invalid entry. Please re-enter your entry.")
            else:
                exploit_content_escape = re.sub(r"\'", r"\\'", exploit_content_string)
                cursor.execute("INSERT INTO exploits(content, hacker_id) VALUES(?, ?)", [exploit_content_escape, hacker_login_id])
                conn.commit()
                print(f"\n@{hacker_login_alias}'s exploit was successfully uploaded.")
                break
        except mariadb.OperationalError:
            print(f"\nErrors in method of retrieving @{hacker_login_alias}'s exploits.\n")
            traceback.print_exc()
        except mariadb.ProgrammingError:
            print(f"\nUnable to escape metacharacters in @{hacker_login_alias}'s exploit. Failed to upload @{hacker_login_alias}'s exploit to the database.\n")
            traceback.print_exc()
        except mariadb.NotSupportedError:
            print("\nInvalid MariaDB syntax.\n")
            traceback.print_exc() 
        except mariadb.DataError:
            print("\nInvalid data being passed to the database.\n")
            traceback.print_exc()
        except mariadb.DatabaseError:
            print(f"\nAn error has occured in the database. Failed to retrieve @{hacker_login_alias}'s exploits.\n")
            traceback.print_exc()
        except:
            print(f"\nAn error occured. Failed to upload @{hacker_login_alias}'s exploit.\n")
            traceback.print_exc()

    close_db_and_cursor(cursor, conn)

def show_options(hacker_login_alias, hacker_login_id):
    while(True):
        try:
            print("\nPlease select one of the following options:\n1: Enter a New Exploit\n2: View My Exploits\n3: Modify My Exploits\n4: View Other Exploits\n5: Exit the Application")
            selection = int(input("\nPlease enter your selection: "))
            if(selection == 1):
                enter_new_exploit(hacker_login_alias, hacker_login_id)
            elif(selection == 2):
                view_my_exploits(hacker_login_alias, hacker_login_id)
            elif(selection == 3):
                modify_my_exploits(hacker_login_alias, hacker_login_id)
            elif(selection == 4):
                view_other_exploits(hacker_login_alias, hacker_login_id)
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

def check_hacker_login():
    conn = open_db_connection()
    cursor = open_cursor(conn)

    if(conn == None or cursor == None):
        print("An error in the database has occured.")
        dbconnect.close_cursor(cursor)
        dbconnect.close_db_connection(conn)
        return

    try:
        print("\nLogin")
        print("-----\n")
        hacker_login_alias = input("Please enter your username: ")
        hacker_login_password = input("Please enter your password: ")
        cursor.execute("SELECT * FROM hackers WHERE alias = ? AND password = ?", [hacker_login_alias, hacker_login_password])
        database_login_info = cursor.fetchall()
        if(cursor.rowcount == 1):
            print("\nYou have successfully logged in.")
            show_options(hacker_login_alias, database_login_info[0][0])
            return
        else:
            print("\nThe username and password do not match our records. Please re-enter your login information.")
    except mariadb.OperationalError:
        print(f"\nFailed to connect to the database. Unable to retrieve @{hacker_login_alias}'s login information.\n")
        traceback.print_exc()
    except mariadb.DatabaseError:
        print(f"\nAn error has occured in the database. Failed to retrieve @{hacker_login_alias}'s login information.\n")
        traceback.print_exc()
    except mariadb.DataError:
        print("\nYour username and password has exceed the limit of 20 characters. Please re-enter your login information.\n")
        traceback.print_exc()
    except mariadb.ProgrammingError:
        print("\nInvalid SQL syntax.\n")
        traceback.print_exc()
    except mariadb.NotSupportedError:
        print("\nInvalid MariaDB syntax.\n")
        traceback.print_exc()

    close_db_and_cursor(cursor, conn)

def signup_hacker():
    conn = open_db_connection()
    cursor = open_cursor(conn)

    if(conn == None or cursor == None):
        print("An error in the database has occured.")
        dbconnect.close_cursor(cursor)
        dbconnect.close_db_connection(conn)
        return

    print("\nWelcome to the Underground Social Media Site!")
    try:
        print("\nSignup")
        print("------\n")

        hacker_signup_alias = input("Create a username: ")
        hacker_signup_password = input("Create a password: ")

        cursor.execute("INSERT INTO hackers(alias, password) VALUES(?, ?)", [hacker_signup_alias, hacker_signup_password])
        cursor.commit()

        if(cursor.rowcount == 1):
            print(f"Your hacker ID is {cursor.lastrowid}\n")
            print("\nYou have successfully created an account. Please verify your credentials by logging into our system.")
            check_hacker_login()
            return 
        else:
            print("\nFailed to create an account.")
    except AttributeError:
        print("Failed to commit changes to the database.")
        cursor.commit()
        traceback.print_exc()
    except mariadb.IntegrityError:
        print(f"\nUsername is already taken. Please enter another username.\n")
        traceback.print_exc()
    except mariadb.OperationalError:
        print(f"\nFailed to connect to the database. Unable to create an account.\n")
        traceback.print_exc()
    except mariadb.DatabaseError:
        print(f"\nAn error has occured in the database. Failed to create an account.\n")
        traceback.print_exc()
    except mariadb.DataError:
        print("\nYour username or password has exceed the limit of 20 characters. Please re-enter your information.\n")
        traceback.print_exc()
    except mariadb.ProgrammingError:
        print("\nInvalid SQL syntax.\n")
        traceback.print_exc()
    except mariadb.NotSupportedError:
        print("\nInvalid MariaDB syntax.\n")
        traceback.print_exc()

    close_db_and_cursor(cursor, conn)

def open_db_connection():
    conn = dbconnect.open_db_connection()
    return conn

def open_cursor(conn):
    cursor = dbconnect.create_db_cursor(conn)
    return cursor

def close_db_and_cursor(cursor, conn):
    dbconnect.close_cursor(cursor)
    dbconnect.close_db_connection(conn)

# while(True):
#     is_hacker_signed_up = signup_hacker()
#     if(is_hacker_signed_up != None):
#         hacker_login_id = check_hacker_login()
#         break
#     else:
#         continue

# signup_hacker()

check_hacker_login()