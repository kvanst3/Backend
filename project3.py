class Bank:

    password_value = None
    checking_balance = None
    saving_balance = None

    def __init__(self, account_holder):
        self.account_holder = account_holder

    def login(self):
        holder_password = input(f"Hello {self.account_holder}, please input your password:")
        if self.password(holder_password):
            print(f'Password accepted. Loging in.')
            return True

    def password(self, attempted_password):
        self.read_account_file('password')
        if self.password_value == attempted_password:
            return True

    def read_account_file(self, req):
        with open(f'/home/k/Desktop/Python_projects/{self.account_holder}.txt', 'r') as account:
            content = account.readlines()
            for line in content:
                if line.split(":")[0].rstrip() == req == 'password':
                    self.password_value = line.split(":")[-1].rstrip()
                    break
                elif line.split(":")[0].rstrip() == req == 'checking_balance':
                    self.checking_balance = float(line.split(":")[-1].rstrip())
                    break
                elif line.split(":")[0].rstrip() == req == 'saving_balance':
                    self.saving_balance = float(line.split(":")[-1].rstrip())
                    break

    def write_account_file(self, req):
        with open(f'/home/k/Desktop/Python_projects/{self.account_holder}.txt', 'r') as account:
            content = account.readlines()
            for line in content:
                if line.split(":")[0].rstrip() == req == 'password':
                    content[0] = (f"password:{self.password_value}\n")
                    break
                elif line.split(":")[0].rstrip() == req == 'checking_balance':
                    content[1] = (f"checking_balance:{self.checking_balance}\n")
                    break
                elif line.split(":")[0].rstrip() == req == 'saving_balance':
                    content[2] = (f"saving_balance:{self.saving_balance}\n")
                    break
        with open(f'/home/k/Desktop/Python_projects/{self.account_holder}.txt', 'w') as account:
            account.writelines(content)

    def check(self):
        pass

    def withdraw(self, amount):
        pass

    def deposit(self, amout):
        pass

    def logout(self):
        pass

    def mainmenue(self, account_type):
        while True:
            cus_action = input("Welcome! What would you like to do today?\n0.\tCheck balance\n1.\tWithdraw\n2.\tDeposit\n3.\tBack\n")
            if cus_action == '0':
                account_type.check()
            elif cus_action == '1':
                withdraw_amount = input("How much?\n")
                account_type.withdraw(int(withdraw_amount))
            elif cus_action == '2':
                deposit_amount = input("How much?\n")
                account_type.deposit(int(deposit_amount))
            elif cus_action == '3':
                break
            else:
                print("unexpected input. Please try again.\n")
                continue


class Checking(Bank):

    def __init__(self, account_holder):
        super().__init__(account_holder)

    def check(self):
        self.read_account_file("checking_balance")
        print("current balance on your checking's account:\t$", self.checking_balance)

    def withdraw(self, amount):
        self.check()
        if int(amount) <= self.checking_balance:
            self.checking_balance -= int(amount)
            self.write_account_file('checking_balance')
            print("Your new balance is:\t$", self.checking_balance)
        else:
            print("Not enough funds.")

    def deposit(self, amount):
        self.check()
        self.checking_balance += int(amount)
        self.write_account_file('checking_balance')
        print("Your new balance is:\t$", self.checking_balance)


class Saving(Bank):

    def __init__(self, account_holder):
        super().__init__(account_holder)

    def check(self):
        self.read_account_file("saving_balance")
        print("current balance on your saving's account:\t$", self.saving_balance)

    def withdraw(self, amount):
        self.check()
        if int(amount) <= self.saving_balance:
            self.saving_balance -= int(amount)
            self.write_account_file('saving_balance')
            print("Your new balance is:\t$", self.saving_balance)
        else:
            print("Not enough funds.")

    def deposit(self, amount):
        self.check()
        self.saving_balance += int(amount)
        self.write_account_file('saving_balance')
        print("Your new balance is:\t$", self.saving_balance)


while True:
    cus_login = input("Welcome! Please enter your login:\n")
    try:
        f = open(f"{cus_login}.txt")
    except Exception as e:
        print("Error. Login not recognised.")
        print(type(e))
        continue
    bank = Bank(cus_login)
    while True:
        if bank.login():
            while True:
                cus_action = input("Choose an account:\n0.\tChecking\n1.\tSaving\n2.\tExit\n")
                if cus_action == '0':
                    checking = Checking(cus_login)
                    bank.mainmenue(checking)
                elif cus_action == '1':
                    saving = Saving(cus_login)
                    bank.mainmenue(saving)
                else:
                    print("Thank you for using FreedomFucker2.0")
                    break
            break
        else:
            print("Incorrect Password")
            continue
    break
