lst = [hex(i) for i in range(5)]
print(*lst)
lst.remove('0x0')
print(*lst)