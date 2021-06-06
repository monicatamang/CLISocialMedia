import mariadb
import dbconnect
import traceback
# import re

def view_other_exploits(hacker_alias, hacker_id):
    conn = dbconnect.open_db_connection()
    cursor = dbconnect.create_db_cursor(conn)
    check_db_and_cursor_connection(conn, cursor)

    try:
        cursor.execute("SELECT h.alias, e.content FROM cli_social_media.hackers h INNER JOIN cli_social_media.exploits e ON e.hacker_id = h.id WHERE h.id != ?", [hacker_id])
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
        print(f"\nErrors found in database contraints. Failed to retrieve @{hacker_alias}'s exploits.\n")
        traceback.print_exc()
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

    close_db_and_cursor(cursor, conn)

def modify_my_exploits(hacker_alias, hacker_id):
    conn = dbconnect.open_db_connection()
    cursor = dbconnect.create_db_cursor(conn)
    check_db_and_cursor_connection(conn, cursor)

    print("\nPlease choose which exploit you would like to modify.")

    while(True):
        try:
            cursor.execute("SELECT e.id, h.alias, e.content, h.id, e.hacker_id FROM hackers h INNER JOIN exploits e ON e.hacker_id = h.id WHERE h.id = ?", [hacker_id])
            my_exploits = cursor.fetchall()
            if(len(my_exploits) == 0):
                print("\nNo posts found.")
                break
            else:
                print("\nMy Exploits")
                print("-----------")
                for exploit in my_exploits:
                    print(f"\nExploit #{exploit[0]} by @{exploit[1]}\n")
                    print(f"{exploit[2]}\n")
                    print(f"Hacker ID: {exploit[3]}\n")
                    print("------------------------------\n")

            exploit_selection = int(input("Please enter the exploit number of the exploit you would like to modify: "))
            
            print(f"\nModifying Exploit #{exploit_selection} by @{hacker_alias}")
            print("------------------------------ \n")
            new_exploit_string = input("Enter text here: \n\n")
            if(new_exploit_string == ""):
                print("Invalid entry. Please re-enter your entry.")
            else:
                # new_exploit_escape = re.sub(r"\'", r"\\'", new_exploit_string)
                cursor.execute("SELECT content FROM exploits e WHERE e.id = ? AND e.hacker_id = ?", [exploit_selection, hacker_id])
                old_exploit = cursor.fetchall()
                
                cursor.execute("UPDATE exploits SET content = ? WHERE content = ?", [new_exploit_string, old_exploit[0][0]])
                conn.commit()

                print(f"\n@{hacker_alias}'s exploit was successfully updated.")
                break
        except IndexError:
            print(f"\n@{hacker_alias} is not authorized to modify Exploit #{exploit_selection}.\n")
            traceback.print_exc()
        except ValueError:
            print("\nInvlaid data entry. Expected a numerical type. Please re-enter the exploit number.\n")
            traceback.print_exc()
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
    
    close_db_and_cursor(cursor, conn)

def view_my_exploits(hacker_alias, hacker_id):
    conn = dbconnect.open_db_connection()
    cursor = dbconnect.create_db_cursor(conn)
    check_db_and_cursor_connection(conn, cursor)

    try:
        cursor.execute("SELECT e.id, h.alias, e.content, h.id FROM hackers h INNER JOIN exploits e ON e.hacker_id = h.id WHERE h.id = ?", [hacker_id])
        my_exploits = cursor.fetchall()
        if(len(my_exploits) == 0):
            print("\nNo posts found.")
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

    close_db_and_cursor(cursor, conn)

def enter_new_exploit(hacker_alias, hacker_id):
    
    conn = dbconnect.open_db_connection()
    cursor = dbconnect.create_db_cursor(conn)
    check_db_and_cursor_connection(conn, cursor)

    while(True):
        try:
            print(f"\nNew Exploit by @{hacker_alias}")
            print("------------------------------ \n")
            exploit_content_string = input("Enter text here: \n\n")
            if(exploit_content_string == ""):
                print("Invalid entry. Please re-enter your entry.")
            else:
                # exploit_content_escape = re.sub(r"\'", r"\\'", exploit_content_string)
                cursor.execute("INSERT INTO exploits(content, hacker_id) VALUES(?, ?)", [exploit_content_string, hacker_id])
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

    close_db_and_cursor(cursor, conn)

def check_db_and_cursor_connection(conn, cursor):
    if(conn == None or cursor == None):
        print("An error in the database has occured.")
        dbconnect.close_cursor(cursor)
        dbconnect.close_db_connection(conn)
        return

def close_db_and_cursor(cursor, conn):
    dbconnect.close_cursor(cursor)
    dbconnect.close_db_connection(conn)