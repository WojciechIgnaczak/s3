def control_sum(pesel):
    wages=[1,3,7,9,1,3,7,9,1,3]
    sum=0
    for i in range(len(wages)):
        sum+=wages[i]*int(pesel[i])
    
    result=str(sum)[-1]
    return 10-int(result)


def check_control_sum(pesel):
    check_sum=control_sum(pesel)
    if check_sum==int(pesel[-1]):
        return True 
    else: return False


def sex_result_short(pesel):
    if int(pesel[9])%2==0:
        return "K"
    else:
        return "M"


def sex_result_long(pesel):
    if int(pesel[9])%2==0:
        return "Kobieta"
    else:
        return "Mężczyzna"   


def month_number(pesel):
    month=int(pesel[2:4])%20
    if month < 10:
        return f"0{month}"
    return str(month)


def month_name(pesel):
    months={1:"styczeń",2:'luty',3:'marzec',4:'kwiecień',5:'maj',6:'czerwiec',7:'lipiec',8:'sierpień',9:'wrzesień',10:'październik',11:'listopad',12:'grudzień'}
    month=int(pesel[2:4])%20
    return months[month]


def year_of_birth(pesel):
    month=pesel[2:4]    
    century=''
    if int(month)>80 and int(month)<=92:
        century= '18'
    elif int(month)>0 and int(month)<=12:
        century= '19'
    if int(month)>20 and int(month)<=32:
        century= '20'
    if int(month)>40 and int(month)<=52:
        century= '21'
    if int(month)>60 and int(month)<=72:
        century= '22'

    year=century+pesel[0:2]
    return year


def day_of_birth(pesel):
    return pesel[4:6]


def date_of_birth(pesel):
    year=year_of_birth(pesel)
    month=month_number(pesel)
    day=day_of_birth(pesel)
    return f"{day}-{month}-{year}"




pesel='04241004933'
print(control_sum(pesel))
print(check_control_sum(pesel))
print(sex_result_long(pesel))
print(sex_result_short(pesel))
print(month_name(pesel))
print(month_number(pesel))
print(year_of_birth(pesel))
print(day_of_birth(pesel))
print(date_of_birth(pesel))