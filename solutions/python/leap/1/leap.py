def leap_year(year):

    val=False

    if year%4==0 and year%100!=0 or year%400==0:
        val=True
    else:
        val=False

    return val
        
