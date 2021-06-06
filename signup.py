import mariadb
import dbconnect
import traceback
import options_menu

def signup_hacker():
    conn = dbconnect.open_db_connection()
    cursor = dbconnect.create_db_cursor(conn)

    if(conn == None or cursor == None):
        print("An error in the database has occured.")
        dbconnect.close_cursor(cursor)
        dbconnect.close_db_connection(conn)
        return

    try:
        print("\nSignup")
        print("------\n")

        hacker_signup_alias = input("Create a username: ")
        hacker_signup_password = input("Create a password: ")

        if(hacker_signup_alias == "" or hacker_signup_password == ""):
            print("\nInvalid signup information. Please enter valid credentials to create an account.")
        else:
            cursor.execute("INSERT INTO hackers(alias, password) VALUES(?, ?)", [hacker_signup_alias, hacker_signup_password])
            conn.commit()

            if(cursor.rowcount == 1):
                print(f"\nWelcome, @{hacker_signup_alias}. Your Hacker ID is {cursor.lastrowid}")
                options_menu.show_options(hacker_signup_alias, cursor.lastrowid)
                return
            else:
                print("\nFailed to create an account.")
    except AttributeError:
        print("Failed to commit changes to the database.")
        cursor.commit()
        traceback.print_exc()
    except mariadb.IntegrityError:
        print(f"\n@{hacker_signup_alias} is already taken. Please enter another username.\n")
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

    dbconnect.close_cursor(cursor)
    dbconnect.close_db_connection(conn)