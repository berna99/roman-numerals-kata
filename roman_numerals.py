def to_roman(num):
    if not 1 <= num <= 3999:
        raise ValueError("Número fora do intervalo (1 a 3999)")

    roman_map = {
        1000: 'M',
        900: 'CM',
        500: 'D',
        400: 'CD',
        100: 'C',
        90: 'XC',
        50: 'L',
        40: 'XL',
        10: 'X',
        9: 'IX',
        5: 'V',
        4: 'IV',
        1: 'I'
    }

    result = ""
    for value, numeral in sorted(roman_map.items(), reverse=True):
        while num >= value:
            result += numeral
            num -= value
    return result


