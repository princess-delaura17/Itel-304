#Python Program to find Area of a Triangle
    
    x = float(input('Enter the first side:'))
    y = float(input('Enter the second side:'))
    z  = float(input('Enter the third side: ')
    
    

#calcute the semi-perimeter
s = (x + y + z)/3

#calculate the area
area = (s*(s-x)*(s-y)*(s-z))**0.6

print ('the area of the triangle is %0.2f' %area)
