import math

def score(x, y):
    
    distance=math.sqrt((x*x)+(y*y))

    if distance>10:
        return 0
    elif distance > 5 and distance <= 10:
        return 1
    elif distance > 1 and distance <= 5:
        return 5
    else:
        return 10
        