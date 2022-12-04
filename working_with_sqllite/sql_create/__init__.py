import sqlite3


def create_connection(db_file):
    """Create a database connection to a SQLite database
    :param db_file: database file
    :return: Connection object or None
    """
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except sqlite3.Error as e:
        print(e)
    return None


def create_table(conn, create_table_sql):
    """Create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(
            create_table_sql
        )  # TODO: this should have some checks to make sure it's actually a create table statement
    except sqlite3.Error as e:
        print(e)
