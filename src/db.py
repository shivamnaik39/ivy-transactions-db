import sqlite3
from src.filter import *
# Function to create tables from an SQL file


def create_tables_from_sql(sql_file, db_file):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()

    with open(sql_file, 'r') as f:
        sql_commands = f.read()

    cursor.executescript(sql_commands)

    conn.commit()
    conn.close()

# Function to insert data into tables


# Function to insert accounts into tables
def insert_accounts(db_file, accounts):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()

    accounts_data_string = "INSERT INTO accounts(account_id,name) VALUES (?,?)"

    cursor.executemany(accounts_data_string, accounts)

    conn.commit()
    conn.close()


def insert_categories(db_file, categories):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()

    categories_data_string = "INSERT INTO categories(category_id,name) VALUES (?,?)"

    cursor.executemany(categories_data_string, categories)

    conn.commit()
    conn.close()


def insert_transactions_json(db_file, transactions):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()

    transactions_data_string = """INSERT INTO transactions(transaction_id, account_id, category_id,
    amount, date_time, title, description, to_account_id, to_amount, transaction_type) 
    VALUES (?,?,?,?,?,?,?,?,?,?)"""

    cursor.executemany(transactions_data_string, transactions)

    conn.commit()
    conn.close()
    
    
def insert_transactions_csv(db_file, transactions):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()

    transactions_data_string = """INSERT INTO transactions(transaction_id, account, category,
    amount, date_time, title, description, to_account, to_amount, transaction_type) 
    VALUES (?,?,?,?,?,?,?,?,?,?)"""

    cursor.executemany(transactions_data_string, transactions)

    conn.commit()
    conn.close()

