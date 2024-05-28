from datetime import datetime
from collections import UserDict
from birth_in_week import get_upcoming_birthdays, prepare_user_list
import pickle


class Field:
    def __init__(self, value: str):
        self.value = value

    def __str__(self):
        return str(self)


class Name(Field):
    def __init__(self, value: str):
        super().__init__(value)

    def __str__(self):
        return f"Name: {self.value}"


class Phone(Field):
    def __init__(self, value: str):
        """Initialize a Phone object with a given value"""
        if len(value) != 10:
            raise ValueError("Phone number must have 10 digits")
        super().__init__(value)

    def __str__(self):
        return f"Phone: {self.value}"


class Birthday(Field):
    def __init__(self, value):
        try:
            value = datetime.strptime(value, "%d.%m.%Y").date()
            super().__init__(value)
        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")

    def __str__(self):
        return f"{self.value}"


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None

    def add_birthday(self, birthday: str):
        """Add a new birthday to the record"""
        try:
            self.birthday = Birthday(birthday)
        except ValueError as e:
            print(f"The birthday has not been add\n{e}")

    def add_phone(self, phone_number: str):
        """Add a new phone number to the record"""
        self.phones.append(Phone(phone_number))

    def edit_phone(self, old_phone: str, new_phone: str):
        """Edit a phone number in the record"""
        for phone in range(len(self.phones)):
            if self.phones[phone].value == old_phone:
                try:
                    self.phones[phone] = Phone(new_phone)
                except ValueError as e:
                    print(f"The number has not been changed\n{e}")
                break
        else:
            print(f"The number {old_phone} not found")

    def find_phone_name(self, phone_number: str):
        """Find a phone number in the record"""
        for phone in self.phones:
            if phone.value == phone_number:
                return phone_number
        return None

    def find_phone(self):
        """Return the phone number in the record"""
        return [phone.value for phone in self.phones]

        # return phone.value

    def __str__(self):
        if len(self.phones):
            return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}, birthday: {self.birthday}"
        else:
            return f"An error occurred while creating the contact"


class AddressBook(UserDict):
    def add_record(self, record: Record):
        """Add a new record to the address book"""
        self.data[record.name.value] = record

    def find(self, name: str):
        """Find a record in the address book"""
        return self.data[name]

    def delete(self, name: str):
        """Delete a record from the address book"""
        if name in self.data:
            del self.data[name]
        else:
            print(f"Contact {name} not found")

    def save_data(self, filename="addressbook.pkl"):
        """Save the address book data to a file"""
        with open(filename, "wb") as f:
            pickle.dump(self, f)

    @classmethod
    def load_data(cls, filename="addressbook.pkl"):
        """Load the address book data from a file"""
        try:
            with open(filename, "rb") as file:
                return pickle.load(file)
        except FileNotFoundError:
            return cls()


# -------------------------------------------------------------------------------

if __name__ == "__main__":
    # Створення нової адресної книги
    book = AddressBook()

    # Створення запису для John
    john_record = Record("John")
    john_record.add_phone("1234567812")

    # Додавання запису John до адресної книги
    book.add_record(john_record)
