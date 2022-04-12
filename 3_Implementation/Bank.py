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
    def __init__(self,amountno, username, inputamount, type):
        self.ACCNUMBER =amountno
        self.username = username
        self.INPUTAMT = inputamount
        self.ACCTYPE = type

    def display(self):
        """summary
        """
        print("***********************************")
        print("ACCOUNT DETAILS \n")
        print("Account Number : ", self.ACCNUMBER)
        print("Account User Name : ", self.username)
        print("Balance : ", self.INPUTAMT)
        print("type of Account", self.ACCTYPE)
        print("\nAccount Created!\n")


ACCNUMBER = input("Enter account number: \n")
username = input("Enter the user name: \n")
INPUTAMT = int(input("Enter deposit amount: \n"))
try:
    if INPUTAMT <= 0:
        print("invalid input amount")
except:
    ValueError
finally:
    print("Input amount", INPUTAMT)
ACCTYPE = input("Enter account type: SA for Savings Account, CA for Current Account \n")

obj = User(ACCNUMBER, username, INPUTAMT, ACCTYPE)
obj.display()


# derived/child class for method print details


class depositwithdraw(User):  # derived constructors from parent class
    """summary
    """
    def __init__(self, totalamount, amount):
        self.totalamount = totalamount
        self.amount = amount

    def depositamount(self):
        """summary
        """
        print("******************************************")
        amount = int(input("Enter amount to be deposited"))
        try:
            if amount <= 0:
                print("invalid")
        except:
            ValueError
        finally:
            print("amount", amount)
        self.totalamount = self.INPUTAMT + amount
        print("Successfully Deposited", self.totalamount)

    def withdrawamount(self):
        """summary
        """
        amount = int(input("Enter amount to be withdraw"))
        try:
            if amount <= 0:
                print("invalid")
        except:
            ValueError
        finally:
            print("amount", amount)
        self.totalamount = self.INPUTAMT - amount
        print("Successfully withdraw", self.totalamount)

    def report(self):
        """summary
        """
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

obj1 = depositwithdraw(1234, 5000)
obj2 = depositwithdraw(1234, 5000)
obj1.depositamount()
obj2.withdrawamount()
obj2.report()

class maindisplay(depositwithdraw):
    """summary

    Args:
        depositwithdraw (type): description
    """
    global ACCNUMBER
    global USERNAME
    global INPUTAMT
    global ACCTYPE

    def intro(self):
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
    print("\t2. DEPOSIT amount")
    print("\t3. WITHDRAW amount")
    print("\t4. Report ")
    print("\t5. EXIT")
    print("\tSelect Your Option (1-5) ")
    CH = input()
    # system("cls");

    if CH == '1':
        obj.display()
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

obj3 = maindisplay()
obj3.intro()