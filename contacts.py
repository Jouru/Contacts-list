import argparse
import sys
import os
import csv
from new_contact.add_contact import Contact
from functionalities import modify, delete, list_contacts, print_contact

def main():
    ## Add the comands for the CLI
    parser = argparse.ArgumentParser(description="A comand line contact list app")
    parser.add_argument("-n", "-N", help="Add new Contact", action="store_true")
    parser.add_argument("-l", "-L", help="List all contacts", action="store_true")
    parser.add_argument("-s", "-S", help="-s 'contact' to Search a contact", nargs="+")
    parser.add_argument("-m", "-M", help="-m 'contact' to modify a contact", nargs="+")
    parser.add_argument("-d", "-D", help="Delete contact", nargs="+")
    args = parser.parse_args()    
    
    file_name = ".contacts.csv"
    if not os.path.isfile(file_name):
        with open(file_name, "w") as file:
            writer = csv.DictWriter(file, fieldnames=["Name", "Phone", "Mobile", "Email", "Work", "Company", "Birthday", "Notes", "Address", "Work_Address"])
            writer.writeheader()
    try:
        if args.n:
            Contact(file_name)
        elif args.s:
            s = " ".join(args.s)
            print_contact(file_name, s)
        elif args.l:
            list_contacts(file_name)
        elif args.m:
            ctm = " ".join(args.m)
            modify(file_name, ctm)
        elif args.d:
            ctd = " ".join(args.d)
            delete(file_name, ctd)
        else:
            print("Use -h or --help to get the user guide")
    
    except KeyboardInterrupt:
        sys.exit("\n")
    


if __name__=="__main__":
    main()
