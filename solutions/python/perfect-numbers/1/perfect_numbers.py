def classify(number):

    if number <= 0:
        raise ValueError("Classification is only possible for positive integers.")

    val = []

    for i in range(1, number):
        if number % i == 0:
            val.append(i)

    final = sum(val)

    if final == number:
        return "perfect"
    elif final < number:
        return "deficient"
    else:
        return "abundant"