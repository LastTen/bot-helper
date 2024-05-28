from birth_in_week import (
    get_upcoming_birthdays,
    prepare_user_list,
    date_to_string,
)
from datetime import datetime

# Phone, Name, Birthday do not delete from next row
from address_book import AddressBook, Record, Phone, Name, Birthday


# decorator error message
def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError as e:
            return f"{e}\nInvalid input"
        except IndexError as e:
            return "Enter phone 'name' or command all "
        except KeyError as e:
            return "Contact not found"
        except AttributeError as e:
            return "No data available"

    return inner


# Pars the user input
@input_error
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


# Add contact to the data base
@input_error
def add_contact(args: list, book: AddressBook):
    """Add a new contact to the data base"""
    name, phone = args
    if len(phone) != 10:
        raise ValueError("Phone must be 10 characters")
    if name in book:
        user = book.find(name)
        user.add_phone(phone)
        return f"Phone added to {name}"
    else:
        user = Record(name)
        user.add_phone(phone)
        book.add_record(user)
        return "New contact added."


# Change contact to the data base
@input_error
def change_contact(args: list, book: AddressBook):
    """Change a contact in the data base"""
    name, old_phone, new_phone = args
    user = book.find(name)
    user.edit_phone(old_phone, new_phone)
    return "Contact changed."


# Show contact information in the data base
@input_error
def show_phone(args: list, book: AddressBook):
    """Show contact information"""
    name = args[0]
    user = book.find(name).find_phone()
    return user


@input_error
def add_birthday(args: str, book: AddressBook):
    """Add birth to user in book"""
    name, date = args
    try:
        datetime.strptime(date, "%d.%m.%Y").date()
        if name in book:
            user = book.find(name)
            user.add_birthday(date)
            return "Birthday added."
        else:
            return "Contact not found."
    except ValueError as e:
        return e


@input_error
def show_birthday(args: str, book: AddressBook):
    """Show user birthday"""
    name = args[0]
    user = book.find(name)
    return user.birthday.value.strftime("%d.%m.%Y")


@input_error
def birthdays(book: AddressBook):
    """List of Birthdays"""
    users = []
    for name, record in book.data.items():
        birth = date_to_string(record.birthday.value)
        name_user = record.name.value
        users.append({"name": name_user, "birthday": birth})

    return get_upcoming_birthdays(prepare_user_list(users), 7)


# The main function
def main():
    book = AddressBook.load_data()
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            book.save_data()
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")

        elif command == "add":
            print(add_contact(args, book))

        elif command == "change":
            print(change_contact(args, book))

        elif command == "phone":
            contacts = show_phone(args, book)
            if isinstance(contacts, list):
                print("\n".join(contacts))
            else:
                print(contacts)

        elif command == "all":
            if len(book.data.items()) == 0:
                print("Contacts are empty\n")
                continue
            for name, record in book.data.items():
                print(record)

        elif command == "add-birthday":
            print(add_birthday(args, book))

        elif command == "show-birthday":
            print(show_birthday(args, book))

        elif command == "birthdays":
            user = birthdays(book)
            if len(user) != 0 and isinstance(user, list):
                for user in user:
                    print(
                        f"{user['name']} celebration birthday {user['congratulation_date']}",
                        sep="\n",
                    )
            else:
                print("No upcoming birthdays")

        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
