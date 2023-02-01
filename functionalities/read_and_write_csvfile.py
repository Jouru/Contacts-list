import csv

def open_contact_list(file_name):
    with open(file_name, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            yield(row)

## Check if a contact there exist in the csv file
def search(file_name, c):
    for row in open_contact_list(file_name):
        if c == row["Name"]:
            return True
        
## Search contacts in the csv file
def print_contact(file_name, s):
    if contact(file_name, s):
        contacts = contact(file_name, s)
        for c in contacts:
            print(f"{format_contact(c)}\n")
    else:
        print(f"{s} is not between your contacts")

## Get a chunk of contacts
def contact(file_name, c):
    contacts = [row for row in open_contact_list(file_name) if row["Name"].startswith(c)]
    return sorted(contacts, key=lambda contact: contact["Name"])

## Print all contacts in a list
def list_contacts(file_name):
    contacts = [row for row in open_contact_list(file_name)]
    for c in sorted(contacts, key=lambda contact: contact["Name"]):
        print(f"{format_contact(c)}\n")
        
        
def format_contact(contacts):
    fhkeys = [
        "Phone",
        "Mobile",
        "Birthday",
    ]

    shkeys = [
        "Work",
        "Company",
        "Email",
    ]
    first_half = [f"{key}: {contacts[key]}" for key in fhkeys if contacts[key] != ""]
    second_half = [f"{key}: {contacts[key]}" for key in shkeys if contacts[key] != ""]
    fhdata = "  ".join(first_half)
    shdata = "  ".join(second_half)
    if contacts["Address"] != "":
        fhdata = f"{fhdata}\n Address: {contacts['Address']}"
    if contacts["Work_Address"] != "":
        shdata = f"{shdata}\n Work Address: {contacts['Work_Address']}"
    if contacts["Notes"] != "":
        shdata = f"{shdata}\n Notes: {contacts['Notes']}"
    return f"{contacts['Name']}\n {fhdata}\n {shdata}"


## Update the csv file
def update_contacts(file_name, u):
    with open(file_name, "w") as file:
        writer = csv.DictWriter(file, fieldnames=["Name", "Phone", "Mobile", "Email", "Work", "Company", "Birthday", "Notes", "Address", "Work_Address"])
        writer.writeheader()
        for row in u:
            writer.writerow(row)