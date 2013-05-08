# Filename: fo_serial.py
# Author: Lim Ah Seng
# Description: Program to CRUD serial file

import datetime

def menu():
    print("[1] Search")
    print("[2] Transact")
    print("[0] Quit")

def search():
    try:
        # open transaction file in read mode
        transaction_file = open("TRANSACTIONS.DAT", 'r')

        # assume valid account number
        account_no = input("Enter account number: ")
        account_no = account_no.upper()

        # get first transaction record
        record = transaction_file.readline()
        # while not end of transaction file
        while record != '':
            # get account number
            current_account_no = record[18:23]
            # if account number matches
            if current_account_no == account_no:
                # get transaction details
                transaction_date = record[0:10]
                transaction_time = record[10:18]
                transaction_type = record[23:24]
                if transaction_type == 'D':
                    transaction_type = "Deposit"
                else: # withdrawal
                    transaction_type = "Withdrawal"
                transaction_amount = record[24:28]
                # display transaction details
                print("Account number:", current_account_no)
                print("Transaction date:", transaction_date)
                print("Transaction time:", transaction_time)
                print("Transaction type:", transaction_type)
                print("Transaction amount: $", transaction_amount)
                print()
            # get next transaction record
            record = transaction_file.readline()

        # close transaction file
        transaction_file.close()

    except IOError:
        # input file read error
        print("Cannot read from transaction file TRANSACTIONS.DAT")

def transact():
    try:
        # open transaction file in append mode
        transaction_file = open("TRANSACTIONS.DAT", 'a')

        # assume valid account number
        account_no = input("Enter account number: ")
        account_no = account_no.upper()

        # assume valid transaction type
        transaction_type = input("Enter transaction type ([D]eposit/[W]ithdrawal): ")
        transaction_type = transaction_type.upper()

        # assume valid transaction amount
        transaction_amount = input("Enter transaction amount: ")

        # get current system date and time
        current_datetime = datetime.datetime.now()
        current_datetime = current_datetime.strftime("%Y-%m-%d%H:%M:%S")

        # add to existing transaction records
        transaction_file.write("{0}{1}{2}{3:>4s}\n".format(current_datetime, account_no, transaction_type, transaction_amount))

        # close transaction file
        transaction_file.close()

        # output status
        print("Transaction successful.")
        print()

    except IOError:
        # output file append error
        print("Cannot write to transaction file TRANSACTIONS.DAT")

# main
option = "1"

while option != '0':
    menu()
    option = input("Enter option: ")
    if option == '1':
        search()
    elif option == '2':
        transact()


