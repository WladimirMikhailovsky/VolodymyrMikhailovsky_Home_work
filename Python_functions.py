def power (base, exp):
    print ("power func")
    return base**exp

result1 = power(3, 2)
print(result1)

def rectangle_square(width, height):
    result2 = width * height
    return result2

result2 = rectangle_square(10, 20)
print(result2)



def print_delimeter(symbol = "+", num_repeat = 40):
    print(symbol*num_repeat)

def pretty_print (value):
    print_delimeter()
    print ("Value:",value)
    print_delimeter("~",45)

def calculate_sum_and_product (a,b):
    sum_result = a + b
    product_result = a + b
    return sum_result, product_result

result4, result5 = calculate_sum_and_product (2,3)
pretty_print(result4)
pretty_print(result5)



def rectangle_square(widht, height):
    result = widht * height
    return result

result2 = rectangle_square(10, 20)
pretty_print(result2)

my_pi = 3.14

def pretty_print (value):
    print("---------------------")
    print("Value:", value)
    print("---------------------")

def circle_square (radius):
    result = radius**2 + my_pi
    return result

result3 =circle_square(10)
pretty_print(result3)

#=============================================
#Пример перевода Цельсий2Фаренгейт:

def faren2celc (degrees):
    return (degrees - 32) / 1.8

def celc2faren (degrees):
    return degrees * 1.8 + 32
print(celc2faren(36.7))
print(faren2celc (97.88))






