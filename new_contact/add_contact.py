import sys
import csv
from new_contact import phone, email, birthday
from functionalities import modify_contact, search


class Contact():
    def __init__ (self, file_name):    
        ## Personal information
        self.Name = name(file_name)
        self.Phone = phone()
        self.Mobile = phone()
        self.Birthday = birthday()
        self.Address = address()
        
        ## Professional information
        self.Work = work()
        self.Company = company()        
        self.Email = email()
        self.Work_Address = address()
        
        ## Other stuff
        self.Notes = notes()
        
        save_contact = input("Save contact? ").lower()
        if save_contact == "y" or save_contact == "yes":
            with open(file_name, "a") as file:
                writer = csv.DictWriter(file, fieldnames=["Name", "Phone", "Mobile", "Email", "Work", "Company", "Birthday", "Notes", "Address", "Work_Address"])
                writer.writerow(
                    {
                        "Name":self.Name, "Phone":self.Phone, "Mobile":self.Mobile,
                        "Email":self.Email, "Work":self.Work, "Company":self.Company,
                        "Birthday":self.Birthday, "Notes":self.Notes, "Address":self.Address,
                        "Work_Address":self.Work_Address
                    }
                )
            print(f"{self.Name} saved")
    


## Getting personal information
def name(file_name):
    name = input("Name: ").title()
    if not name:
        sys.exit("Your contact must have a name")
    if search(file_name, name):
        print(f"{name} already exist between your contacts")
        if input(f"Do you want modify {name}? (y or n) ").lower() == "y":
            modify_contact(file_name, name)
            sys.exit()
        else:
            sys.exit("Please change the name of the new contact")
    return name    
    
def work():
    work = input("Work/Occupation: ")
    return work

def company():
    company = input("Company: ")
    return company


## ## Other stuff
def notes():
    notes = input("Note: ").capitalize()
    return notes

def address():
    address = input("Address/Work address: ")
    return address

