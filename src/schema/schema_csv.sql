DROP TABLE IF EXISTS transactions;
CREATE TABLE  transactions (
  transaction_id TEXT PRIMARY KEY,
  account TEXT,
  category TEXT,
  amount REAL,
  date_time DATETIME,
  title TEXT,
  description TEXT,
  to_account TEXT,
  to_amount REAL,
  transaction_type TEXT
)