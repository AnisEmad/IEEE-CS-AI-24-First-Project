import re
def handleString(string):
    """ 
    asks for input while the input is not string
    return string
    """
    words = string.split()
    for word in words:
        if not word.isalpha():
            string = input("Input must be string with no digits in it, Try again: ")
            return handleString(string)
    return string    
def handleInt(number):
    """
    asks for input while the input is not an intger
    return int
    """
    try:
        decimal_number = float(number)
        number = int(number)
        if number != decimal_number:
            raise TypeError
    except:
        number = input("Input must be a poistive intger, Try again: ")
        number = handleInt(number)
    return number
def handleSignal(number):
    """ return poistive number """
    number = handleInt(number)
    while number <= 0:
        number = handleInt(input("Input must be a poistive intger, Try again: "))
    return number
def isEmail(email):
    """ verfiy it's in email form """
    email_pattern = re.compile(r'^[\w\.-]+@[\w\.-]+\.\w+$')
    return bool(re.match(email_pattern, email))

def handleEmail(email):
    while not isEmail(email):
        email = input("Input must be in email form\n")