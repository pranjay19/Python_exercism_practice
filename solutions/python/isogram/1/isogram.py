def is_isogram(phrase):

    for i in phrase.lower():

        if i == " " or i == "-":
            continue
        
        count=0
        for j in phrase.lower():
            if i==j:
                count+=1
            else:
                continue 

        if count>1:
            return False
        else:
            continue  

    return True
        
                
