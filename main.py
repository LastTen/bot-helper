# Pars the user input
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


# Add contact to the data base
def add_contact(args: list, phone_base: dict):
    if len(args) != 2:
        return "Invalid argument."
    name, phone = args
    if name in phone_base:
        return "Contact already exists."
    phone_base[name] = phone
    return "Contact added."


# Change contact to the data base
def change_contact(args: list, phone_base: dict):
    if len(args) != 2:
        return "Invalid argument."
    name, phone = args
    if name in phone_base:
        phone_base[name] = phone
        return "Contact changed."
    return "Contact not found."


# Show contact information in the data base
def show_phone(args: list, phone_base: dict):
    if len(args) != 1:
        return "Invalid argument."
    name = args[0]
    if name in phone_base:
        return phone_base[name]
    return "Contact not found."


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
            for name, phone in contacts.items():
                print(f"{name}: {phone}")
            print("\n")
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
