def validate_len(pesel):
    if len(pesel) != 11:
        return False
    if not pesel.isdigit():
        return False
    return True

def sum_control(pesel):
    wages = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3]
    sum = 0
    for i in range(10):
        sum += int(pesel[i]) * wages[i]
    control_number = (10 - sum % 10) % 10
    return control_number == int(pesel[10])

def validate_pesel(pesel):
    if not validate_len(pesel):
        return False
    if not sum_control(pesel):
        return False
    return True

def day_of_birth(pesel):
    return int(pesel[4:6])

def month_of_birth_number(pesel):
    return int(pesel[2:4]) % 20

def month_of_birth_name(pesel):
    months = {
        1: "styczeń",
        2: "luty",
        3: "marzec",
        4: "kwiecień",
        5: "maj",
        6: "czerwiec",
        7: "lipiec",
        8: "sierpień",
        9: "wrzesień",
        10: "październik",
        11: "listopad",
        12: "grudzień"
    }
    return months[month_of_birth_number(pesel)]

def year_of_birth(pesel):
    month = int(pesel[2:4])
    year = int(pesel[0:2])

    if 80 <= month <= 92:
        return 1800 + year
    elif 0 <= month <= 12:
        return 1900 + year
    elif 20 <= month <= 32:
        return 2000 + year
    elif 40 <= month <= 52:
        return 2100 + year
    elif 60 <= month <= 72:
        return 2200 + year
    else:
        raise ValueError("Nieprawidłowy miesiąc w PESEL")

def sex(pesel):
    if int(pesel[9]) % 2 == 0:
        return "Kobieta"
    else:
        return "Mężczyzna"



pesel = input("Podaj PESEL: ")

if validate_pesel(pesel):
    print("\n✅ PESEL poprawny!")
    
    year = year_of_birth(pesel)
    month_num = month_of_birth_number(pesel)
    month_name = month_of_birth_name(pesel)
    day = day_of_birth(pesel)
    
    print(f"Data urodzenia (rrrr-mm-dd): {year}-{month_num:02d}-{day:02d}")
    print(f"Data urodzenia (słownie): {day} {month_name} {year}")
    print(f"Płeć: {sex(pesel)}")
else:
    print("\n❌ Niepoprawny PESEL!")
