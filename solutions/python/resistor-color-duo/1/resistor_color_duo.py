def value(colors):
    color_codes = { "black": 0, "brown": 1, "red": 2, "orange": 3, 
                    "yellow": 4, "green": 5,"blue":6, 
                    "violet": 7, "grey": 8, "white": 9 }
    new_values=[]
    for i in range(2):
        new_values.append(str(color_codes[colors[i]]))

    return int("".join(new_values))
