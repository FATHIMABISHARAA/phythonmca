#lambda
a=int(input("enter the sides of the square \n"))
area=lambda b:b*b
print("area of sqare",area(a))

a=int(input("enter the length of the triangle\n"))
b=int(input("enter the breadth of the triangle \n"))
area=lambda h,b:0.5*h*b
print("area of the triangle is",area(a,b))

a=int(input("enter the height of the rectangle\n"))
b=int(input("enter the breadth of the rectangle \n"))
area=lambda l,b:l*b
print("area of the rectangle is",area(a,b))
