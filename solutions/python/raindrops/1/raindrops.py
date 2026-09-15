def convert(number):
    val=""
    if number%3==0:
        val+="Pling"
        
    if number%5==0:
        val+="Plang"
        
    if number%7==0:
        val+="Plong"
        
    if number%3!=0 and number%5!=0 and number%7!=0:
        val+=str(number)

    return val
        