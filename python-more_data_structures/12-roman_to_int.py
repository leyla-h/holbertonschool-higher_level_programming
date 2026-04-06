for i in range(len(roman_string)):
    if i + 1 < len(roman_string) and rom_n[roman_string[i]] < rom_n[roman_string[i+1]]:
        res -= rom_n[roman_string[i]]
    else:
        res += rom_n[roman_string[i]]
