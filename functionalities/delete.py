import sys
from functionalities.read_and_write_csvfile import contact, format_contact, open_contact_list, update_contacts


## Prepare for delete a contact
def delete(file_name, ctd):
    if contact(file_name, ctd):
        lenght = len(contact(file_name, ctd))
        match lenght:
            case 1:
                delete = input(f"Did you mean {contact(file_name, ctd)[0]['Name']}? (y/n) ").lower()
                if delete == "y":
                    ctd = contact(file_name, ctd)[0]['Name']
                    delete_contact(file_name, ctd)
                    sys.exit()

            case other:
                for c in contact(file_name, ctd):
                    print(f"{format_contact(c)}\n")

                delete = input(f"Wich {ctd} do you want to delete? ")
                if delete == contact(file_name, delete)[0]["Name"]:
                    delete_contact(file_name, delete)
                    sys.exit()
                else:
                    sys.exit(f"{delete} is not between your contacts")

    else:
        print(f"{ctd} is not between your contacts")
    
    
## Delete a contact from the csv file
def delete_contact(file_name, d):
    delete = input(f"Do you want to delete {d} form the contact list? (y/n) ").lower()
    if delete == "y" or delete == "yes":
        new_data = [c for c in open_contact_list(file_name) if d != c["Name"]]
        print(f"{d} has been deleted")
        changes = input("Do you want save the changes?(y/n): ").lower()
        if changes == "y" or changes == "yes":
            update_contacts(file_name, new_data)
            print(f"{d} has been deleted")