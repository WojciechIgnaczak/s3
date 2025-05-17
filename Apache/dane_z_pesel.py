# def validate_len(pesel):
#     if len(pesel) != 11:
#         return False
#     if not pesel.isdigit():
#         return False
#     return True

# def sum_control(pesel):
#     wages = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3]
#     sum = 0
#     for i in range(10):
#         sum += int(pesel[i]) * wages[i]
#     control_number = (10 - sum % 10) % 10
#     return control_number == int(pesel[10])

# def validate_pesel(pesel):
#     if not validate_len(pesel):
#         return False
#     if not sum_control(pesel):
#         return False
#     return True

def day_of_birth(pesel):
    return int(pesel[4:6])

def month_of_birth_number(pesel):
    return int(pesel[2:4]) % 20

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