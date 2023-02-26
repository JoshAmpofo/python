#!/usr/bin/env python3
"""Encoding and decoding strings and bytes"""

place = 'caf\u00e9'
print(place)
print(type(place))

# encode in utf-8
print('\n')
place_bytes = place.encode('utf-8')
print(place_bytes)
print(type(place_bytes))

# decode into ASCII
print('\n')
place2 = place_bytes.decode('utf-8')
print(f'UTF-8: {place2}')

# trying to decode into a different format
# print('\n')
# place3 = place_bytes.decode('ascii')
# print(f'ASCII: {place3}')

# decode to latin-1
print('\n')
place4 = place_bytes.decode('latin-1')
print(f'Latin-1: {place4}')

# decode into windows-1252
print('\n')
place5 = place_bytes.decode('windows-1252')
print(f'Windows-1252: {place5}')
