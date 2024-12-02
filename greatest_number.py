# Program to read three numbers and find the biggest number. Let "n" is the biggest number, compute n+nn+nnn. Assume the same "n" is the radius of a circle and find its area and perimeter. Find the volume of a sphere with a redius"n".

num1=int(input("Enter first number :"))
num2=int(input("Enter second number :"))
num3=int(input("Enter third number :"))
if num1>num2 and num1>num3:
    n=num1
elif num2>num1 and num2>num3:
    n=num2
else:
    n=num3
print("The biggest number is:",n)

print("The sum of n, nn, nnn is:",n+(n**2)+(n**3))
print("The area of the circle is:",3.14*n**2)