import sqlite3


def execute_with_output(conn, query_txt, fetch_quant="one"):
    """
    Takes the connection file variable and executes the query text within that connection
    :param fetch_quant:
    :param conn:
    :param query_txt:
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(query_txt)
        if fetch_quant == "one":
            return c.fetchone()
        else:
            return c.fetchall()
    except sqlite3.Error as e:
        print(e)
