import sqlite3


def query(conn, query_txt):
    try:
        c = conn.cursor()
        c.execute(query_txt)
        rows = c.fetchall()
        for row in rows:
            print(row)
    except sqlite3.Error as e:
        print(e)
