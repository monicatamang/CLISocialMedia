import dbcreds
import mariadb
import traceback

# Creating a function that opens that database connection
def open_db_connection():
    # Using a try-except block to catch errors when connecting to the database
    try:
        # Trying to return the connection object to the caller
        return mariadb.connect(user=dbcreds.user, password=dbcreds.password, host=dbcreds.host, port=dbcreds.port, database=dbcreds.database)
    # If there is a connection failure, raise the following exceptions, print an error message to the hacker and the traceback
    except mariadb.OperationalError:
        # An OperationalError exception is raised for things that are not in control of the programmer such as an unexpected connection failure, server shutting down, etc.
        print("\nOperational errors detected in the database connection.\n")
        traceback.print_exc()
    except mariadb.DatabaseError:
        # A DatabaseError exception is raised for all errors that are related to the database
        print("\nError detected in the database and resulted in a connection failure.\n")
        traceback.print_exc()
    except:
        # Catching all other errors
        print("\nAn error has occured. Failed to connect to the database.\n")
        traceback.print_exc()
        return None

# Creating a function that returns a cursor object using the current connection, which is passed as an argument
def create_db_cursor(conn):
    # Using a try-except block to catch errors when creating a cursor
    try:
        # Trying to return a cursor object using the current connection
        return conn.cursor()
    # If the cursor object cannot be created, raise the following exceptions, print an error message to the hacker and the traceback
    except mariadb.InternalError:
        # An InternalError exception is raised if a cursor is invalid, database transcations out of sync, etc.
        print("\nInternal errors detected in the database. Failed to create a cursor.\n")
        traceback.print_exc()
    except mariadb.OperationalError:
        # An OperationalError exception is raised for things that are not in control of the programmer such as an unexpected connection failure, server shutting down, etc.
        print("\nOperational errors detected in the database connection. Failed to create a cursor.\n")
        traceback.print_exc()
    except mariadb.DatabaseError:
        # A DatabaseError exception is raised for all errors that are related to the database
        print("\nErrors detected in database. Failed to create a cursor.\n")
        traceback.print_exc()
    except:
        # Catching all other errors
        print("\nAn error has occured. Failed to create a cursor.\n")
        traceback.print_exc()
        return None

# Creating a function that closes the cursor
def close_cursor(cursor):
    # Checking to see if the cursor was initially created and if it wasn't, don't attempt to close the cursor
    if(cursor == None):
        return True
    # Using a try-except block to catch errors when closing the cursor
    try:
        # Trying to close the cursor, returning "True" to indicate that the cursor was closed successfully
        cursor.close()
        return True
    # If the cursor failed to close, raise the following exceptions, print an error message to the hacker and the traceback
    except mariadb.InternalError:
        # An InternalError exception is raised if a cursor is invalid, database transcations out of sync, etc.
        print("\nInternal errors detected in the database. Failed to create a cursor.\n")
        traceback.print_exc()
    except mariadb.OperationalError:
        # An OperationalError exception is raised for things that are not in control of the programmer such as an unexpected connection failure, server shutting down, etc.
        print("\nOperational errors detected in the database connection. Failed to create a cursor.\n")
        traceback.print_exc()
    except mariadb.DatabaseError:
        # A DatabaseError exception is raised for all errors that are related to the database
        print("\nErrors detected with the current connection. Failed to close cursor.\n")
        traceback.print_exc()
    except:
        # Catching all other errors
        print("An error has occured. Failed to close cursor.")
        traceback.print_exc()
        return False

# Creating a function that closes the database connection
def close_db_connection(conn):
    # If the database connect was not initially opened, don't attempt to close it
    if(conn == None):
        return True
    # Using a try-except block to catch errors when closing the database connection
    try:
        # Trying to close the connection, returning "True" to indicate that the connection was close successfully
        conn.close()
        return True
    # If the connection failed closed, raise the following exceptions, print an error message to the hacker and the traceback
    except mariadb.OperationalError:
        # An OperationalError exception is raised for things that are not in control of the programmer such as an unexpected connection failure, server shutting down, etc.
        print("\nOptional errors detected in the database. Failed to close the connection.\n")
        traceback.print_exc()
    except mariadb.DatabaseError:
        # A DatabaseError exception is raised for all errors that are related to the database
        print("Errored detected in the database. Failed to close the connection.")
        traceback.print_exc()
    except:
        # Catching all other errors
        print("An error has occured. Failed to close database connection.")
        traceback.print_exc()
        return False