import mariadb
import dbconnect
import traceback
import options_menu

def check_hacker_login():
    conn = dbconnect.open_db_connection()
    cursor = dbconnect.create_db_cursor(conn)

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
            print(f"\nWelcome back, @{hacker_login_alias}.")
            options_menu.show_options(hacker_login_alias, database_login_info[0][0])
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

    dbconnect.close_cursor(cursor)
    dbconnect.close_db_connection(conn)