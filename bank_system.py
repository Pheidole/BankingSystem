''' REMEMBER TO WRITE LOTS OF COMMENTS '''

from customer_account import CustomerAccount
from admin import Admin

accounts_list = []
admins_list = []

class BankSystem(object):
    def __init__(self):
        self.accounts_list = []
        self.admins_list = []
        self.load_bank_data()
    
    def load_bank_data(self):
        
        # create customers
        account_no = 1234
        customer_1 = CustomerAccount("Adam", "Smith", ["14", "Wilcot Street", "Bath", "B5 5RT"], account_no, 5000.00)
        self.accounts_list.append(customer_1)
        
        account_no+=1
        customer_2 = CustomerAccount("David", "White", ["60", "Holborn Viaduct", "London", "EC1A 2FD"], account_no, 3200.00)    
        self.accounts_list.append(customer_2)

        account_no+=1
        customer_3 = CustomerAccount("Alice", "Churchil", ["5", "Cardigan Street", "Birmingham", "B4 7BD"], account_no, 18000.00)
        self.accounts_list.append(customer_3)

        account_no+=1
        customer_4 = CustomerAccount("Ali", "Abdallah",["44", "Churchill Way West", "Basingstoke", "RG21 6YR"], account_no, 40.00)
        self.accounts_list.append(customer_4)
                
        # create admins
        admin_1 = Admin("Julian", "Padget", ["12", "London Road", "Birmingham", "B95 7TT"], "1", "1", True)
        self.admins_list.append(admin_1)

        admin_2 = Admin("Cathy",  "Newman", ["47", "Mars Street", "Newcastle", "NE12 6TZ"], "2", "2", False)
        self.admins_list.append(admin_2)


    def search_admins_by_name(self, admin_username):
        found_admin = None
        for a in self.admins_list:
            lname = a.get_username()
            if lname == admin_username:
                found_admin = a
                break
        if found_admin == None:
            print("\n The Admin %s does not exist! Try again...\n" %admin_username)
            
        return found_admin
    
    def search_admins_by_last_name(self, admin_last_name): #used for editing admin details (checks last name as opposed to checking 'username')
        found_admin = None
        for a in self.admins_list:
            lname = a.get_last_name()
            if lname == admin_last_name:
                found_admin = a
                break
        if found_admin == None:
            print("\n The Admin %s does not exist! Try again...\n" %admin_last_name)
            
        return found_admin
        
    def search_customers_by_name(self, customer_lname):
        found_customer = None
        for a in self.accounts_list: #goes through each entry in account_list
            lastname = a.get_last_name()
            if lastname == customer_lname: #checks each entry last name against the input name
                found_customer = a
                print("customer found") #debugging, delete later
                break
        if found_customer == None:
            print("\n The Customer %s does not exist! Try again...\n" %customer_lname)
            
        return found_customer
        
        
    def main_menu(self):
        #print the options you have
        print()
        print()
        print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print ("Welcome to the Python Bank System")
        print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print ("1) Admin login")
        print ("2) Quit Python Bank System")
        print (" ")
        option = int(input ("Choose your option: "))
        return option


    def run_main_options(self):
        loop = 1         
        while loop == 1:
            choice = self.main_menu()
            if choice == 1:
                username = input ("\nPlease input admin username: ")
                password = input ("\nPlease input admin password: ")
                msg, admin_obj = self.admin_login(username, password)
                print(msg)
                if admin_obj != None:
                    self.run_admin_options(admin_obj)
            elif choice == 2:
                loop = 0
        print ("\nThank-You for stopping by the bank!")


    def transferMoney(self, sender_lname, receiver_lname, receiver_account_no, amount): #Do this after I have done the prerequisite things
        #ToDo
        pass

                
    def admin_login(self, username, password):
        found_admin = self.search_admins_by_name(username) #Checks if parameter username exists
        msg = "\nLogin failed"
        if found_admin != None: #If a matching admin account exists, check for correct password
            if found_admin.get_password() == password:
                msg = "\nLogin successful"
        return msg, found_admin

    def admin_menu(self, admin_obj):
         #print the options you have
         print (" ")
         print ("Welcome Admin %s %s: Avilable options are:" %(admin_obj.get_first_name(), admin_obj.get_last_name()))
         print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
         print ("1) Transfer money")
         print ("2) Customer account operations & profile settings")
         print ("3) Delete customer")
         print ("4) Print all customers detail")
         print ("5) Update administrator details")
         print ("6) Sign out")
         print (" ")
         while True: #Exception handling loop
             try:
                 option = int(input("Choose your option: "))
                 break
             except ValueError:
                 print("Invalid input, please try again")
         return option


    def run_admin_options(self, admin_obj):                                
        loop = 1
        while loop == 1: #Transfer money
            choice = self.admin_menu(admin_obj)
            if choice == 1:
                sender_lname = input("\nPlease input sender surname: ")
                amount = float(input("\nPlease input the amount to be transferred: "))
                receiver_lname = input("\nPlease input receiver surname: ")
                receiver_account_no = input("\n Please input receiver account number: ")
                self.transferMoney(sender_lname, receiver_lname, receiver_account_no, amount)   
                 
            elif choice == 2: #This option is used to access a specific customers account
                customer_name = input("\nPlease input customer surname: \n")
                customer_account = self.search_customers_by_name(customer_name)
                if customer_account != None:
                    customer_account.run_account_options()
            
            elif choice == 3: #Delete customer
                if Admin.has_full_admin_right(admin_obj) == True: #Checks the current logged in administrator for their full administration rights
                    customer_name = input("\nInput customer name you want to delete: ")
                    customer_account = self.search_customers_by_name(customer_name) #Looks to see if the entered account exists in the
                    if customer_account != None:
                        self.accounts_list.remove(customer_account)
                        print("%s was deleted successfully!"%customer_name)
                else:
                    print("\nYou do not have permission to delete customers \n")
            
            elif choice == 4: #Print all customer details
                self.print_all_accounts_details() #Calls fucntion to print all customer account details
                
            elif choice == 5: #Update current logged in administrators details
                if Admin.has_full_admin_right(admin_obj) == True: #Checks whether the current admin has full admin rights
                    admin_last_name = input("\nPlease input admin surname: \n")
                    admin_account = self.search_admins_by_last_name(admin_last_name)
                    if admin_account != None:
                        admin_account.run_account_options() #WHY IS THIS NOT WORKING HAVE TO INVESTIGATE ARRRHHJHHJHJKGHFGJH
                else:
                    print("\nYou do not have full administrator rights")
                
            
            elif choice == 6:
                loop = 0
        print ("\n Exit account operations")


    def print_all_accounts_details(self): 
            # list related operation - move to main.py (not sure what this means)
            i = 0
            for c in self.accounts_list: #For entries in accounts_list
                i+=1 #Iterates every pass through the loop
                print('\n %d. ' %i, end = ' ') #Prints 'i'
                c.print_details() #Prints details of current account entry
                print("------------------------") #Formattting


app = BankSystem()
app.run_main_options()
