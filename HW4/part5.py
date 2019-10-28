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

