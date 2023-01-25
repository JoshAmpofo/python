short_list = [1, 2, 3]
position = 5
print(short_list[position])

# wrapping it in a try-except block
short_list = [1, 2, 3]
position = 5
try:
    short_list[position]
except IndexError:
    print("Need a position between 0 and", len(short_list)-1, "but got", position)
    
# STORING ERRORS IN NAME
short_list = [1, 2, 3]
while True:
    value = input('Position [q to quit]? ')
    if value == "q":
        break
    try:
        position = int(value)
        print(short_list[position])
    except IndexError as err:
        print("Bad Index:", position)
    except Exception as other:
        print("Something else broke:", other)
        
        
# HOW TO CREATE AN EXCEPTION 
class UppercaseException(Exception):
    pass

words = ['eenie', 'meenie', 'miny', 'MO']
for word in words:
    if word.isupper():
        raise UppercaseException(word)
    
    
# DEFINING EXCEPTION BEHAVIOUR AND RETRIEVING EXCEPTION OBJECT
class OopsException(Exception):
    pass

words = ['eenie', 'meenie', 'miny', 'MO']
for word in words:
    if word.isupper():
        try:
            raise OopsException('panic')
        except OopsException as exc:
            print(exc)
