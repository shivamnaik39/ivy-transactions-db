import csv
from src.fetch_json import remove_emojis
from config.logger import get_logger
from src.utils.helper import convert_timestamp_to_datetime, convert_to_sql_datetime


logger = get_logger("FETCH_CSV")


def get_data_csv(file_path):
    try:
        with open(file=file_path, mode='r', encoding='utf-16') as csv_file:
            csv_reader = csv.DictReader(csv_file, skipinitialspace=True)
            filtered_transactions = filter_transactions(csv_reader)

    except Exception as e:
        print(f"error: {e}")

    return filtered_transactions


def filter_transactions(transactions):
    logger.debug("filtering transactions into the tuple.")
    filtered_transactions = []
    for transaction in transactions:
        if transaction.get('Date') == "":
            continue
      #  or None is used to get None as the value if the dictionary has empty strings
        transaction_id = transaction.get('ID', None) or None
        account_id = transaction.get('Account', None) or None
        category_id = transaction.get('Category', None) or None
        amount = transaction.get('Amount', None) or None
        date_time = convert_to_sql_datetime(
            transaction.get('Date', None)) or None
        title = remove_emojis(transaction.get('Title', None)) or None
        description = remove_emojis(
            transaction.get('Description', None)) or None
        to_account_id = transaction.get('To Account', None) or None
        to_amount = transaction.get('Transfer Amount', None) or None
        transaction_type = transaction.get('Type', None) or None
        transaction_record = (transaction_id, account_id, category_id, amount,
                              date_time, title, description, to_account_id, to_amount, transaction_type)
        filtered_transactions.append(transaction_record)

    return filtered_transactions
