import sql_create as sc
import to_db as db
from time import sleep
import query as q


def main():
    database = "database\\python_sqlite.db"  # declares the database location
    sql_create_csv_table = """CREATE TABLE IF NOT Exists answer_log_csv (
                                   transaction_id bigint,
                                   session VARCHAR (120),
                                   concept_id VARCHAR (120),
                                   value text)
                                   ;"""  # Create table declaration and only creates the table if it doesn't exist
    # create a database connection
    conn = sc.create_connection(database)  # connects to the database
    if conn is not None:
        sc.create_table(conn, sql_create_csv_table)  # create answer log table
        # yaml = db.DataObjects(r'data\\config.yml').set_config()  # not used as I am using SQLite
        db.DataObjects(r'data\\config.yml').csv_file(r'data/answers_log.csv', conn)  # Loads the csv file
        print('Data has been imported to the sqlite database in the database folder of the project')
        q.query(conn, 'select * from answer_log_csv')  # Executes the sql statement to show it has been loaded
        sleep(10)
    else:
        print("Error! Cannot create the database connection. Please contact the admin.")


if __name__ == '__main__':
    main()  # Only runs the main function when execute this file
