def steps(number):

    if number<=0:
        raise ValueError("Only positive integers are allowed")
    else:
        count=0
        if number==1:
            return count
        else:
            while number!=1:
                if number%2==0:
                    number=int(number/2)
                    count=count+1
                else:
                    number=(number*3)+1
                    count=count+1

    return count
                    
