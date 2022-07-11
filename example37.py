def ipv4_address(address):
    try:
        if address.count('.') != 4:
            return False
        return address.split('.') == list(map(str, list(map(int, address.split('.'))))) and \
                list(filter(lambda x: 0 <= x <= 255, list(map(int, address.split('.'))))) == list(map(int, address.split('.')))
    except:
        return False
    #return list(filter(lambda x: 0 <= x <= 255, list(map(int, address.split('.'))))) == list(map(int, address.split('.'))) and


print(ipv4_address('..255.255'))
# string = '12.12.12.10'
# arr = [12, 12, 12, 10]
# print(string.split('.'))
# fact = list(map(str, arr)) == string.split('.')
# print(fact)
