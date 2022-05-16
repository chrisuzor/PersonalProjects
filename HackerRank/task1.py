def romanizer(numbers):
    units = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
    tens = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
    hundreds = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM "]
    thousands = ["", "M", "MM", "MMM"]

    final_solution = []
    for num in numbers:

        unit = units[num % 10]
        print((num % 100) // 10)
        ten = tens[(num % 100) // 10]
        hundred = hundreds[(num % 1000) // 100]
        thousand = thousands[num // 1000]
        roman_value = f"{thousand}{hundred}{ten}{unit}"

        final_solution.append(roman_value)

    return final_solution


"\n".join(romanizer([1, 49, 23]))
