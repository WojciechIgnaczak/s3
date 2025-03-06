addr="55.105.125.168/30"
addr=addr.split("/")
ip=addr[0]
mask=addr[1]
ip=ip.split(".")
ip_bit=(int(ip[0])<<24)|(int(ip[1])<<16)|(int(ip[2])<<8)|(int(ip[3]))
#print("{0:b}".format(ip_bit))
print("adres ip: "+str(format(ip_bit,'032b')))
mask_bit=int("1"*int(mask)+"0"*(32-int(mask)),2)
print("adres maski: "+str(format(mask_bit,'032b')))
adres_sieci=ip_bit & mask_bit
print("adres sieci: "+ str(format(adres_sieci,'032b')))


adres_broadcast=adres_sieci | (~mask_bit & 0xFFFFFFFF)
print("adres broadcast: "+str(format(adres_broadcast,'032b')))
host_count=pow(2,32-int(mask))-2
print("Host count: "+str(host_count))


pierwszy_host=adres_sieci+1
print("pierwszy host: "+str(format(pierwszy_host,'032b')))


ostani_host=adres_broadcast-1
print("ostatni host: "+str(format(ostani_host,'032b')))