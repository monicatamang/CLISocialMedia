import traceback
import dbcreds
import mariadb

def open_db_connection():
    try:
        return mariadb.connect(user=dbcreds.user, password=dbcreds.password, host=dbcreds.host, port=dbcreds.port, database=dbcreds.database)
    except mariadb.OperationalError:
        print("Failed to connect to the database.")
        traceback.print_exc()
    except mariadb.DatabaseError:
        print("Failed to connect to the database.")
        traceback.print_exc()
    except:
        print("An error has occured. Failed to connect to the database.")
        traceback.print_exc()
        return None

def create_db_cursor(conn):
    try:
        return conn.cursor()
    except mariadb.DatabaseError:
        print("Failed to connect to the database. Failed to create a cursor.")
        traceback.print_exc()
    except mariadb.InternalError:
        print("Failed to create a cursor.")
        traceback.print_exc()
    except:
        print("An error has occured. Failed to create a cursor.")
        traceback.print_exc()
        return None

def close_cursor(cursor):
    # If the cursor was initially not created, don't close it
    if(cursor == None):
        return True
    try:
        cursor.close()
        return True
    except mariadb.DatabaseError:
        print("Failed to connect to the database. Failed to create a cursor.")
        traceback.print_exc()
    except mariadb.InternalError:
        print("Failed to create a cursor.")
        traceback.print_exc()
    except:
        print("An error has occured. Failed to close cursor.")
        traceback.print_exc()
        return False

def close_db_connection(conn):
    # If the database connection was initially not opened, don't close it
    if(conn == None):
        return True
    try:
        conn.close()
        return True
    except mariadb.OperationalError:
        print("Failed to close the database connection.")
        traceback.print_exc()
    except mariadb.DatabaseError:
        print("Failed to close the database connection.")
        traceback.print_exc()
    except:
        print("An error has occured. Failed to close database connection.")
        traceback.print_exc()
        return False