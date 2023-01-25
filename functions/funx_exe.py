# Define a function called "good()" that returns the following list:
# ['Harry', 'Ron', 'Hermione']

def good():
    return ['Harry', 'Ron', "Hermione"]

print(good())

# Alternative method using lambda
good = lambda: ['Harry', 'Ron', 'Hermione']

print(good())

# Define a generator function called get_odds() that
# returns the odd numbers from range(10). Use a for loop
# to find and print the third value returned

def get_odds():
    for num in range(10): 
        if num % 2 == 1:
            yield num

# for num in get_odds():
    # print(num)  # print all values in generator function

gen_val = get_odds()
for index, value in enumerate(gen_val):
    if index == 2:  # check if position is third
        print(value)  # print value in third position


# Define a decorator called test that prints 'start' when a function is called
# and 'end' when it finishes

def test(func):
    def new_func(*args, **kwargs):
        print("start")
        result = func(*args, **kwargs)
        print('end')
        return result
    return new_func

@test
def my_function():
    print("doing something here")

my_function()


# Define an exception called OopsException. Raise this 
# exception to see what happens. Then, write the code to catch
# this exception and print 'Caught an oops'

# first part
class OopsException(Exception):
    pass

value = [1, 2, 3, 4, 5, 'boo']
for val in value:
    if not isinstance(val, int):
        raise OopsException(val)
    
# second part
class OopsException(Exception):
    pass

value = [1, 2, 3, 4, 5, 'boo']
for val in value:
    if not isinstance(val, int):
        try: 
            raise OopsException('Caught an oops')
        except OopsException as exc:
            print(exc)