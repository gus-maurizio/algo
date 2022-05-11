import sys
s = sys.argv[1] if len(sys.argv) > 1 else '0123'
b = s.encode('utf-8')
value = int.from_bytes(b, sys.byteorder) 
digit = value & (value + 0x06060606) & 0xF0F0F0F0 == 0x30303030 
digsi = value & 0xF0F0F0F0 == 0x30303030
print(s,f'{b}',value,digit,digsi)