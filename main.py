# decorator error message
def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except IndexError as e:
            return "Enter phone 'name' or command all "
        except KeyError as e:
            return "Contact not found"

    return inner


# Pars the user input
@input_error
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


# Add contact to the data base
@input_error
def add_contact(args: list, phone_base: dict):
    name, phone = args
    if name in phone_base:
        return "Contact already exists."
    phone_base[name] = phone
    return "Contact added."


# Change contact to the data base
@input_error
def change_contact(args: list, phone_base: dict):
    name, phone = args
    phone_base[name] = phone
    return "Contact changed."


# Show contact information in the data base
@input_error
def show_phone(args: list, phone_base: dict):
    name = args[0]
    return phone_base[name]


# The main function
def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts), "\n")
        elif command == "change":
            print(change_contact(args, contacts), "\n")
        elif command == "phone":
            print(show_phone(args, contacts), "\n")
        elif command == "all":
            if len(contacts) == 0:
                print("Contacts are empty\n")
                continue
            for name, phone in contacts.items():
                print(f"{name}: {phone}")
            print("\n")
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
