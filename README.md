# Contact_list
#### Description: A CLI application to store and manage your contacts in the terminal

#### Introduction:
Contact list is an application which uses a csv file to store a simple list of contacts, the app is focused on simple usage and lightweight performance requiring a minimum amount of resources on your device.
### Command List for cli usage

1. **-n, -N**: Create a new contact

     To create a new contact just type the command -n or -N, without any other argument

2. **-m, -M**: Modify a contact

     To modify a contact you must type the command plus a contact name (-m "contact" or -M "contact")

3. **-d, -D**: Delete a Contact

     To delete a contact you must type the command plus a contact name (-d "contact" or -D "contact")

4. **-s, -S**: Search contacts

     To search a contact you must type the command plus a contact name (-s "contact" or -D "contact")

5. **-l, -L**: Print the full list of contacts

     To print the full list of contact you must type the command -l or -L without any other argument

6. **-h, --help**: Shows a help messege with the usage of the application


### Contacts
#### contacts are compounds of ten fields
1. Name  (*Obligatory*)
2. Phone (*Optional*)
3. Mobile (*Optional*)
4. Email (*Optional*)
5. Work (*Optional*)
6. Company (*Optional*)
7. Birthday (*Optional*)
8. Notes (*Optional*)
9. Address (*Optional*)
10. Work_Address (*Optional*)


#### Name
  Name is the only one field which is obligatory in order to be able of search and print the contact with the search, contact and print_contact functions


#### Notes
   The reason to include the field notes in a contact is to be able to write a short note about the contact in order of get clues of who is exactly the person, company or entity behind the contact, clues like where are they from for example


## Functions

1. #### open_contact_list and update_contacts functions
     Since the app works with python's csv module, is needed to open a file.csv whose content is the contact list in order to avoid retype the exact same couple of lines each time the program have to use the file.csv, so I decide to include a function that handle this task.
     This function task it is open the file.csv as a dictionary and yield it line by line in order to be used by the function that called ope_contact_list function.

     The same idea is applied to the update_contacts function, but with a different task to handle.
     This function take a list as argument, this list content is the new data that going to be write on the file.csv in other word take a new list of contacts given by the functions that modify or delete contacts and update the file.csv with the new data

2. #### search and contact functions
     These two functions at first glance look like both of them fulfill the same task, but the reason for including two different functions which handle two very similar tasks is to allow the user to print all contacts that share the start of name like the same name or the same first letter in their names.

     The search function returns true when the name that is search for match exactly with the name in the file.csv whose content is the contact list, by other hand the contact function return a sorted alphabetical list of contacts which started with the keyword of searching, this behavior allows the alphabetical search, also allows do an search using only the first name or searching by first and last name.

3. #### format_contact function
    The task of this function is take the information from the dictionaries in the list geven as argument and reformat it in order to print to the user in a more undertandable way.

    The contacts are printed as follows:

    line 1: Name

    line 2: Phone, Mobile and Birthday

    line 3: Address

    line 4: Work, Company and Email

    line 5: Work Address

    line 6: Notes

    The basic idea behind thes format is easily be able to get the personal information (lines 2 and 3) and the professional information (lines 4 and 5) and the short notes (line 6) of a given contact (line 1).

    This is the output shows in the terminal is:

        Bulma Brief
         Phone: +34-159-753-852  Mobile: +34-159-465-285  Birthday: August 18, 734
         Address: Capsule Corp, Nishinomiya
         Work: Scientist  Company: Capsule Corp.  Email: buruma@capsule.com
         Work Address: Capsule Corp, Nishinomiya
         Notes: She is the greatest inventor of the world.

4. #### delete_contact
     This function adds all the contacts given by the open_contact_list to a list except the contact whose name matches with the name given to the delete_fuction as argument and then calls the update_contacts function with this list as argument. Since once you delete a contact the app has not way to recover it, in order to avoid accidentally delete a contact the function ask for confirmation twice before to delete a contact.

     If the argument of the function not is a fully match with some contact, the function is going to shows to the user a list of contacts that its name started with the argument and ask the user to choose which one is going to delete, for example if the argument is "A" the function is going to shows all the contacts started by "A".


5. #### Modify
     The task of this function is modify a contact in order to do so, its work is divided in two different subtask
     - 1 modify each field of a contact separately
     - 2 create a list with all contacts in file.csv but with the data of the contact that was modified in the subtask 1

     The behavior in the first subtask is allows to modify every field one by one, no matter in which order you type each field, in order to do so, the function print a list of keywords which are the fields plus the "exit" keyword and then ask the user for the keyword corresponding to which field the user is going to modify. This behavior continues in an infinite loop until the user types the keyword "exit" or hits enter without any keyword, this allows continues type and retype the changes in all the fields without worry of doing something wrong because the file.csv won't be updated until the user decide to exit from the loop and save all changes. If the user type wrong data(see **get_phone, get_birthday and add_email**) the modify function is going to ignore the new inputs and keep the old data.

     If the argument of the function not is a fully match with some contact, the function is going to shows to the user a list of contacts that its name started with the argument and ask the user to choose which one is going to modify, for example if the argument is "A" the function is going to shows all the contacts started by "A".

     The second subtask of the function create a list of all contacts in file.csv, but substituting in the contact which was modified in the first subtask, the data of the fields that was modified with the new data given by the user, and then after the confirmation of the user, proceed to update the file.csv calling the function update_contacts with the list recently created as argument.

6. #### get_phone, get_birthday and add_email
    These three functions were added in order to prevent the user input wrong data the the fields phone, mobile, birthday and email. The behavior of these three functions is very similar, each function allows the user input the data, if the data is correct the field is going to be filled with the data given by the user; otherwise, the field is going to be filled with a void string. I if the fields were filled with void string once the data is saved, the user can change the void string using the modify function to modify the contact with void strings in its fields.

    The get_phone check if the number given by the user in the fields "phone" and "mobile" is actually a phone number, when the user type something that is not a phone number the function returns None and the field is filled with a void string.

    The get_birthday checks if the date given by the user is in the format year/month/day, and if the input of the user is a date, in this field the year is optional but even if the user does not type a year the format of date still the same. After the check becomes true, the function reformat the date to a more understandable format as follows: name_of_month day, year. When the user type something that is not a date or type a date in a wrong format the function returns None and the field is filled with a void string.

    This is the output in the terminal:

        Birthday: August 18, 734

    In the case of add_email function its allows type the email and check if the input is an email, when the user type something that is not an email, the function ask if the user want to retype the email, in case of confirmation the function ask again to the user for an email, this behavior is repeated three times. When the user does not want to retype their email or type three times something that's not an email the function returns None and the field is filled with a void string.




