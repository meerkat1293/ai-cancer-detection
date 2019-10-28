def max_length(string1,string2,string3):
    if len(string1) >= len(string2) and len(string1) >= len(string3):
        return len(string1)
    elif len(string2) > len(string3):
        return len(string2)
    else:
        return len(string3)

def interleave(string1,string2,string3):
    new_string = ''
    max_str_lngth = max_length(string1,string2,string3)
    string1 = string1 + ' ' * (max_str_lngth-len(string1))
    string2 = string2 + ' ' * (max_str_lngth-len(string2))
    string3 = string3 + ' ' * (max_str_lngth-len(string3))
    for i in range(max_str_lngth):
        new_string += string1[i]+string2[i]+string3[i]
    return new_string


print(interleave("xxx","yyy","zzz"))