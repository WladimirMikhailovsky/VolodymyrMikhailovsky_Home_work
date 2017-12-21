import math

# Calculate square of rectangle
#------------------------------------------------------------------------------------------------------

width = 10
height = 25
rectangle_square = width + height
print("Площадь прямоугольника при высоте", height, "и ширине", width, " равна:",rectangle_square)
print("Площадь прямоугольника при высоте %d и ширине %d равна: %d" % (height, width, rectangle_square))

# Calculate hypotenuse
#------------------------------------------------------------------------------------------------------
catheter1 = 4
catheter2 = 4
hypotenuse = math.sqrt(catheter1**2 + catheter2**2)
print"Гипотенуза при катете1 = %d см. и катете2 = %d см. равна: %3.f см." %(catheter1, catheter2, hypotenuse))

# Calculate circle_square
#------------------------------------------------------------------------------------------------------
radius = 10
circle_square = radius**2 * math.pi
print("Площадь круга при радиусе = %d см. равна: %.3f кв.см." % (radius, circle_square))