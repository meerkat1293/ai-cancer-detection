def is_triangle(a,b,c):
    if a + b > c or a + c > b or b + c > a:
        return True
    return False


print(is_triangle(12,1,1))
print(is_triangle(6,8,5))
print(is_triangle(6,8,15))