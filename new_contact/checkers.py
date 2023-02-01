import re
import calendar
import phonenumbers
from validator_collection import checkers

def email():
    i = 0
    while i < 3:
        try:
            email =  input("Email: ")
            if checkers.is_email(email):
                return email
            if i < 2:
                if input("Invalid email\nDo you wnat to retype your email? (y/n) ").lower() == "y":
                    raise ValueError
                else:
                    break
            elif i == 2:
                print("Invalid Email")
        except ValueError:
            pass
        i += 1 

def phone():
    print("Phone/Mobile:")
    code = input("Country code (e,g: US for United State): ").upper()
    if code:
        try:
            phone = phonenumbers.parse(input(f"Phone: "),code)
            if phonenumbers.is_valid_number(phone):
                return phonenumbers.format_number(phone, phonenumbers.PhoneNumberFormat.E164)
            else:
                print("invalid phone number")
        except phonenumbers.phonenumberutil.NumberParseException:
            print("invalid phone number")
    else:
        phone = input("Phone: ")
        if (phone.removeprefix("+")).isdigit() and len(phone) <= 15:
            return phone
        else:
            print("invalid phone number")

def birthday():
    date = input("Birthday (YYYY/MM/DD): ")
    if matches := re.search(r"^(\d{3,4})?/?(\d{1,2})/(\d{1,2})$", date, re.ASCII):
        try:
            month = calendar.month_name[int(matches.group(2))]
            m = d = ""
            if month:
                match month:
                    case "January" | "March" | "May" | "July" | "August" | "October" | "December":
                        if int(matches.group(3)) > 0 and int(matches.group(3)) <= 31:
                            m = month
                            d = matches.group(3)

                    case "April" | "June" | "September" | "November":
                        if int(matches.group(3)) > 0 and int(matches.group(3)) <= 30:
                            m = month
                            d = matches.group(3)

                    case "February":
                        if matches.group(1):
                            if calendar.isleap(int(matches.group(1))):
                                if int(matches.group(3)) > 0 and int(matches.group(3)) <= 29:
                                    m = month
                                    d = matches.group(3)
                            if int(matches.group(3)) > 0 and int(matches.group(3)) <= 28:
                                m = month
                                d = matches.group(3)
                        else:
                            if int(matches.group(3)) > 0 and int(matches.group(3)) <= 29:
                                m = month
                                d = matches.group(3)

                if m and d:
                    if matches.group(1):
                        date = f"{m} {d}, {matches.group(1)}"
                        return date
                    date = f"{m} {d}"
                    return date

        except IndexError:
            print("Invalid date")
