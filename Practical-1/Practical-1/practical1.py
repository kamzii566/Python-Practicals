import cmath

a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))

D = b**2 - 4*a*c

root1 = (-b + cmath.sqrt(D)) / (2*a)
root2 = (-b - cmath.sqrt(D)) / (2*a)

print("Roots are:", root1, "and", root2)
