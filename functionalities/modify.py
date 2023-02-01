import sys
from functionalities.read_and_write_csvfile import contact, format_contact, search, open_contact_list, update_contacts
from new_contact import phone, email, birthday

## Prepare to modify a contact
def modify(file_name,ctm):
    if contact(file_name, ctm):
        lenght = len(contact(file_name, ctm))
        match lenght:
            case 1:
                mod = input(f"Did you mean {contact(file_name, ctm)[0]['Name']}? (y/n) ").lower()
                if mod == "y":
                    modify_contact(file_name, contact(file_name, ctm)[0]["Name"])
                    sys.exit()
                sys.exit()

            case otrhe:
                for c in contact(file_name, ctm):
                    print(f"{format_contact(c)}\n")

                contact_to_modify = input(f"Wich {ctm} do you want to modify? ")
                if search(file_name, contact_to_modify):
                    modify_contact(file_name, contact_to_modify)
                    sys.exit()
                else:
                    sys.exit(f"{contact_to_modify} is not between your {ctm} contacts")
    else:
        print(f"{ctm} is not between your contacts")            
            
## Modify a contact in the csv file
def modify_contact(file_name, m):
    new_data = []
    mods = 0
    for row in open_contact_list(file_name):
        if m == row["Name"]:
            while True:
                print("Which field do you want modify?\n Name, Phone, Mobile, Brithday, Address, Work, Company, Email, Work Address, Notes or exit")
                mod = input("Modify: ").lower()
                match mod:
                    case "name":
                        new_name = input("New Name: ").title()
                        if new_name:
                            row["Name"] = new_name
                            mods += 1

                    case "phone":
                        new_phone = phone()
                        if new_phone:
                            row["Phone"] = new_phone
                            mods += 1

                    case "mobile":
                        new_phone = phone()
                        if new_phone:
                            row["Mobile"] = new_phone
                            mods += 1

                    case "email":
                        new_email = email()
                        if new_email:
                            row["Email"] = new_email
                            mods += 1

                    case "work":
                        new_work = input("New Work: ")
                        if new_work:
                            row["Work"] = new_work
                            mods += 1

                    case "company":
                        new_company = input("New Company: ")
                        if new_company:
                            row["Company"] = new_company
                            mods += 1

                    case "birthday":
                        new_birthday = birthday()
                        if new_birthday:
                            row["Birthday"] = new_birthday
                            mods += 1

                    case "notes":
                        new_notes = input("New Notes: ").capitalize()
                        if new_notes:
                            row["Notes"] = new_notes
                            mods += 1

                    case "address":
                        new_address = input("New Address: ")
                        if new_address:
                            row["Address"] = new_address
                            mods += 1

                    case "work address":
                        new_work_address = input("New Work Address: ")
                        if new_work_address:
                            row["Work_Address"] = new_work_address

                    case "exit" | "":
                        break

                    case other:
                        sys.exit("Invalid field")
        new_data.append(row)
    changes = input("Do you want to save changes?(y/n):").lower()
    if changes == "y" or "yes":
        update_contacts(file_name, new_data)
    if mods != 0:
        print(f"{m} has been modified")