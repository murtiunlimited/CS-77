def signmag_to_twoccomp(binary, bits=8):
    sign = binary[0]
    magnitude = int(binary[1:], 2)

    if sign == '0':
        return format(magnitude, f'0{bits}b')
    else:
        value = (1 << bits) - magnitude
        return format(value, f'0{bits}b')


def twoccomp_to_signmag(binary, bits=8):
    value = int(binary, 2)

    if binary[0] == '0':
        return binary 
    else:

        magnitude = (1 << bits) - value
        return '1' + format(magnitude, f'0{bits-1}b')


def convert(binary, mode, bits=8):
    if mode == "sm":
        return signmag_to_twoccomp(binary, bits)
    elif mode == "tc":
        return twoccomp_to_signmag(binary, bits)

print("Positive Number")
# +10 in signed magnitude
signed_positive = "00001010"   
print("Signed Magnitude:", signed_positive)
print("Two's Complement:", convert(signed_positive, "sm"))

print("\nNegative Number")
# -10 in signed magnitude
signed_negitive = "10001010"
print("Signed Magnitude:", signed_negitive)
print("Two's Complement:", convert(signed_negitive, "sm"))

print("\nNegative number back to SM")
# -10 in two's complement
twos_negitive = "11110110"   
print("Two's Complement:", twos_negitive)
print("Signed Magnitude:", convert(twos_negitive, "tc"))
