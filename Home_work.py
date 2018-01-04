import math

a = 10
b = 20
c = 30

#1.	Найти результат выражения для произвольных значений a,b,c: a + b * (c / 2)

d = a + b * (c / 2)

print("Задание 1")
print("При a = %d, b = %d, c = %d d равно: %d" % (a, b, c, d))
print("--------------------------------------------")

#2.	Найти результат выражения для произвольных значений a,b: (a2 + b2) % 2

e = (a**2 + b**2) % 2

print("Задание 2")
print("При a = %d, b = %d e равно: %d" % (a, b, e))
print("--------------------------------------------")

#3.	Найти результат выражения для произвольных значений a,b,c: ( a + b ) / 12 * c % 4 + b

f = (a + b) / 12 * c % 4 + b
print("Задание 3")
print("При a = %d, b = %d , c = %d f равно: %d" % (a, b, c, f))
print("--------------------------------------------")

#4. Найти результат выражения для произвольных значений a,b,c: (a - b * c ) / ( a + b ) % c

g = (a - b * c) / (a + b) % c
print("Задание 4")
print("При a = %d, b = %d, c = %d g равно: %0.2f" % (a, b, c, g))
print("--------------------------------------------")

#5.	Найти результат выражения для произвольных значений a,b,c: | a - b | /( a + b)3 - cos( c )

h = abs(a - b) / (a + b)**3 - math.cos(c)
print("Задание 5")
print("При a = %d, b = %d, c = %d h равно: %0.3f" % (a, b, c, h))
print("--------------------------------------------")

#6.	Найти результат выражения для произвольных значений a,b,c: ( ln( 1 + c ) / -b )4+ | a |

f = (math.log(1 + c) / -b)**4 + abs(a)
print("Задание 6")
print("При a = %d, b = %d, c = %d f равно: %0.6f" % (a, b, c, f))
print("--------------------------------------------")

#7.	Преобразовать строку с американским форматом даты в европейский. Например, "05.17.2016" преобразуется в "17.05.2016"
                      #0123456789
american_date_style = "05.17.2016"

print("Задание 7")
print("american_date_style is:")
print("05.17.2016")
print("european_date_style is: ")
european_date_style = american_date_style [3:6] + american_date_style [0:3] + american_date_style [6:100]
print(european_date_style)

# Еще один вариант кода:

current_date = "05.17.2016"
data_1st = current_date.split('.')
months = int(data_1st[0])
days = int(data_1st[1])
years = int(data_1st[2])
print("%d.%d.%d" % (days, months, years))
print("%s.%s.%s" % (data_1st[1], data_1st[0], data_1st[2]))
print("--------------------------------------------")

#8.	Дана строка с именем студента, в которой имя предшествует фамилии, например
# ‘Mark Zuckerberg‘. Написать программу, которая преобразует эту строку, ставя
# фамилию на первое место, а имя на второе. Т.е. ‘Mark Zuckerberg‘ -> ‘Zuckerberg Mark‘.

name_surname = "Mark Zuckerberg"
data_1st = name_surname.split(" ")
name = data_1st[0]
surname = data_1st[1]
print("Задание 8")
print("%s %s" % (surname, name))
print("--------------------------------------------")

#9.	Написать программу, которая преобразует имя переменной в формате snake_style
# в формат CamelizedStyle. Для простоты считаем, что имя переменной всегда состоит
# из 3-х слов. Например: ‘employee_first_name’ -> ‘EmployeeFirstName’

print("Задание 9")
snake_style_name = "employee_first_name"
split1 = snake_style_name.split("_")
camelized_style_name = split1[0].capitalize() + split1[1].capitalize() + split1[2].capitalize()
print("Snake_style: %s" % snake_style_name)
print("CamelizedStyle: %s" % camelized_style_name)
print("--------------------------------------------")

#10.Дана строка вида 'Leo Tolstoy*1828-08-28*1910-11-20'. В этой строке указаны имя
# писателя и через символ * даты рождения и смерти. Даты указаны в формате "YYYY-MM-DD".
#  Требуется написать программу, которая по переданной строке определит возраст писателя
#  и распечает его имя и возраст. Например, для строки 'Leo Tolstoy*1828-08-28*1910-11-20'
#  программа должна распечает: 'Leo Tolstoy, 82'. Для строки 'Marcus Aurelius*121-04-
# 26*180-03-17' - 'Marcus Aurelius, 59'.

print("Задание 10")
writer = "Alexander Pushkin*06-06-1799*10-02-1837"

split2 = writer.split("*")
dates = split2[1].split("-") + split2[2].split("-")
years_old = int(dates[5]) - int(dates[2])
name_years = split2[0] + " - " + str(years_old)

print("Имя и возраст писателя: % s" %(name_years))

painter = "Leonardo da Vinchi*1452-15-04*1519-02-05"
info_split = painter.split("*")
life_dates = info_split[1].split("-") + info_split[2].split("-")
year_old = int(life_dates[3]) - int(life_dates[0])
name_year = info_split[0] + " - " + str(year_old)
print("Имя и возраст художника: %s" % (name_year))
print("--------------------------------------------")

#11.Написать функцию, которая будет переводить градусы в радианы.
# Используя эту функцию вывести на экран значения косинусов углов в 60, 45 и 40 градусов.

print("Задание 11")
def degrees2radians(degrees):
    return float((degrees * math.pi) / 180)
print(degrees2radians(60))
print(degrees2radians(45))
print(degrees2radians(40))


#13.Пользователь вводит длины катетов прямоугольного треугольника.
# Написать функцию, которая вычислит площадь треугольника и его периметр.
# Результат работы функции вывести на печать.

print("Задание 13")
def triangle_square_and_perimeter(a, b):
    return float((a * b) / 2) # Triangle square
    return float(math.sqrt((a**2 + b**2))) # Hypotenuse
    return float(a + b + c) # Triangle_perimeter
print(triangle_square_and_perimeter(3, 2))
print("--------------------------------------------")

#14.Написать функцию, которая будет проверять четность некоторого числа.

print("Задание 14")
def is_even(number):
    return number % 2 == 0
print(is_even(3))
print("--------------------------------------------")









