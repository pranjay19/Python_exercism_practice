
def is_valid(isbn):
    isbn = isbn.replace("-", "")

    if len(isbn) != 10:
        return False

    for i in isbn[:9]:
        if not i.isdigit():
            return False

    if not (isbn[-1].isdigit() or isbn[-1] == "X"):
        return False

    val = 0
    count = 10

    for i in isbn:
        if i == "X":
            val += 10 * count
        else:
            val += int(i) * count
        count -= 1

    return val % 11 == 0

