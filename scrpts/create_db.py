__author__ = 'kuroi'
if not os.path.exists(db_path_name):                                # if there is no such file or dir
        db_connection = sqlite3.connect(db_path_name)                   # create one, connect and create a table.
        db_connection.execute('PRAGMA foreign_keys = ON')               # foreign_keys are off by default
        db_connection.execute('''CREATE TABLE NAMES (
        CUSTOMER_ID     INT     PRIMARY KEY NOT NULL,
        NAME    TEXT    NOT NULL,
        PHONE   INT,    COMMENT TEXT,
        AGREED  TEXT    NOT NULL
        )''')
        db_connection.execute('''CREATE TABLE NOTIFY (
        ID      INT     PRIMARY KEY NOT NULL,
        CUSTOMER_ID     INT         NOT NULL,
        P_DATE  TEXT    NOT NULL,   C_DATE      TEXT    NOT_NULL,
        INFORMED    TEXT    NOT NULL,
        CONTRACT    TEXT    NOT NULL,
        B_B     TEXT    NOT NULL,   B_A         TEXT    NOT NULL
        )''')
        db_connection.close()

if not os.path.isfile(db_path_name):                                # if the given path and name exist
    print('something wrong with database file. shutting down')      # something is broken.
    return