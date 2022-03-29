import math
a, b, c = 15, 24, 4

delta = math.pow(b, 2)-(4*a*c)
print(delta)

if delta < 0:
    print("Denklemin reel kökü yoktur!")

elif delta > 0:
    x1 = (-b + math.sqrt(delta))/2*a
    x2 = (-b - math.sqrt(delta))/2*a

    print("Denkelmin kökleri= " , x1 ,"ve", x2)


elif delta == 0:
    print("denklemin çift kökü vardır!")
    x1 = -b/2*a
    print("x1 ve x2 = ", x1)

    
