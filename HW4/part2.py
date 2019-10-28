def is_triangle(a,b,c):
    if a + b < c or a + c < b or b + c < a:
        return False
    return True

def try_triangle():
    len1 = int(input("Enter first length: "))
    len2 = int(input("Enter second length: "))
    len3 = int(input("Enter third length: "))
    return is_triangle(len1,len2,len3)
