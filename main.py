import sql_create as sc
import to_db as db
from time import sleep


def main():
    database = "database\\python_sqlite.db"
    sql_create_csv_table = """CREATE TABLE IF NOT Exists answer_log_csv (
                                   transaction_id bigint,
                                   session VARCHAR (120),
                                   concept_id VARCHAR (120),
                                   value text)
                                   ;"""
    # create a database connection
    conn = sc.create_connection(database)
    if conn is not None:
        # create answer log table
        sc.create_table(conn, sql_create_csv_table)
        # yaml = db.DataObjects(r'data\\config.yml').set_config()  # not used as I am using SQLite
        db.DataObjects(r'data\\config.yml').csv_file(r'data/answers_log.csv', conn)
        print('Data has been imported to the sqlite database in the database folder of the project')
        sleep(10)
    else:
        print("Error! Cannot create the database connection. Please contact the admin.")


if __name__ == '__main__':
    main()
