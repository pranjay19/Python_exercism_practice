def commands(binary_str):
    list_val=[]
    if binary_str[4]=="1":
        list_val.append("wink")
    if binary_str[3]=="1":
        list_val.append("double blink")
    if binary_str[2]=="1":
        list_val.append("close your eyes")
    if binary_str[1]=="1":
        list_val.append("jump")
    if binary_str[0]=="1":
        list_val.reverse()  

    return list_val

    

    
        
            
        
        
