from fizzbuzz import fizzBuzz


def checkFizzBuzz(value, expectedVal):
    retVal = fizzBuzz(value)
    assert retVal == expectedVal


def test_fizzBuzzRtnNum():
    checkFizzBuzz(1, "1")


def test_fizzBuzzRtnFizz():
    checkFizzBuzz(3, "fizz")


def test_fizzBuzzRtnBuzz():
    checkFizzBuzz(5, "buzz")


def test_fizzBuzzRtnFizzBuzz():
    checkFizzBuzz(15, "fizzbuzz")
