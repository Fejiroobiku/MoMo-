# import xml.etree.ElementTree as ET
# from datetime import datetime
# from db_functions import convert_to_date

# mytree = ET.parse("modified_sms_v2.xml")
# root = mytree.getroot()
# sms_total = len(root)
# print("sms_total:", sms_total)

# sample = root[0]

# date = int(sample.get("date"))
# date = date / 1000
# date_readable = datetime.fromtimestamp(date)
# # print(date_readable)


# # Parsng incoming money √ √

# income_msg_tot = 0
# for element in root:
#     if element.get("body").startswith("You have received"):
#         income_msg_tot += 1
#         # table data
#         msg_parts = element.get("body").split(".")
#         amount = msg_parts[0].split(" ")[3]
#         sender_firstname, senders_second_name = msg_parts[0].split()[6:8]
#         id = element.get("date")
#         date = msg_parts[0].split(" ")[-2]
#         date = datetime.strptime(date, "%Y-%m-%d")
#         # print(
#         #     f"id: {id} | Sender: {sender_firstname} {senders_second_name} | amount: {amount} | date: {date}"
#         # )
#         # print("------------------+----------------------------------------------")

# print("income_msg_tot:", income_msg_tot)


# # parse payments code owner. √√
# payment_msg_tot = 0
# for element in root:
#     if element.get("body").startswith("TxId:"):
#         msg = element.get("body")
#         # print(msg)
#         payment_msg_tot += 1
# print("payment_msg_tot:", payment_msg_tot)


# # payments to (with not id) ^ (TRANSFER TO MOMO CATEGORY) √ √
# # warning: be careful when adding this to the db
# payment_with_no_id = 0
# for element in root:
#     if element.get("body").startswith("Your payment"):
#         msg = element.get("body")
#         # print(msg)
#         payment_with_no_id += 1
# print("payment with no id:", payment_with_no_id)


# # parse (transfers to Momo) from 36521838, √ √
# transfers_tot = 0
# for element in root:
#     if element.get("body").startswith("*165*S*"):
#         msg = element.get("body")
#         # print(msg)
#         transfers_tot += 1
# print("transfers_to:", transfers_tot)

# # transfer to (Transfer to Momo category) √ √
# # warning be careful when parsing. . this meassages have no fee.
# transfers_owner_tot = 0
# for element in root:
#     if element.get("body").startswith("You have transferred"):
#         transfers_owner_tot += 1
#         msg = element.get("body")
#         print(msg)
# print("You have transferred:", transfers_owner_tot)

# # parse bank deposits √ √
# bank_deposits_transaction_tot = 0
# for element in root:
#     if element.get("body").startswith("*113*R*A"):
#         msg = element.get("body")
#         # print(msg)
#         bank_deposits_transaction_tot += 1
# print("bank_deposits:", bank_deposits_transaction_tot)


# # parse payments to services and other transactions (ex direct payment) √ (still some work to do)
# payment_to_services_tot = 0
# for element in root:
#     if element.get("body").startswith("*162*T") or element.get("body").startswith(
#         "*164*S"
#     ):
#         msg = element.get("body")
#         id = int(element.get("date"))
#         # amount = int(element.get("body").split(' ')[3])
#         date = convert_to_date(element.get("readable_date"))
#         payment_to_services_tot += 1
#         print(msg)
#         # print(id, amount, date)

# print("services payments:", payment_to_services_tot)


# # parse withdrawals √ √
# withdrawals_tot = 0
# for element in root:
#     if "withdrawn " in element.get("body"):
#         msg = element.get("body")
#         # print(msg)
#         withdrawals_tot += 1
# print("withdrawn:", withdrawals_tot)



# # bad data >> log them in a separate file.. not in the db

# # bad data # to be loged them afile that contans ignored infor √ √
# bad_data = 0
# for element in root:
#     if element.get("body").startswith("1)"):
#         msg = element.get("body")
#         # print(msg)
#         bad_data += 1
# # print("bad_data", bad_data)


# # parse yello's //to be loged them afile that contans ignored infor √ √
# yello_s = 0
# for element in root:
#     if element.get("body").startswith("Yello"):
#         msg = element.get("body")
#         # print(msg)
#         yello_s += 1
# # print("yello's: ", yello_s)


# # transactions with no amount ?? to be loged them afile that contans ignored infor √ √
# no_amount_data = 0
# for element in root:
#     if "Dear Customer, your MTN" in element.get("body"):
#         msg = element.get("body")
#         # print(msg)
#         no_amount_data += 1
# print("vauge data:", no_amount_data)


# # these two are in failed transactions.

# # failed transactions. to be loged them afile that contans ignored infor √ √
# failed_tot = 0
# for element in root:
#     if element.get("body").startswith("*143*"):
#         failed_tot += 1
#         msg = element.get("body")
#         # print(msg)
# print("failed:", failed_tot)


# # reversal -- to be loged them afile that contans ignored infor √ √
# reversals = 0
# for element in root:
#     if element.get("body").startswith("A reversal"):
#         reversals += 1
#         msg = element.get("body")
#         # print(msg)
# print("reversals:", reversals)

# # track messages total
# print(
#     bank_deposits_transaction_tot
#     + payment_msg_tot
#     + income_msg_tot
#     + transfers_tot
#     + payment_to_services_tot
#     + no_amount_data
#     + withdrawals_tot
#     + yello_s
#     + transfers_owner_tot
#     + bad_data
#     + failed_tot
#     + payment_with_no_id
#     + reversals
#     - sms_total
# )
