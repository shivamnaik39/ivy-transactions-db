
# ivy-transactions-db

Unofficial companion tool to add the transactions data generated and exported by ivy wallet from json/csv to a sqlite database for deep analytics purposes.

With all the data in a SQL database, it opens up a wide range of possibilities for gaining deeper insights into our personal expenses

Although this tool is designed to work with csv/json file generated by ivy wallet, but it will work with any file provided it is in the correct format


## Example of custom csv file
| ID                                   | Date              | Title               | Category           | Account             | Amount   | Type      | Transfer Amount | To Account       | Description               |
|--------------------------------------|-------------------|---------------------|--------------------|---------------------|----------|-----------|-----------------|-------------------|---------------------------|
| 1 | 13/08/2023 23:55 | Salary              | Income             | XYZ Bank            | 5000.00  | INCOME    |                 |                   | Monthly salary           |
| 2 | 13/08/2023 21:48 | Grocery Shopping    | Groceries          | Local Mart          | 150.00   | EXPENSE   |                 |                   | Weekly grocery expenses  |
| 3 | 13/08/2023 23:51 | Rent Payment        | Housing            | ABC Realty          | 1200.00  | TRANSFER  | 1200.00         | XYZ Bank          | Monthly rent payment     |



[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)


## Requirements

  - Python 3.11
  - Copy the csv file to `data/` directory



## Run Locally

Clone the project

```bash
  git clone https://github.com/shivamnaik39/ivy-transactions-db
```

Go to the project directory

```bash
  cd ivy-transactions-db
```

Run the file

```bash
  python -u main.py
```

- After successful execution the output will be saved at `data/transactions.db`

