
def label(colors):
    color_codes = {
        "black": 0,
        "brown": 1,
        "red": 2,
        "orange": 3,
        "yellow": 4,
        "green": 5,
        "blue": 6,
        "violet": 7,
        "grey": 8,
        "white": 9
    }

    # First two colors make the main number
    new_values = []

    for i in range(2):
        new_values.append(str(color_codes[colors[i]]))

    value = int("".join(new_values))

    # Third color tells us how many zeros to add
    zeros = color_codes[colors[2]]

    value = value * (10 ** zeros)

    # Choose the unit
    if value >= 1_000_000_000:
        value = value // 1_000_000_000
        return f"{value} gigaohms"

    elif value >= 1_000_000:
        value = value // 1_000_000
        return f"{value} megaohms"

    elif value >= 1_000:
        value = value // 1_000
        return f"{value} kiloohms"

    else:
        return f"{value} ohms"

