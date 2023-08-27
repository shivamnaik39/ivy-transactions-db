from src.db import *
from src.fetch_json import get_data_json
from src.fetch_csv import get_data_csv
import os
from config.logger import get_logger

logger = get_logger("App")


def main():
    has_erros = False
    cwd = os.getcwd()
    sql_file_json = os.path.join(cwd, 'src/schema/schema_json.sql')
    sql_file_csv = os.path.join(cwd, 'src/schema/schema_csv.sql')
    db_file = os.path.join(cwd, 'data/transactions.db')
    json_file = os.path.join(cwd, 'data/transactions.json')
    csv_file = os.path.join(cwd, 'data/transactions.csv')

    try:
        # Create tables from sql schema
        create_tables_from_sql(sql_file_csv, db_file)
        logger.info("Tables created successfully.")

        # Fetch all the filtered records from the json file
        # data = get_data_json(json_file)
        # logger.info("Data fetched and filtered from the JSON file.")

        # Fetch all the filtered records from the csv file
        transactions = get_data_csv(csv_file)
        logger.info("Data fetched and filtered from the CSV file.")

        # # Extract the required record tuples separately
        # accounts = data['accounts']
        # categories = data['categories']
        # transactions = data['transactions']

        #  Insert all the records into the respective tables
        # insert_accounts(db_file, accounts)
        # insert_categories(db_file, categories)
        insert_transactions(db_file, transactions)
        logger.info("Data inserted into the tables successfully.")
        logger.info(f"Sqlite database created and stored at: {db_file} ")

    except Exception as e:
        has_erros = True
        logger.error(e)

    finally:
        if has_erros:
            logger.error("App finished execution with some error!")

        else:
            logger.info("App finished execution successfully.")


if __name__ == '__main__':
    main()
