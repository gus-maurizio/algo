import sys
s = sys.argv[1] if len(sys.argv) > 1 else 'a0123456789b'
for a in s:
    print(a,ord(a) & (ord(a)+0x06) & 0xF0 == 0x30)