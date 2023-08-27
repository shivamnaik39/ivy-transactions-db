def filter_accounts(accounts):
  accounts_data_string = "INSERT INTO accounts(account_id,name) VALUES "
  for account in accounts:
    account_id = account['id']
    name = account['name']
    tmp_data_string = f'("{account_id}","{name}"),'
    accounts_data_string += tmp_data_string
    
  return accounts_data_string[:-1]