birthdays = {
    "22 nov": ["Bob Bernt", "Mathias"],
    "10 des": "Elle",
    "31 okt": ["Aragusta", "Carina"],
    "12 jan": "Silje",
    "23 okt": "Willy",
    "5 jul": ["Martin", "Øystein"],
    "11 mar": "Miriam"
}

print("\na) b)")
print(birthdays)


def add_birthday_to_date(date, name):
    try:
        birthdays[date].append(name)
    except AttributeError:
        person = birthdays[date]
        list_of_people = list()
        list_of_people.append(person)
        list_of_people.append(name)
        birthdays[date] = list_of_people
    except KeyError:
        birthdays[date] = name


# add_birthday_to_date("31 okt", "Gunnar")
# print(birthdays)
# add_birthday_to_date("23 okt", "Sunniva")
# print(birthdays)
# add_birthday_to_date("9 feb", "Lillian")
# print(birthdays)


add_birthday_to_date("12 jan", "Sindre")
add_birthday_to_date("9 feb", "Lillian")
print(birthdays)