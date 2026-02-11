import math

def convert_to_simplified_float(number):
    if number == 0.0:
        return "0 00000 00000000"
    
    sign_bit = 0 if number >= 0 else 1
    absolute_value = abs(number)

    exponent = math.log2(absolute_value)
    exponent = math.floor(exponent)
    exponent = int(exponent)
    biased_exponent = exponent + 15

    normalized_value = absolute_value / (2 ** exponent)
    fractional_part = normalized_value - 1

    significand_bits = ""

    while len(significand_bits) < 8:
        fractional_part *= 2
        current_bit = int(fractional_part)
        significand_bits += str(current_bit)
        fractional_part -= current_bit

    return f"{sign_bit} {biased_exponent:05b} {significand_bits}"

# Examples
print("6.25  ->", convert_to_simplified_float(6.25))
print("-3.75 ->", convert_to_simplified_float(-3.75))
