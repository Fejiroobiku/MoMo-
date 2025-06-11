#!/usr/bin/python3
import xml.etree.ElementTree as ET
from db_functions import convert_to_date
from models import Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.exc import IntegrityError
import os
import json

# models/tables
from models.airtime_payments import AirTime
from models.incoming_money import IncomingMoney
from models.bank_deposits import BankDeposits
from models.cash_power_bills import CashPowerPayments
from models.transactions_by_third_parties import PaymentToThirdParty
from models.transfers_to_momo import TransferToMomo
from models.internet_and_voice_bundle import Bundles
from models.payment_to_code_holders import PaymentToCode
from models.withdrawals import Withdrawals

# from models.bank_transfers import

# accessing the xml file
mytree = ET.parse("modified_sms_v2.xml")
root = mytree.getroot()


# folder_name = "./MOMO_DASHBOARD"
# folder_path = os.path.abspath(folder_name)
# print("Data base name:", folder_path)

# creating an the database / opening the database
engine = create_engine(f"sqlite:///momo_database.db", echo=False)
Base.metadata.create_all(bind=engine)


# creating a seession.
SessionFactory = sessionmaker(bind=engine)
Session = scoped_session(SessionFactory)


# populating the money recieved table, >> 65 tot records √
try:
    with Session() as session:
        # Creates session that will be use to interact with the database
        for element in root:
            if element.get("body").startswith("You have received"):
                body_parts = element.get("body").split(".")
                amount = body_parts[0].split(" ")[3]
                firstname, second_name = body_parts[0].split()[6:8]
                id = int(element.get("date"))
                date = convert_to_date(element.get("readable_date"))
                table_row = IncomingMoney(id, firstname, second_name, amount, date)
                session.add(table_row)
        session.commit()
except IntegrityError:
    # This handles integrity error there is no duplicate of data.
    print("(1) Table with the same data already exists!")


# populating the airtime table, >> 15 tot records √
try:
    with Session() as session:
        for element in root:
            if "Airtime" in str(element.get("body")):
                id = int(element.get("date"))
                amount = int(element.get("body").split(" ")[3])
                date = convert_to_date(element.get("readable_date"))

                # add the data to the db
                table_row = AirTime(id=id, amount=amount, date=date)
                session.add(table_row)
        session.commit()
except IntegrityError:
    print("(2) Table with the same data already exists!")


# populating the bank_deposits # 248 recs √
try:
    with Session() as session:
        for element in root:
            if str(element.get("body")).startswith("*113*R*A"):
                id = int(element.get("date"))
                amount = int(element.get("body").split(" ")[4])
                date = convert_to_date(element.get("readable_date"))

                # populatng the database
                table_row = BankDeposits(id, amount, date)
                session.add(table_row)
        session.commit()
except IntegrityError:
    print("(3) Table with the same data already exists!")


# populating the cashpower bills # 11 rec √
try:
    with Session() as session:
        for element in root:
            if "MTN Cash Power" in str(element.get("body")):
                id = int(element.get("date"))
                amount = int(element.get("body").split(" ")[3])
                date = convert_to_date(element.get("readable_date"))

                # populate the database
                table_row = CashPowerPayments(
                    id=id, amount=amount, date=date, service_provider="REG"
                )
                session.add(table_row)
        session.commit()
except IntegrityError:
    print("(4) Table with the same data already exists!")


# populating Data, packs and bundles # 37 rec √
try:
    with Session() as session:
        for element in root:
            if "by Data Bundle" in str(element.get("body")):  # 16rec
                id = int(element.get("date"))
                amount = int(element.get("body").split(" ")[3])
                date = convert_to_date(element.get("readable_date"))

                table_row = Bundles(id=id, amount=amount, date=date)
                session.add(table_row)

            elif "Bundles" in str(element.get("body")):  # 21 rec
                id = int(element.get("date"))
                amount = int(element.get("body").split(" ")[3])
                date = convert_to_date(element.get("readable_date"))

                table_row = Bundles(id=id, amount=amount, date=date)
                session.add(table_row)
        session.commit()
except IntegrityError:
    print("(5) Table with the same data already exists!")


# populating to transfers Momo # 585 + 2 + 6 payment to momo numbers recs
transfers_tot = 0

try:
    with Session() as session:
        for element in root:
            if element.get("body").startswith("*165*S*"):
                id = int(element.get("date"))
                date = convert_to_date(element.get("readable_date"))
                amount = int(element.get("body").split(" ")[0].split("*")[-1])
                first_name = element.get("body").split(" ")[4]
                last_name = element.get("body").split(" ")[5]
                tel = element.get("body").split(" ")[6]
                fee = element.get("body").split(" ")[-16]
                table_row = TransferToMomo(
                    id, first_name, last_name, tel, fee, amount, date
                )
                session.add(table_row)
            elif element.get("body").startswith("Your payment"):  # 2 recs
                id = int(element.get("date"))
                date = convert_to_date(element.get("readable_date"))
                amount = int(element.get("body").split(" ")[3])
                first_name = element.get("body").split(" ")[5]
                last_name = element.get("body").split(" ")[6]
                tel = element.get("body").split(" ")[7]
                fee = 0
                table_row = TransferToMomo(
                    id, first_name, last_name, tel, fee, amount, date
                )
                session.add(table_row)
            elif element.get("body").startswith("You have transferred"):
                id = int(element.get("date"))
                date = convert_to_date(element.get("readable_date"))
                amount = int(element.get("body").split(" ")[3])
                first_name = element.get("body").split(" ")[6]
                last_name = element.get("body").split(" ")[7]
                tel = element.get("body").split(" ")[8]
                fee = None
                table_row = TransferToMomo(
                    id, first_name, last_name, tel, fee, amount, date
                )
                session.add(table_row)
        session.commit()
except IntegrityError:
    print("(6) Table with the same data already exists!")


# populating the DB with transfert to code holders # 658 recs
try:
    with Session() as session:

        for element in root:
            if element.get("body").startswith("TxId:"):
                id = int(element.get("date"))
                date = convert_to_date(element.get("readable_date"))
                amount = element.get("body").split(" ")[5]
                amount = int("".join(amount.split(",")))
                first_name = element.get("body").split(" ")[8]
                last_name = element.get("body").split(" ")[9]
                code = element.get("body").split(" ")[10]

                table_row = PaymentToCode(id, first_name, last_name, code, amount, date)
                session.add(table_row)
                session.commit()
except IntegrityError:
    print("(7) Table with the same data already exists!")

# withdrawals
withdrawals_tot = 0
try:
    with Session() as session:
        for element in root:
            if "withdrawn" in element.get("body"):
                id = int(element.get("date"))
                date = convert_to_date(element.get("readable_date"))
                amount = element.get("body").split(" ")[12]
                agent = element.get("body").split(" ")[9]
                agents_tel = element.get("body").split(" ")[10].split(",")[0]
                fee = element.get("body").split(" ")[-10]
                table_row = Withdrawals(id, agent, agents_tel, amount, fee, date)
                session.add(table_row)
        session.commit()
except IntegrityError:
    print("(8) Table with the same data already exists!")

# transactions initiated by third parties. # 20 recs
try:
    with Session() as session:
        for element in root:
            if element.get("body").startswith(
                "*164*S*Y'ello"
            ) and not "Data Bundle MTN" in element.get("body"):
                id = int(element.get("date"))
                amount = int(element.get("body").split(" ")[3])
                service_provider = " ".join(
                    element.get("body").split(".")[0].split(" ")[6:-10]
                )
                date = convert_to_date(element.get("readable_date"))
                table_row = PaymentToThirdParty(
                    id=id, amount=amount, service_provider=service_provider, date=date
                )
                session.add(table_row)
        session.commit()
except IntegrityError:
    print("(9) Table with the same data already exists!")


# log invalid data
with open("failed_transactions_data.json", "w") as file:
    data = []
    for element in root:
        if (
            element.get("body")
            and element.get("body").startswith("*143*")
            or element.get("body").startswith("A reversal")
        ):
            msg = element.get("body")
            data.append(msg)
    json.dump(data, file, indent=2)

with open("invalid_data.json", "w") as file:
    data = []
    for element in root:
        if (
            element.get("body").startswith("Yello")
            or "Dear Customer, your MTN" in str(element.get("body"))
            or element.get("body").startswith("1)")
        ):
            msg = element.get("body")
            data.append(msg)
    json.dump(data, file, indent=2)
