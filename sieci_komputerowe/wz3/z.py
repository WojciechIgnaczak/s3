import sys
def bin_to_addr(ip):
    first = (ip >> 24)
    second = (ip >> 16) & 0xFF
    third = (ip >> 8) & 0xFF
    last = (ip & 0xFF)
    adres=f"{first}.{second}.{third}.{last}"
    return adres

#addr=sys.argv[1]
addr="78.100.240.0/26"
addr=addr.split("/")
ip=addr[0]
mask=addr[1]
ip=ip.split(".")
ip=(int(ip[0])<<24)|(int(ip[1])<<16)|(int(ip[2])<<8)|(int(ip[3]))
print("adres ip",bin_to_addr(ip))

mask=int("1"*int(mask)+"0"*(32-int(mask)),2)
print("adres maski",bin_to_addr(mask))

adres_sieci=ip & mask
print("adres_sieci",bin_to_addr(adres_sieci))

adres_broadcast=adres_sieci | (~mask & 0xFFFFFFFF)
print("adres_broadcast",bin_to_addr(adres_broadcast))

host_count=pow(2,32-int(addr[1]))-2
print("Host count: "+str(host_count))

pierwszy_host=adres_sieci+1
print("pierwszy_host",bin_to_addr(pierwszy_host))

ostani_host=adres_broadcast-1
print("ostani_host",bin_to_addr(ostani_host))