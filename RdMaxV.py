import math
rdtyp = int(input("1:banked  2:flat 3:frictionless"))
r=float(input("r in meters"))
theta =math.radians(int(input("theta")))
mew =  float(input("mew"))
if rdtyp ==1:
    output = math.sqrt(((math.sin(theta)+(math.cos(theta)*mew))*9.8*r)/(math.cos(theta)-(mew*math.sin(theta)))) 
if rdtyp ==2:
    output = math.sqrt(r*9.8*mew)
if rdtyp ==3:
    output = math.sqrt(r*9.8*math.tan(theta))

print(str(output)+" m/s")
print(str(output*2.2)+" mph")