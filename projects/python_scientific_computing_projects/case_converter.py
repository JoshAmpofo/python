"""
Project 4: Build a Case Converter using List Comprehensions
"""


### APPROACH ONE: USING LOOPS
def convert_to_snake_case(pascal_or_camel_cased_string: str) -> str:
    """
    Convert an input text string (either in PasCal or Camelcase) to snake_case

    Args:
        pascal_or_camel_cased_string (str): target string to convert

    Returns:
        str: string formatted to snake_case
    """
    # create empty list to hold snake_case strings
    snake_cased_char_list = []
    
    # iterate through each character in function arg
    for char in pascal_or_camel_cased_string:
        # check if char is uppercase
        if char.isupper():
            # convert character to lowercase
            converted_character = '_' + char.lower()
            # append converted char to list
            snake_cased_char_list.append(converted_character)
        else:
            # if char is lowercase
            snake_cased_char_list.append(char)
    
    # add chars into string
    snake_cased_string = ''.join(snake_cased_char_list)
    # remove underscore appended to end of string
    clean_snake_cased_string = snake_cased_string.strip('_')
    
    # return snake_case
    return clean_snake_cased_string
    


### APPROACH TWO: USING LIST COMPREHENSIONS
def convert_to_snake_case(pascal_or_camel_cased_string: str) -> str:
    snake_case_char_list = [
        '_' + char.lower() if char.isupper()
        else char
        for char in pascal_or_camel_cased_string
    ]
    return ''.join(snake_case_char_list).strip('_')


def main():
    input_string = input('Enter Pascal Case or Camel case string: ')
    print(convert_to_snake_case(input_string))


if __name__ == '__main__':
    main()