#to defang an ip address, replace every. to [.]
#the function we gonna use is split() and join
def ip_address(address):
    new_address = ""
    #so we first split whatever the address from the user
    split_address = address.split(".")
   # print(split_address) ["1","10","1","8"],and then we join it
    new_address = "[.]".join(split_address)
    return new_address

ipaddress = ip_address(input("type in your ip address: "))
print(ipaddress)