def ess(string1,string2):
    return str(len(string1))+" "+string1+string2

def dess(combined_string, num):
    point_index = int(combined_string[0])
    actual_string = combined_string[2:]
    if num == 1:
        return actual_string[:point_index]
    elif num == 2:
        return actual_string[point_index:]
    
    


