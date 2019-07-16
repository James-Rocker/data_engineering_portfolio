import sqlite3


def query(conn, query_txt):
    """
    Takes the connection file variable and executes the query text within that connection
    :param conn:
    :param query_txt:
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(query_txt)
        rows = c.fetchall()
        for row in rows:
            print(row)
    except sqlite3.Error as e:
        print(e)
