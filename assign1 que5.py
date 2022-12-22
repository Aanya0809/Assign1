import math
print("Sine and cos series is as shown below\n")
for i in range(0,350,15):
     x=math.radians(i)
     y=math.sin(x)
     a=round(y,4)
     z=math.cos(x)
     b=round(z,4)
     print( i ,":", a,b)
