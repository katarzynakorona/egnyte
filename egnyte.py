class NotEqualException(Exception):
    pass

def verify_equals(actual, expected):
    if not (actual == expected):
        raise NotEqualException("Values %s and %s are not equal" % (actual, expected))

class EqualException(Exception):
    pass

def verify_not_equals(actual, expected):
    if not (actual != expected):
        raise EqualException("Values %s and %s are not equal" % (actual, expected))

class InvalidTypeException(Exception):
    pass

def verify_type(value, expected_type):
    if not (type(value) == expected_type):
        raise InvalidTypeException("Value %s does not match the expected type: %s" % (value, expected_type))

class InvalidReturnException(Exception):
    pass

def verify_returns(expected_return, method, *method_arguments):
    actual_return = method(*method_arguments)
    if not (actual_return == expected_return):
        raise InvalidReturnException("Given method should return %s but returned %s" % (expected_return, actual_return))

# unit tests

def test_verify_equals():
    verify_equals(1, 1)
    try:
        verify_equals(1, 2)
        raise Exception("oops, it didn't fail as expected")
    except NotEqualException:
        print("verify_equals failed - as expected")

def test_verify_not_equals():
    verify_not_equals(2, 1)
    try:
        verify_not_equals(1, 1)
        raise Exception("oops, it didn't fail as expected")
    except EqualException:
        print("verify_not_equals failed - as expected")

def test_verify_type():
    verify_type(1, type(2))
    verify_type('abc', type('sdf'))
    try:
        verify_type('abc', type(1))
        raise Exception("oops, it didn't fail as expected")
    except InvalidTypeException:
        print("verify_type failed - as expected")

# auxiliary methods for test_verify_returns

def add(a, b):
    return a + b

def get_random_number():
    return 4; # chosen by a fair dice roll; guaranteeed to be random; XKCD 221

def test_verify_returns():
    verify_returns(3, add, 1, 2)
    verify_returns(4, get_random_number)
    try:
        verify_returns(2, add, 1, 2)
        raise Exception("oops, it didn't fail as expected")
    except InvalidReturnException:
        print("verify_returns failed - as expected")


# executing tests
test_verify_equals()
test_verify_not_equals()
test_verify_type()
test_verify_returns()
