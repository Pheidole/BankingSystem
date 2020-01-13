
class Admin:
    
    def __init__(self, fname, lname, address, user_name, password, full_rights):
        self.fname = fname
        self.lname = lname
        self.address = address
        self.user_name = user_name
        self.password = password
        self.full_admin_rights = full_rights
    
    def update_first_name(self, fname): #use this
        self.fname = fname
    
    def update_last_name(self, lname): #use this
        self.lname = lname
                
    def get_first_name(self):
        return self.fname
    
    def get_last_name(self):
        return self.lname
        
    def update_address(self, addr):
        self.address = addr
    
    def set_username(self, uname): #use this
        self.user_name = uname
        
    def get_username(self):
        return self.user_name
        
    def get_address(self):
        return self.address      
    
    def update_password(self, password): #use this
        self.password = password
    
    def get_password(self):
        return self.password
    
    def set_full_admin_right(self, admin_right):
        self.full_admin_rights = admin_right

    def has_full_admin_right(self):
        return self.full_admin_rights
    
    def print_details(self):
        #STEP A.4.3
        print("First name: %s"%self.fname)
        print("Last name: %s"%self.lname)
        print("Username: %s"%self.user_name)
        print("Password: %s"%self.password)
        print("Address: %s"%self.address[0])
        print("         %s"%self.address[1])
        print("         %s"%self.address[2])
        print("         %s"%self.address[3])
        print(" ")
    
    def account_menu(self):
        print ("\n Your Administrator Options Are:")
        print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print ("1) Update administrator name")
        print ("2) Update administrator address")
        print ("3) Update username")
        print ("4) Update password")
        print ("5) Show administrator details")
        print ("6) Back")
        print (" ")
        option = int(input ("Choose your option: "))
        return option
    
    def run_account_options(self):
        loop = 1
        while loop == 1:
            choice = Admin.account_menu(self)
            if choice == 1: #Update administrator name
                fname = input("\n Enter new administrator first name: ")
                self.update_first_name(fname)
                lname = input("\n Enter new administrator last name: ")
                self.update_last_name(lname)
                
            elif choice == 2: #Update address
                self.address[0] = input("Enter house/flat number: ")
                self.address[1] = input("Enter street: ")
                self.address[2] = input("Enter city/town: ")
                self.address[3] = input("Enter postcode: ")
                
            elif choice == 3: #Update username
                username = input("\nEnter new username: ")
                self.set_username(username)
                
            elif choice == 4: #Update password
                password = input("\nEnter new password: ")
                self.update_password(password)
                
            elif choice == 5: #Prints administrator details
                Admin.print_details(self)
                
            elif choice == 6:
                loop = 0
        print ("\n Exit account operations")

