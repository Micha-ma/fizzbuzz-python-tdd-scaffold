def fizzBuzz(value):
    if value % 15 == 0:
        return "fizzbuzz"
    elif value % 3 == 0:
        return "fizz"
    elif value % 5 == 0:
        return "buzz"
    return str(value)
