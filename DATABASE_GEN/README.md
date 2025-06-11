# MOMO Transactions Parser

## Description
This project extracts financial transaction data from an XML file containing mobile money (MoMo) transaction messages. The extracted data is parsed, categorized, and stored in an SQLite database.

## Features
- Parses an XML file (`modified_sms_v2.xml`) containing MoMo transaction records.
- Categorizes transactions into various tables, including:
  - Incoming money
  - Airtime purchases
  - Bank deposits
  - Cash power bill payments
  - Transfers to MoMo numbers
  - Internet and voice bundles
  - Payments to code holders
  - Withdrawals
  - Transactions initiated by third parties
- Uses SQLAlchemy as an ORM for database management.
- Logs invalid and failed transactions separately in JSON files.

## Installation
### Prerequisites
Ensure you have the following installed on your system:
- Python 3
- SQLite3
- Required Python packages: `sqlalchemy`, `xml.etree.ElementTree`

### Setup
1. Clone the repository:
   ```sh
   git clone <repository_url>
   cd momo_transactions_parser
   ```
2. Ensure `modified_sms_v2.xml` is present in the project directory.

## Usage
1. Run the script:
   ```sh
   python main.py
   ```
2. The script will parse the XML data and populate the `momo_database.db` file with categorized transactions. (Which will be used by Django)
3. Check the generated JSON logs (`failed_transactions_data.json` and `invalid_data.json`) for any failed or unrecognized transactions.

## Project Structure
```
.
├── models/                     # Contains SQLAlchemy models for different transaction types
│   ├── __init__.py
│   ├── airtime_payments.py
│   ├── bank_deposits.py
│   ├── cash_power_bills.py
│   ├── incoming_money.py
│   ├── internet_and_voice_bundle.py
│   ├── payment_to_code_holders.py
│   ├── transactions_by_third_parties.py
│   ├── transfers_to_momo.py
│   ├── withdrawals.py
|   |__ payments_base.py
│
├── main.py                      # Main script to process XML and populate the database
├── db_functions.py               # Helper functions for data conversion
├── modified_sms_v2.xml           # XML file containing transaction messages
├── momo_database.db              # SQLite database (generated)
├── failed_transactions_data.json # Logs of failed transactions
├── invalid_data.json             # Logs of invalid transactions
└── README.md                     # Project documentation
```

## Notes
- Duplicate data handling: The script prevents inserting duplicate records using SQLAlchemy’s `IntegrityError` handling.
- The `convert_to_date` function helps convert dates into a standardized format.

## License
No licencse

## Author
Aimable Nkurikiyimana

