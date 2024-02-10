import os.path as o
import pickle as p
import random as r

def get_all_accounts():
    if o.isfile("Account.bat"):
        read_file = open("Account.bat","rb")
        Accounts =  p.load(read_file)
        read_file.close()
        
        return Accounts
    
    else:
        return {}
    
def write_accounts(Accounts):
    write_file = open("Account.bat","wb")
    p.dump(Accounts,write_file)
    write_file.close()

def display_account(Act):
    Accounts = get_all_accounts()
    print("-"*80)
    print("Holder Name: ",Act[0])
    print("Phone Number: ",Act[1])
    print("Address: ",Act[2])
    print("Gender: ",Act[3])
    print("Password: ",Act[4])
    print("Balance: ",Act[5])
    print("-"*80)


def add_account():
    Accounts = get_all_accounts()
    ac_no = input("Enter Account Number: ")
    if ac_no in Accounts.keys():
        print("This Account number already exist.")
        return

    name = input("Enter Account Holder Name: ")
    phone = input("Enter Phone Number: ")
    address = input("Enter Address: ")
    gender = input("Enter Gender: ")
    password = r.randint(100000,1000000)
    balance= 0

    Accounts[ac_no] = [name,phone,address,gender,password,balance]

    write_accounts(Accounts)
    print("Account has been created...")

def remove_account():
    Accounts = get_all_accounts()
    ac_no = input("Enter Account Number: ")

    if ac_no in Accounts.keys():
        del Accounts[ac_no]
        print("Account has been deleted")
        write_accounts(Accounts)
    else:
        print("Account does not exist")        

def edit_account():
    Accounts = get_all_accounts()
    ac_no = input("Enter Account Number: ")

    if ac_no in Accounts.keys():
        display_account(Accounts[ac_no])
        print("What do you want to change?")
        print("0. Holder Name:")
        print("1. Phone Number:")
        print("2. Address:")
        print("3. Gender:")
        choice = int(input("\nEnter your choice: "))
        if choice>=0 and choice<4:
            v = input("Enter New Value: ")
            if v!="":
                Accounts[ac_no][choice]=v
                print("Account has been Updated")
                write_accounts(Accounts)
            else:
                print("Try Again!!!")
        else:
            print("Wrong Choice")
    else:
        print("Account does not exist")      

def display_all_account():
    Accounts = get_all_accounts()
    print("-"*80)
    print("Account Table".center(80))
    print("-"*80)
    
    for account in Accounts:
        print(account,Accounts[account])

def search_account():
    Accounts = get_all_accounts()
    ac_no = input("Enter Account Number: ")

    if ac_no in Accounts.keys():
        display_account(Accounts[ac_no])
    else:
        print("Account does not exist")


def admin_menu():
    print("-"*80)
    print("Admin Panel".center(80))
    print("-"*80)
    print("1. Add New Account")
    print("2. Remove Account")
    print("3. Edit Account")
    print("4. Display All Account")
    print("5. Search Account")
    print("0. Exit")

    choice = int(input("\nSelect option: "))
    
    if choice==1:
        add_account()
    elif choice==2:
        remove_account()
    elif choice==3:
        edit_account()
    elif choice==4:
        display_all_account()
    elif choice==5:
        search_account()
    elif choice==0:
        exit()

    input("Continue...")
    admin_menu()

def deposit_cash(ac_no):
    Accounts = get_all_accounts()
    amount = int(input("Enter Amount for Deposit: "))
    Accounts[ac_no][5]=int(Accounts[ac_no][5])+amount
    write_accounts(Accounts)
    print("Amount Deposited")    

def withdraw_cash(ac_no):
    Accounts = get_all_accounts()
    amount = int(input("Enter Amount to be withdrawn: "))
    
    if Accounts[ac_no][5]>amount:
        Accounts[ac_no][5]=int(Accounts[ac_no][5])-amount
        write_accounts(Accounts)
        print("Amount Withdrawn")

    else:
        print("Not enough amount left in account, cannot withdraw as balance is: ",Accounts[ac_no][5]) 

def check_balance(ac_no):
    Accounts = get_all_accounts()
    print("Balance: Rs.",Accounts[ac_no][5])

def account_details(ac_no):
    Accounts = get_all_accounts()
    display_account(Accounts[ac_no])

def customer_menu(ac_no):
    print("-"*80)
    print("Customer Panel".center(80))
    print("-"*80)
    print("1. Deposit Cash")
    print("2. Withdraw Cash")
    print("3. Check Balance")
    print("4. Account Details")
    print("0. Exit")

    choice = int(input("\nSelect option: "))
    
    if choice==1:
        deposit_cash(ac_no)
    elif choice==2:
        withdraw_cash(ac_no)
    elif choice==3:
        check_balance(ac_no)
    elif choice==4:
        account_details(ac_no)
    elif choice==0:
        exit()

    input("Continue...")
    customer_menu(ac_no)

def main_menu():
    print("-"*80)
    print("Banking System".center(80))
    print("-"*80)
    print("1. Admin Login\n2. Customer Login")
    choice= int(input("\nSelect option: "))
    
    if choice==1:
        admin_id = input("\nEnter Admin Id: ")
        password  = input("Enter Admin Password: ")

        if admin_id == "Ankit" and password == "1234":
            admin_menu()
        else:
            print("ID/Password not matched...")

    elif choice==2:
        Accounts = get_all_accounts()
        ac_no = input("\nEnter Account number: ")
        if ac_no in Accounts.keys():
            password = int(input("Enter Password: "))
            if Accounts[ac_no][4] == password:
                customer_menu(ac_no)
            else:
                print("Password does not matched")
        
        else:
            print("Account not available")
    

main_menu()
