# Python program to find Area of a circle

def findArea(r):
    PI = 3.142
    return PI * (r * r);

# Driver method INPUT AND OUTPUT
r=int(input("Enter radius of the circle : "))
print ("Area is %.6f" % findArea (r));

