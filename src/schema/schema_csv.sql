CREATE TABLE IF NOT EXISTS transactions (
  transaction_id TEXT PRIMARY KEY,
  account TEXT,
  category TEXT,
  amount REAL,
  date_time DATETIME,
  title TEXT,
  description TEXT,
  to_account TEXT,
  to_amount REAL,
  transaction_type TEXT,
  FOREIGN KEY (account_id) REFERENCES accounts (account_id),
  FOREIGN KEY (to_account_id) REFERENCES accounts (account_id),
  FOREIGN KEY (category_id) REFERENCES categories (category_id)
);
DELETE FROM transactions;