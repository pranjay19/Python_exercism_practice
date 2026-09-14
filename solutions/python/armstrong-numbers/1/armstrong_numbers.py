def is_armstrong_number(number):

    list=str(number)

    count=len(list)

    sum=0

    for i in list:
        sum=sum+int(i)**count

    if sum==number:
        return True

    else:
        return False
