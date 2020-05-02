import os
import itertools
import string

# Get the input from the user
user_input = input('Format of the number plate: ')

# String of the alphabet can be used by string.ascii_lowercase or string.ascii_uppercase

# Check the format of the input

# Defining different cases
# Cases can be found https://en.wikipedia.org/wiki/Vehicle_registration_plates_of_South_Africa
wcp = 'Cab #'
knp = 'Nab #'
mp = 'aaa+++ MP'
ec = 'aaa+++ EC'
lp = 'aaa+++ L'
gp = 'aaa+++ GP'
gp2 = 'aa++aa GP'
ncp = 'aaa+++ NC'
fsp = 'aaa+++ FS'
nwp = 'aaa+++ NW'
ngv = 'Gaa+++ G'
pv = 'Baa+++ B'
mv = 'aaa+++ M'

# Use cases of formats
f1 = 'aaa+++'
f2 = 'aa++aa'
f3 = 'Gaa+++'
f4 = 'Baa+++'

# Key:
# UPPER CASE LETTERS: Literal letters in the number plate
# a: compulsory letter (A - Z)
a_string = string.ascii_uppercase
a_list = list(a_string)
# b: letter (A - Z) or nothing
b_string = a_string
b_list = list(b_string)
b_list.append(' ')
# #: an integer number (1 - 999,999)
hash = []
for i in range(999999):
    hash.append(i)
# +: a compulsory digit (0 - 9)
plus_string = ''
for i in range(10):
    plus_string += str(i)
print(plus_string)
plus_list = list(plus_string)
# x: compulsory character (A - Z, 0 - 9)
x_string = a_string + plus_string
x_list = list(x_string)
# z: character (A - Z, 0 - 9) or nothing
z_string = a_string + plus_string
z_list = list(z_string)
z_list.append(' ')
# NB:Vowels are not used on private vehicles.

a = 'a'
b = 'b'
plus = '+'
x = 'x'
z = 'z'

# Check what input it matches
# Seperate the province from the string, we only need the first 6 digits
lists = []
province = ''
Government = ''
g = False
for i in range(len(user_input)):
    character = user_input[i]
    print(character)
    if (character is not None):
        if character.isupper():
            if character == 'G' or character == 'B':
                g = True
        if character == a:
            lists.append(a_list)
        if character == plus:
            lists.append(plus_list)
        if character == b:
            lists.append(b_list)
        if character == x:
            lists.append(x_list)
        if character == z:
            lists.append(z_list)
        
        print(f'lists: {lists}')
    
# Result
result = list(itertools.product(*lists))
for i in range(0, len(result)):
    print(f'{i}: ' + ''.join(result[i]))
