def wha(txt):
    outhash = 0
    mask = 0x3FFFFFFF
    for c in txt:
        b = ord(c)
        val =  ((b ^ 0xCC) << 24)
        val |= ((b ^ 0x33) << 16)
        val |= ((b ^ 0xAA) << 8)
        val |= (b ^ 0x55)
        outhash = (outhash & mask) + (val & mask)
    return outhash

fi = open("3.2_input_string.txt", "r")
txt = fi.readline().strip()
fi.close()

print(hex(wha(txt)))
