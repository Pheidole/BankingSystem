
class CustomerAccount:
    def __init__(self, fname, lname, address, account_no, balance):
        self.fname = fname
        self.lname = lname
        self.address = address
        self.account_no = account_no
        self.balance = float(balance)
    
    def update_first_name(self, fname):
        self.fname = fname
    
    def update_last_name(self, lname):
        self.lname = lname
                
    def get_first_name(self):
        return self.fname
    
    def get_last_name(self):
        return self.lname
        
    def update_address(self, addr):
        self.address = addr
        
    def get_address(self):
        return self.address
    
    def deposit(self, amount):
        self.balance += amount #Amount deposited added to account balance
        
    def withdraw(self, amount):
        self.balance -= amount #Amount withdrawn subtracted from account balance
        
    def print_balance(self):
        print("\n The account balance is %.2f" %self.balance)
        
    def get_balance(self):
        return self.balance
    
    def get_account_no(self):
        return self.account_no
    
    def account_menu(self):
        print ("\n Your Transaction Options Are:")
        print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print ("1) Deposit money")
        print ("2) Withdraw money")
        print ("3) Check balance")
        print ("4) Update customer name")
        print ("5) Update customer address")
        print ("6) Show customer details")
        print ("7) Back")
        print (" ")
        option = int(input ("Choose your option: "))
        return option
    
    def print_details(self):
        #STEP A.4.3
        print("First name: %s"%self.fname)
        print("Last name: %s"%self.lname)
        print("Account No: %s"%self.account_no)
        print("Address: %s"%self.address[0])
        print("         %s"%self.address[1])
        print("         %s"%self.address[2])
        print("         %s"%self.address[3])
        print(" ")
   
    def run_account_options(self):
        loop = 1
        while loop == 1:
            choice = self.account_menu()
            if choice == 1: #Deposit money
                amount = float(input("\n Please enter amount to be deposited: "))
                self.deposit(amount)
                self.print_balance()
            elif choice == 2: #Withdraw money
                amount = float(input("\n Please enter amount to be withdrawn: "))
                self.withdraw(amount)
                self.print_balance()
            elif choice == 3: #Print balance
                self.print_balance()
            elif choice == 4: #Update customer name
                fname = input("\n Enter new customer first name: ")
                self.update_first_name(fname)
                lname = input("\n Enter new customer last name: ")
                self.update_last_name(lname)
            elif choice == 5: #Update address 
                '''MIGHT WANT TO REVISIT THIS TO USE self.update_address SOMEHOW'''
                self.address[0] = input("Enter house/flat number: ")
                self.address[1] = input("Enter street: ")
                self.address[2] = input("Enter city/town: ")
                self.address[3] = input("Enter postcode: ")
                
            elif choice == 6: #Prints customer details
                self.print_details()
            elif choice == 7:
                loop = 0
        print ("\n Exit account operations")