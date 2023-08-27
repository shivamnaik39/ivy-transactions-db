CREATE TABLE IF NOT EXISTS accounts (account_id TEXT PRIMARY KEY, name TEXT);
CREATE TABLE IF NOT EXISTS categories (
    category_id TEXT PRIMARY KEY,
    name TEXT
);
CREATE TABLE IF NOT EXISTS transactions (
    transaction_id TEXT PRIMARY KEY,
    account_id TEXT,
    category_id TEXT,
    amount REAL,
    date_time DATETIME,
    title TEXT,
    description TEXT,
    to_account_id TEXT,
    to_amount REAL,
    transaction_type TEXT,
    FOREIGN KEY (account_id) REFERENCES accounts (account_id),
    FOREIGN KEY (to_account_id) REFERENCES accounts (account_id),
    FOREIGN KEY (category_id) REFERENCES categories (category_id)
);
DELETE FROM accounts;
DELETE FROM categories;
DELETE FROM transactions;