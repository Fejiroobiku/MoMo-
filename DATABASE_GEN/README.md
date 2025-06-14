MoMo Transaction Data Extractor

Overview
This application is designed to extract, interpret, and organize transaction details from an XML file containing mobile money (MoMo) message records. It processes the data, classifies transactions, and stores them in a structured SQLite database.

Key Functionalities
Processes an XML file (modified_sms_v2.xml) with MoMo-related SMS transaction entries.

Differentiates and stores various transaction types in separate database tables, such as:

Funds received

Airtime recharges

Bank transfers

Cash Power bill settlements

MoMo-to-MoMo transfers

Bundle purchases (internet and voice)

Payments made to coded merchant accounts

Money withdrawals

Transactions triggered by external users

Employs SQLAlchemy ORM for seamless interaction with the database.

Logs any failed or invalid transaction data into JSON files for easy debugging.

Setup Instructions
Requirements
To run this project, ensure your environment has the following:

Python 3 installed

SQLite3 database engine

Python libraries: sqlalchemy, and the built-in xml.etree.ElementTree

Installation Steps
Clone the project repository:

bash
Copy
Edit
git clone <repository_url>  
cd momo_transactions_parser  
Place the modified_sms_v2.xml file in the root of the project directory.

How to Use
Execute the main script:

bash
Copy
Edit
python main.py  
The parser will extract and save transactions to an SQLite file named momo_database.db, which will later be used within a Django environment.

Refer to failed_transactions_data.json and invalid_data.json to review any transactions the script couldn't process correctly.

File & Folder Structure
graphql
Copy
Edit
.
├── models/                          # All SQLAlchemy models categorized by transaction type
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
│   └── payments_base.py  
│
├── main.py                          # Core script that drives the parsing process  
├── db_functions.py                  # Utility methods for data formatting and processing  
├── modified_sms_v2.xml              # Source XML file with raw MoMo messages  
├── momo_database.db                 # Generated SQLite DB file holding the parsed data  
├── failed_transactions_data.json    # Output log of failed transactions  
├── invalid_data.json                # Output log for unrecognized message formats  
└── README.md                        # Documentation  
Additional Information
The script includes logic to prevent redundant entries by catching IntegrityError exceptions from SQLAlchemy.

Date formatting is standardized using the convert_to_date utility function.

License
This project does not currently use any specific license.













