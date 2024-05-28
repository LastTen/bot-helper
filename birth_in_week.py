from datetime import datetime, date, timedelta


def string_to_date(date_string):
    return datetime.strptime(date_string, "%Y.%m.%d").date()


def date_to_string(date):
    return date.strftime("%Y.%m.%d")


def prepare_user_list(user_data):
    prepared_list = []
    for user in user_data:
        if user["birthday"] is not None:
            prepared_list.append(
                {"name": user["name"], "birthday": string_to_date(user["birthday"])}
            )
    return prepared_list


def get_upcoming_birthdays(users, days=7):
    upcoming_birthdays = []
    today = date.today()
    for user in users:
        new_data = user["birthday"].replace(year=today.year)
        delta = int((new_data - today).days)
        if delta <= days and delta > 0:
            data = {
                "name": user["name"],
                "congratulation_date": date_to_string(new_data),
            }
            upcoming_birthdays.append(data)

    return upcoming_birthdays


if __name__ == "__main__":
    users = [
        {"name": "Sarah Lee", "birthday": None},
        {"name": "John Doe", "birthday": "1985.08.20"},
        {"name": "Jane Smith", "birthday": "1990.05.28"},
        {"name": "John Doe", "birthday": "1985.01.23"},
    ]

    print(get_upcoming_birthdays(prepare_user_list(users), 7))
