class ATM:
    def __init__(self,id,name,address,card_number,card_pin,status,balance): 
        self.id = id
        self.name = name
        self.address = address
        self.card_number = card_number
        self.card_pin = card_pin
        self.status = status
        self.balance = balance
    def withdraw(self,money):
        if self.balance > money:
            self.balance -= money
            print("You withdraw",money)
            print("Your current balance is", self.balance)
        else:
            print("Sorry for inconvence, your balance does not have enough money")
    def deposit(self,dep):
        self.balance += dep
        print("We already proceeded your deposit, your current balance is",self.balance)
    def newpin(self):
        data = input("Do you want to change your pin number? (y,n): ")
        while True:
            if data == "y":
                confirm_pin = input("Please enter your old current")
                if confirm_pin == self.card_pin:
                    self.card_pin = input("Please enter your new pin")
                else:
                    print("Your pin is incorrect, please try again")
                    break
            elif data == "n":
                print("Thank you for your cooperation")
                break
            else:
                print("Please select again (y/n)")
    def newstat(self):
        input = input("Do you want to update your status? (y/n): ")
        if input == "y":
            newstate = input("please select number 1 for active and 2 for inactive: ")
            if int(newstate) == 1:
                self.status = "Active"
                print("Now your status is", self.status)
            elif int(newstate) == 2:
                self.status = "Inactive"
                print("Now your status is",self.status)
            else:
                print("Your input is incorrect, please try again later")
        else:
            print("Thank you for your cooperation")
    def check(self):
        print("Now your current balance is",self.balance)

p1 = ATM(1,"Alice", "123 Main Street", "1234-5678-9012-3456", "1234", "Active", 1000)
p2 = ATM(2,"Bob", "456 Elm Street", "9876-5432-1098-7654", "5432", "Active", 500)
p3 = ATM(3,"Carol", "789 Oak Street", "0123-4567-8901-2345", "8901", "Active", 250)
p4 = ATM(4,"Dave", "1011 Pine Street", "1111-2222-3333-4444", "2222", "Active", 100)
p5 = ATM(5,"Eve", "1213 Maple Street", "2222-3333-4444-5555", "3333", "Active", 50)
p6 = ATM(6,"Frank", "1314 Birch Street", "3333-4444-5555-6666", "4444", "Active", 25)
