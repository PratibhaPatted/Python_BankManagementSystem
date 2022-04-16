"""summary
    Returns:
        user_type: description
    """
class User(): # multiple inheritance
    """summary
    """
    ACCNUMBER = 0
    USER_NAME = ""
    INPUTAMT = 0
    ACCTYPE = ""
    @classmethod

    def createuser(self,amountno, username, inputamount, user_type):
        self.ACCNUMBER =amountno
        self.USER_NAME = username
        self.INPUTAMT = inputamount
        self.ACCTYPE = user_type
    @classmethod
    def display(self):
        """summary
        """
        print("***********************************")
        print("ACCOUNT DETAILS \n")
        print("Account Number : ", self.ACCNUMBER)
        print("Account User Name : ", self.USER_NAME)
        print("Balance : ", self.INPUTAMT)
        print("Type of Account", self.ACCTYPE)
        print("\nAccount Created!\n")

ACCNUMBER = int(input("Enter account number: \n"))
USER_NAME = input("Enter the user name: \n")
INPUTAMT = int(input("Enter deposit amount: \n"))
try:
    if INPUTAMT <= 0:
        print("invalid input amount")
except ValueError as excepz_err:
    print("Error is", excepz_err)
finally:
    print("Input amount", INPUTAMT)
ACCTYPE = input("Enter account user_type: SA for Savings Account, CA for Current Account \n")

STRINGP_1 = "SA"
STRINGP_2 = "CA"
try:
    if STRINGP_1 != "SA":
        print("invalid input")
    elif STRINGP_2 != "CA":
        print(" invalid user_type")
        print ("vaild SA/CA")
finally:
    print("Wrong account user_type")

obj = User()
obj.createuser(ACCNUMBER,USER_NAME,INPUTAMT,ACCTYPE)
obj.display()

class Depositwithdraw(User):  # derived constructors from parent class
    """summary
    """
    def deposit_amt(self, totalamount, amount):
        self.totalamount = totalamount
        self.amount = amount

    def depositamount(self):
        """summary
        """
        print("******************************************\n")
        amount = int(input("Enter amount to be deposited"))
        try:
            if amount <= 0:
                print("invalid")
        except ValueError as excepz_err:
            print("Error is", excepz_err)
        finally:
            print("amount", amount)
        self.totalamount = self.INPUTAMT + amount
        print("Successfully Deposited", self.totalamount)

    def withdrawamount(self):
        """summary
        """
        print("******************************************\n")
        amount = int(input("Enter amount to be withdraw"))
        try:
            if amount <= 0:
                print("invalid")
        except ValueError as excepz_err:
            print("Error is", excepz_err)
        finally:
            print("amount", amount)
        self.totalamount = self.INPUTAMT - amount
        print("Successfully withdraw", self.totalamount)

    def report(self):
        """summary
        """
        print("******************************************\n")
        print(self.ACCNUMBER, " ", self.USER_NAME, " ", self.INPUTAMT, " ", self.ACCTYPE)
        print("Total amount is:")
        print(self.totalamount)


# class to display main options

obj1 = Depositwithdraw()
obj2 = Depositwithdraw()
obj1.depositamount()
obj2.withdrawamount()
obj2.report()

class Maindisplay(Depositwithdraw):
    """summary
    Args:
        Depositwithdraw (user_type): description
    """
    def introduction(self):
        """summary
        """
        print("\t\t\t\t****")
        print("\t\t\t\tBANK MANAGEMENT SYSTEM")
        print("\t\t\t\t****")
        input()


CH = ''
NUM = 0

while CH != 5:
    print("\tMAIN MENU")
    print("\t1. Create account")
    print("\t2. Deposit amount")
    print("\t3. Withdraw amount")
    print("\t4. Report ")
    print("\t5. Exit")
    print("\tSelect Your Option (1-5) ")
    CH = input()

    if CH == '1':
        obj.createuser( amountno=0, username = " ", inputamount=0, user_type= "")
    elif CH == '2':
        NUM = int(input("\tEnter to deposit account amount. : "))
        obj1.depositamount()
    elif CH == '3':
        NUM = int(input("\tEnter to withdraw amount. : "))
        obj2.withdrawamount()
    elif CH == '4':
        NUM = int(input("\tEnter to see report : "))
        obj2.report()
    elif CH == '5':
        print("\tThanks for using bank managemnt system")
        break
    else:
        print("Invalid choice\n")

    CH = input("Enter your choice : \n")

obj3 = Maindisplay()
obj3.introduction()
