def bin_to_addr(ip):
    first = (ip >> 24)
    second = (ip >> 16) & 0xFF
    third = (ip >> 8) & 0xFF
    last = (ip & 0xFF)
    adres=f"{first}.{second}.{third}.{last}"
    return adres

def ip_info(addr):
    addr=addr.split("/")
    ip=addr[0]
    mask=addr[1]
    ip=ip.split(".")
    ip=(int(ip[0])<<24)|(int(ip[1])<<16)|(int(ip[2])<<8)|(int(ip[3]))
  #  print("adres ip",bin_to_addr(ip))

    mask=int("1"*int(mask)+"0"*(32-int(mask)),2)
   # print("adres maski",bin_to_addr(mask))

    adres_sieci=ip & mask
    #print("adres_sieci",bin_to_addr(adres_sieci))

    adres_broadcast=adres_sieci | (~mask & 0xFFFFFFFF)
    #print("adres_broadcast",bin_to_addr(adres_broadcast))

    host_count=pow(2,32-int(addr[1]))-2
    #print("Host count: "+str(host_count))

    pierwszy_host=adres_sieci+1
    #print("pierwszy_host",bin_to_addr(pierwszy_host))

    ostani_host=adres_broadcast-1
    #print("ostani_host",bin_to_addr(ostani_host))


def maska(liczba_ip):
    for i in reversed(range(32)):
        if (liczba_ip<(pow(2,32-i)-2)):
            return i



addr="78.100.240.0/26"
addr=addr.split("/")

it=50
it*=1.5

hr=12
hr*=1.5

ksiegowosc=10
ksiegowosc*=1.5

magazyn=5
magazyn*=1.5

siec_dla_gosci=100
siec_dla_gosci*=1.5


it=round(it+1)
hr=round(hr+1)
ksiegowosc=round(ksiegowosc+1)
magazyn=round(magazyn+1)
siec_dla_gosci=round(siec_dla_gosci+1)


host_count=pow(2,32-int(addr[1]))-2

if((it+hr+ksiegowosc+magazyn+siec_dla_gosci) > host_count):
    print("Za mało adresów ip")
print(host_count)
print(it,hr,ksiegowosc,magazyn,siec_dla_gosci)


it_mask=maska(it)
hr_mask=maska(hr)
ksiegowosc_mask=maska(ksiegowosc)
magazyn_mask=maska(magazyn)
siec_dla_gosci_mask=maska(siec_dla_gosci)
print(it_mask,hr_mask,ksiegowosc_mask,magazyn_mask,siec_dla_gosci_mask)




