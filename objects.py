class BankAccount:
    def __init__(self, account_holder, initial_balance=0):
        self.account_holder = account_holder
        self.__balance = initial_balance  # Private attribute

    def deposit(self, amount):
        if amount < 0:
            print(f"({self.account_holder}) Deposit amount must be positive.")
            return

        self.__balance += amount
        print(f"({self.account_holder}) Deposit accepted. New balance: {self.__balance}")

    def withdraw(self, amount):
        if amount < 0:
            print(f"({self.account_holder}) Withdraw amount must be positive.")
            return

        if amount > self.__balance:
            print(f"({self.account_holder}) Insufficient funds.")
            return

        self.__balance -= amount
        print(f"({self.account_holder}) Withdraw accepted. New balance: {self.__balance}")

    def transfer(self, other_account, amount):
        if amount < 0:
            print(f"({self.account_holder}) Transfer amount must be positive.")
            return
        other_account.withdraw(amount)
        self.__balance += amount
        print(
            f"({other_account.account_holder} > {self.account_holder}) Transfer accepted. New balance: {self.__balance}")



class ATM:
    def menu(self):
        print("Vítejte v bance!")
        print("1 - seznam účtů")
        print("2 - přidat účet")
        print("3 - převod financí")
        print("4 - výběr financí")
        print("5 - vklad financí")

        choice = int(input("Zvolte akci:"))
        if choice == 1:
            self.print_accounts_atm()
        elif choice == 2:
            self.add_account()
        elif choice == 3:
            self.transfer()
        elif choice == 4:
            self.withdraw()
        elif choice == 5:
            self.deposit()
        else:
            print("Chybná akce, vyber znovu")



    def print_accounts_atm(self):
        i = 0
        for bank_account in bank_accounts:
            print(f"{i} - {bank_account.account_holder}")
            i += 1

        self.menu()


    def add_account(self):
        name = input("Název účtu: ")
        bank_accounts.append(BankAccount(name))

        self.menu()

    def transfer(self):
        print("Dostupnýé účty:")
        self.print_accounts()

        index_from = input("Účet ze kterého:")
        index_to = input("Účet do kterého:")
        amount = input("Částka:")

        bank_accounts[int(index_to)].transfer(bank_accounts[int(index_from)], int(amount))

        self.menu()

    def withdraw(self):
        print("Dostupné účty:")
        self.print_accounts()

        index_from = input("\nz jakého účtu:")
        amount = input("částka:")

        bank_accounts[int(index_from)].withdraw(int(amount))

        self.menu()

    def deposit(self):
        print("Dostupné účty:")
        self.print_accounts()

        index_to = input("\nDo jakého účtu:")
        amount = input("částka:")

        bank_accounts[int(index_to)].deposit(int(amount))

        self.menu()

    def print_accounts(self):
        i = 0
        for bank_account in bank_accounts:
            print(f"{i} - {bank_account.account_holder}")
            i += 1


#
#
#
#
#
bank_accounts = [BankAccount('Jon', 1000)]

def main():
    bank = ATM()

    choice = int(input("Zvolte 1 pro použití bankomatu:"))
    if choice == 1:
        bank.menu()
        return

main()






#def menu():
#    print("Vítejte v bance!")
#    print("1 - seznam účtů")
#    print("2 - přidat účet")
#    print("3 - převod financí")
#    print("4 - výběr financí")
#    print("5 - vklad financí")
#
#    choice = int(input("Zvolte akci:"))
#    if choice == 1:
#        print_accounts()
#    elif choice == 2:
#        add_account()
#    elif choice == 3:
#        transfer()
#    elif choice == 4:
#        withdraw()
#    elif choice == 5:
#        deposit()
#    else:
#        print("Chybná akce, vyber znovu")
#
#    menu()
#
#def print_accounts():
#    i = 0
#    for bank_account in bank_accounts:
#        print(f"{i} - {bank_account.account_holder}")
#        i += 1
#
#def add_account():
#    name = input("Název účtu: ")
#    bank_accounts.append(BankAccount(name))
#
#def transfer():
#    print("Dostupnýé účty:")
#    print_accounts()
#
#    index_from = input("Účet ze kterého:")
#    index_to = input("Účet do kterého:")
#    amount = input("Částka:")
#
#    bank_accounts[int(index_to)].transfer(bank_accounts[int(index_from)], int(amount))
#
#def withdraw():
#    print("Dostupné účty:")
#    print_accounts()
#
#    index_from = input("\nz jakého účtu:")
#    amount = input("částka:")
#
#    bank_accounts[int(index_from)].withdraw(int(amount))
#
#def deposit():
#    print("Dostupné účty:")
#    print_accounts()
#
#    index_to = input("\nDo jakého účtu:")
#    amount = input("částka:")
#
#    bank_accounts[int(index_to)].deposit(int(amount))
#
#menu()

# TODO: dokončit bankomat jako objekt