#Fizzbuzz 2

def fizzbuzz(x):
    if x % 3 == 0 and x % 5 == 0:
        return "FizzBuzz"
    elif x % 3 == 0 and x % 5 != 0:
        return "Fizz"
    elif x % 3 != 0 and x % 5 == 0:
        return "Buzz"
    else:
        return x