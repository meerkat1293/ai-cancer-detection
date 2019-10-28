
def has_consecutive(some_string):
    place_holder = ""
    for i in some_string:
        if i == place_holder:
            return True
        elif i != place_holder:
            place_holder = i
            continue
    return False


