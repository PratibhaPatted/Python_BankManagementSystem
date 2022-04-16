"""summary

    Returns:
        type: description
    """
class User(): # multiple inheritance
    """summary
    """
    ACCNUMBER = 0
    username = ""
    INPUTAMT = 0
    ACCTYPE = ""
    @classmethod

    def createuser(self,amountno, username, inputamount, type):
        self.ACCNUMBER =amountno
        self.username = username
        self.INPUTAMT = inputamount
        self.ACCTYPE = type
    @classmethod
    def display(self):
        """summary
        """
        print("***********************************")
        print("ACCOUNT DETAILS \n")
        print("Account Number : ", self.ACCNUMBER)
        print("Account User Name : ", self.username)
        print("Balance : ", self.INPUTAMT)
        print("Type of Account", self.ACCTYPE)
        print("\nAccount Created!\n")

ACCNUMBER = int(input("Enter account number: \n"))
username = input("Enter the user name: \n")
INPUTAMT = int(input("Enter deposit amount: \n"))
try:
    if INPUTAMT <= 0:
        print("invalid input amount")
except TypeError as excep:
    print("Error is", excep)
finally:
    print("Input amount", INPUTAMT)
ACCTYPE = input("Enter account type: SA for Savings Account, CA for Current Account \n")

str1 = "SA"
str2 = "CA"
try:
    if str1 != "SA":
        print("invalid input")
    elif str2 != "CA":
        print(" invalid type")
except:
    print ("vaild SA/CA")
finally:
    print("Wrong account type")

obj = User()
obj.createuser(ACCNUMBER,username,INPUTAMT,ACCTYPE)
obj.display()

class Depositwithdraw(User):  # derived constructors from parent class
    """summary
    """
    def _init_Deposit(self, totalamount, amount):
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
        except TypeError as excep:
            print("Error is", excep)
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
        except TypeError as excep:
            print("Error is", excep)
        finally:
            print("amount", amount)
        self.totalamount = self.INPUTAMT - amount
        print("Successfully withdraw", self.totalamount)

    def report(self):
        """summary
        """
        print("******************************************\n")
        print(self.ACCNUMBER, " ", self.username, " ", self.INPUTAMT, " ", self.ACCTYPE)
        print("Total amount is:")
        print(self.totalamount)

    def getamountno(self):
        """summary

        Returns:
            type: description
        """
        return self.ACCNUMBER

    def getusername(self):
        """summary

        Returns:
            type: description
        """
        return self.username

    def getdepositamount(self):
        """summary

        Returns:
            type: description
        """
        return self.inputamount

    def getaccounttype(self):
        """summary

        Returns:
            type: description
        """
        return self.ACCTYPE


# class to display main options

obj1 = Depositwithdraw()
obj2 = Depositwithdraw()
obj1.depositamount()
obj2.withdrawamount()
obj2.report()

class Maindisplay(Depositwithdraw):
    """summary

    Args:
        Depositwithdraw (type): description
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
    # system("cls");
    print("\tMAIN MENU")
    print("\t1. Create account")
    print("\t2. Deposit amount")
    print("\t3. Withdraw amount")
    print("\t4. Report ")
    print("\t5. Exit")
    print("\tSelect Your Option (1-5) ")
    CH = input()
    # system("cls");

    if CH == '1':
        obj.createuser()
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
