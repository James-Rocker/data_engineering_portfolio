import psycopg2


class Postgres:
    def __init__(self):
        self.connection = psycopg2.connect(
            user="postgres",
            password="postgres",  # don't ever do this in any environment, use env or secrets
            host="localhost",
            port="5432",
            database="postgres",
        )
        self.cursor = self.connection.cursor()

        # Create a cursor to perform database operations
        print(
            "PostgreSQL server connection params", self.connection.get_dsn_parameters()
        )
        self.cursor.execute("SELECT version();")
        print("You are connected to - ", self.cursor.fetchone(), "\n")


Postgres()
