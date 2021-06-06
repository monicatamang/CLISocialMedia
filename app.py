import mariadb
import dbconnect
import traceback
import re

def view_other_exploits(hacker_alias, hacker_login_id):
    conn = dbconnect.open_db_connection()
    cursor = dbconnect.create_db_cursor(conn)
    try:
        cursor.execute("SELECT e.id, h.alias, e.content, h.id FROM cli_social_media.hackers h INNER JOIN cli_social_media.exploits e ON e.hacker_id = h.id WHERE h.id != ?", [hacker_login_id])
        other_exploits = cursor.fetchall()
        if(len(other_exploits) == 0):
            print("\nNo posts found.\n")
        else:
            print("\nOther Exploits")
            print("--------------")
            for exploit in other_exploits:
                print(f"\nExploit #{exploit[0]} by @{exploit[1]}\n")
                print(f"{exploit[2]}\n")
                print(f"Hacker ID: {exploit[3]}\n")
                print("------------------------------")
    except mariadb.IntegrityError:
        print(f"\nErrors found in database contraints. Failed to retrieve @{hacker_alias}'s exploits.\n")
    except mariadb.OperationalError:
        print(f"\nFailed to connect to the database. Unable to retrieve @{hacker_alias}'s exploits\n")
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
        print(f"\nAn error has occured in the database. Failed to retrieve @{hacker_alias}'s exploits.\n")
        traceback.print_exc()
    except:
        print("\nAn error has occurred.\n")
        traceback.print_exc()
    dbconnect.close_cursor(cursor)
    dbconnect.close_db_connection(conn)

def view_my_exploits(hacker_alias, hacker_login_id):
    conn = dbconnect.open_db_connection()
    cursor = dbconnect.create_db_cursor(conn)
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
        print(f"\nErrors found in database contraints. Failed to retrieve @{hacker_alias}'s exploits.\n")
        traceback.print_exc()
    except mariadb.OperationalError:
        print(f"\nErrors in method of retrieving @{hacker_alias}'s exploits.\n")
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
        print(f"\nAn error has occured in the database. Failed to retrieve @{hacker_alias}'s exploits.\n")
        traceback.print_exc()
    dbconnect.close_cursor(cursor)
    dbconnect.close_db_connection(conn)

def enter_new_exploit(hacker_alias, hacker_login_id):
    conn = dbconnect.open_db_connection()
    cursor = dbconnect.create_db_cursor(conn)
    while(True):
        try:
            print(f"\nNew Exploit by @{hacker_alias}")
            print("------------------------------ \n")
            exploit_content_string = input("Enter text here: \n\n")
            if(exploit_content_string == ""):
                print("Invalid entry. Please re-enter your entry.")
            else:
                exploit_content_escape = re.sub(r"\'", r"\\'", exploit_content_string)
                cursor.execute("INSERT INTO exploits(content, hacker_id) VALUES(?, ?)", [exploit_content_escape, hacker_login_id])
                conn.commit()
                print(f"\n@{hacker_alias}'s exploit was successfully uploaded.")
                break
        except mariadb.OperationalError:
            print(f"\nErrors in method of retrieving @{hacker_alias}'s exploits.\n")
            traceback.print_exc()
        except mariadb.ProgrammingError:
            print(f"\nUnable to escape metacharacters in @{hacker_alias}'s exploit. Failed to upload @{hacker_alias}'s exploit to the database.\n")
            traceback.print_exc()
        except mariadb.NotSupportedError:
            print("\nInvalid MariaDB syntax.\n")
            traceback.print_exc() 
        except mariadb.DataError:
            print("\nInvalid data being passed to the database.\n")
            traceback.print_exc()
        except mariadb.DatabaseError:
            print(f"\nAn error has occured in the database. Failed to retrieve @{hacker_alias}'s exploits.\n")
            traceback.print_exc()
        except:
            print(f"\nAn error occured. Failed to upload @{hacker_alias}'s exploit.\n")
            traceback.print_exc()
    dbconnect.close_cursor(cursor)
    dbconnect.close_db_connection(conn)

def show_options(hacker_alias, hacker_login_id):
    while(True):
        try:
            print("\nPlease select one of the following options:\n1: Enter a New Exploit\n2: View My Exploits\n3: View Other Exploits\n4: Exit the Application")
            selection = int(input("\nPlease enter your selection: "))
            if(selection == 1):
                enter_new_exploit(hacker_alias, hacker_login_id)
            elif(selection == 2):
                view_my_exploits(hacker_alias, hacker_login_id)
            elif(selection == 3):
                view_other_exploits(hacker_alias, hacker_login_id)
            elif(selection == 4):
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
    conn = dbconnect.open_db_connection()
    cursor = dbconnect.create_db_cursor(conn)
    if(conn == None or cursor == None):
        print("An error in the database has occured.")
        dbconnect.close_cursor(cursor)
        dbconnect.close_db_connection(conn)
        return
    try:
        print("\nWelcome to the Underground Social Media Site!")
        print("\nLogin")
        print("-----\n")
        hacker_alias = input("Please enter your username: ")
        hacker_password = input("Please enter your password: ")
        cursor.execute("SELECT * FROM hackers WHERE alias = ? AND password = ?", [hacker_alias, hacker_password])
        database_login_info = cursor.fetchall()
        if(cursor.rowcount == 1):
            print("\nYou have successfully logged in.")
            show_options(hacker_alias, database_login_info[0][0])
        else:
            print("\nThe username and password do not match our records. Please re-enter your login information.")
    except mariadb.OperationalError:
        print(f"\nFailed to connect to the database. Unable to retrieve @{hacker_alias}'s login information.\n")
        traceback.print_exc()
    except mariadb.DatabaseError:
        print(f"\nAn error has occured in the database. Failed to retrieve @{hacker_alias}'s login information.\n")
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
    dbconnect.close_cursor(cursor)
    dbconnect.close_db_connection(conn)

hacker_login_id = check_hacker_login()