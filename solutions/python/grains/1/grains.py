def square(number):

    if number<1 or number>64:
        raise ValueError("square must be between 1 and 64")
        
    val=2**(number-1)
    return val


def total():

    val=0

    for i in range(1,65):
        val=val+square(i)

    return val
