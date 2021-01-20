# int -> str
#
def convert(num, b, base_num=''):
    """Recursive function that returns a string representing num in the base b"""
    quotient = num // b
    remainder = round(((num / b) - quotient) * b)  # (quotient and remainder as a decimal minus quotient) times the
    # base to get a whole number
    if remainder > 9:
        if remainder == 10:
            base_num += 'A'
        elif remainder == 11:
            base_num += 'B'
        elif remainder == 12:
            base_num += 'C'
        elif remainder == 13:
            base_num += 'D'
        elif remainder == 14:
            base_num += 'E'
        elif remainder == 15:
            base_num += 'F'
    else:
        base_num += str(remainder)

    if quotient == 0:
        rev_base = ''
        while len(base_num) > 0:        # reverses string
            rev_base += base_num[-1]
            base_num = base_num[:-1]
        return rev_base
    else:
        return convert(quotient, b, base_num)