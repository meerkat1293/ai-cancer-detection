def every_third_equal(some_string):
    comp_string = some_string[2]
    new_string = some_string[2:]
    for r in new_string[::3]:
        if comp_string != r:
            return False
    return True

