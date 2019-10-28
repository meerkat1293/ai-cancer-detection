def is_even(num):
    return num % 2 == 0

def is_triangle(a,b,c):
    if a + b < c or a + c < b or b + c < a:
        return False
    return True

def try_triangle():
    len1 = int(input("Enter first length: "))
    len2 = int(input("Enter second length: "))
    len3 = int(input("Enter third length: "))
    return is_triangle(len1,len2,len3)


def has_consecutive(some_string):
    place_holder = ""
    for i in some_string:
        if i == place_holder:
            return True
        elif i != place_holder:
            place_holder = i
            continue
    return False


def ess(string1,string2):
    return str(len(string1))+" "+string1+string2

def dess(combined_string, num):
    point_index = int(combined_string[0])
    actual_string = combined_string[2:]
    if num == 1:
        return actual_string[:point_index]
    elif num == 2:
        return actual_string[point_index:]
    
    


def bitwise_or(string1,string2):
    if len(string1) != len(string2):
        return 'ERROR'
    return_value = ''
    for i in range(len(string1)):
        if string1[i] == '1' or string2[i] == '1':
            return_value += '1'
        else:
            return_value += '0'
    return return_value

def every_third_equal(some_string):
    comp_string = some_string[2]
    new_string = some_string[2:]
    for r in new_string[::3]:
        if comp_string != r:
            return False
    return True

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

