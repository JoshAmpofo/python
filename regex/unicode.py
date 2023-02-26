#!/usr/bin/env python3
"""unicode translation"""

def unicode_test(value):
    import unicodedata
    name = unicodedata.name(value)  #convert unicode to uppercase name 
    value2 = unicodedata.lookup(name)  # convert uppercase name to unicode
    print("value='%s', name='%s', value2='%s'" % (value, name, value2))

# unicode_test('A')
# unicode_test('$')
# unicode_test('\u00a2')
# unicode_test('\u2603')
# unicode_test('\u00e9')
