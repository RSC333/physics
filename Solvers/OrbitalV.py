import math
cmass = int(input("1:Orbit Earth  2:Orbit other"))
if cmass ==1:
    mode = int(input("1:Distance from Center  2:Distance from Surface"))

    if mode == 1:
        dfc = int(input("Distance from Center"))
        output = math.sqrt((398866000000)/dfc)
    
    if mode == 2:
        dfs = int(input("Distance from Surface"))
        r=int(dfs+6370)
        output = math.sqrt((398866000000)/r)
    
if cmass ==2:
    mode = int(input("1:Distance from Center  2:Distance from Surface"))
    mass = int(input("mass of central object in kg"))
    if mode == 1:
        dfc = int(input("Distance from Center"))
        output = math.sqrt((0.0000000000667)*mass/dfc)
    
    if mode == 2:
        dfs = int(input("Distance from Surface"))
        rad = int(input("radius of cen-obj"))
        r=int(dfs+rad)
        output = math.sqrt((0.0000000000667)*mass/r)
    
print(str(output)+" m/s")
print(str(output/1000)+" km/s")