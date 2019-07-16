import yaml
import csv


class DataObjects(object):
    def __init__(self, config_filepath):
        """
        :param config_filepath: A config.yml file containing credentials for databases you're using. (required)
        """
        self.config_filepath = config_filepath
        self.config_dictionary = self.set_config()

    def set_config(self):
        """
        :return: returns yaml config object
        """
        mydict = yaml.safe_load(open(self.config_filepath))
        return mydict

    def csv_file(self, csv_file, connection):
        """
        :param connection: sql db connection
        :param csv_file: file to load the data
        :return: load the file as a csv in the cache
        """
        with open(csv_file, 'r') as file:
            reader = csv.reader(file)
            columns = next(reader)
            query = 'insert into answer_log_csv({0}) values ({1})'
            query = query.format(','.join(columns), ','.join('?' * len(columns)))
            cursor = connection.cursor()
            for data in reader:
                cursor.execute(query, data)
        # return df

