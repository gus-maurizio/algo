
# a packed decimal has 0-9 in each half byte, cannot have a-f anywhere
# 1000 8 1001 9 1__0/1 no bits 2 or 3 set if bit 1 is set
# 0xE is 1110b
k = 16*9
for i in range(k,k+32):
    packed      = (i & 0x08 == 0) or (i & 0x06 == 0)
    notpacked   = (i & 0x88 and i & 0x66) == 0
    print(f'{i:02d} {i:02x} {packed} {notpacked}')