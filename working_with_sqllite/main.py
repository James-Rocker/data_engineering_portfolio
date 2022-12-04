import sqlite3

import sql_create as sc
import to_db as db
import query


class SqlLiteConnection:
    def __init__(self):
        self.connection = sc.create_connection(
            "database\\python_sqlite.db"
        )  # connects to the database
        self.destination_table = "answer_log_csv"

    def create_table_load_file(self):
        # create a database connection
        sql_create_csv_table = f"""CREATE TABLE IF NOT Exists {self.destination_table} (
                                       transaction_id bigint,
                                       session VARCHAR (120),
                                       concept_id VARCHAR (120),
                                       value text)
                                       ;"""  # Create table declaration and only creates the table if it doesn't exist
        if self.connection is not None:
            self.connection.execute(sql_create_csv_table)
            sc.create_table(
                self.connection, sql_create_csv_table
            )  # create answer log table
            query.execute_with_output(
                self.connection, f"delete from {self.destination_table}"
            )  # if the table does exist then it should be clear
            db.DataObjects(self.connection).load_csv_file(
                "./data/answers_log.csv",
            )
            print(
                "Data has been imported to the sqlite database in the database folder of the project"
            )
        else:
            print(
                "Error! Cannot create the database connection. Please contact the admin."
            )

    def check_data_exists(self):
        # Checks data has been loaded
        if self.connection is not None:
            try:
                output = query.execute_no_output(
                    self.connection, f"select count(*) from {self.destination_table};"
                )
                return output
            except sqlite3.Error as err:
                print(err, err.__traceback__)


if __name__ == "__main__":
    db_initialise = SqlLiteConnection()
    db_initialise.create_table_load_file()  # Only runs the main function when execute this file
    print(db_initialise.check_data_exists())
