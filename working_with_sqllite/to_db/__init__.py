import csv


class DataObjects(object):
    def __init__(self, connection):
        """
        :param connection:
        """
        self.db_connection = connection

    def load_csv_file(self, csv_file):
        """
        :param csv_file: file to load the data
        :return: load the file as a csv in the cache
        """
        with open(csv_file, "r") as file:
            reader = csv.reader(file)
            columns = next(reader)  # treat the columns as an iterable
            query = "insert into answer_log_csv ({0}) values ({1})"
            # using this format method because we don't know the column quantity
            query = query.format(",".join(columns), ",".join("?" * len(columns)))
            cursor = self.db_connection.cursor()
            insert_count = 0
            for data in reader:
                cursor.execute(query, data)
                # connection.set_trace_callback(print) # if you want to see the query
                insert_count += 1
            print(f"loading {insert_count} lines into SQLLite db")
            print(f"csv file {csv_file} has been loaded to SQLLite")
