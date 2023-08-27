from datetime import datetime
import json
import re

import pytz

from config.logger import get_logger
from src.utils.helper import convert_timestamp_to_datetime, remove_emojis
# function to get required data from json file

logger = get_logger("FETCH_JSON")

def filter_accounts(accounts):
    logger.debug("filtering accounts into the tuple.")
    filtered_accounts = []
    for account in accounts:
        account_id = account['id']
        name = account['name']
        account_record = (account_id, name)
        filtered_accounts.append(account_record)

    return filtered_accounts


def filter_categories(categories):
    logger.debug("filtering categories into the tuple.")
    filtered_categories = []
    for category in categories:
        category_id = category['id']
        name = category['name']
        category_record = (category_id, name)
        filtered_categories.append(category_record)

    return filtered_categories


def filter_transactions(transactions):
    logger.debug("filtering transactions into the tuple.")
    filtered_transactions = []
    for transaction in transactions:
        transaction_id = transaction.get('id', None)
        account_id = transaction.get('accountId', None)
        category_id = transaction.get('categoryId', None)
        amount = transaction.get('amount', None)
        date_time = convert_timestamp_to_datetime(
            transaction.get('dateTime', None))
        title = remove_emojis(transaction.get('title', None))
        description = remove_emojis(transaction.get('description', None))
        to_account_id = transaction.get('toAccountId', None)
        to_amount = transaction.get('toAmount', None)
        transaction_type = transaction.get('type', None)
        transaction_record = (transaction_id, account_id, category_id, amount,
                              date_time, title, description, to_account_id, to_amount, transaction_type)
        filtered_transactions.append(transaction_record)

    return filtered_transactions


def get_data_json(file_path):
    # Specify the path to your JSON file
    # file_path = 'data/transactions_14082023.json'

    # Open the JSON file in read mode
    with open(file_path, 'r', encoding='utf-16') as json_file:
        # Parse the JSON content into a Python data structure (dictionary or list)
        try:
            data = json.load(json_file)

        except Exception as e:
            print(f"JSON file processing error: {e}")

    filtered_data = {
        "accounts": filter_accounts(data['accounts']),
        "categories": filter_categories(data['categories']),
        "transactions": filter_transactions(data['transactions'])
    }

    return filtered_data
