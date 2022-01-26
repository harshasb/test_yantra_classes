# # # # to check number is even or not
# # #
# # # number = 5
# # #
# # # if number % 2 == 0:
# # #     print(f'{number} is an even number')
# # # else:
# # #     print(f'{number} is an odd number')
# #
# # ## to check character is in lower case or not
# #
# # char_ = 'Q'
# #
# # if char_.islower():
# #     print(f'{char_} is in lower case')
# # else:
# #     if char_.isupper():
# #         print(f'{char_} is in upper case')
# #     else:
# #         print(f'{char_} is not a character')
# #
# # if 'a' <= char_ <= 'z':
# #     print(f'{char_} is in lower case')
# # else:
# #     if 'A' <= char_ <= 'Z':
# #         print(f'{char_} is in upper case')
# #     else:
# #         print(f'{char_} is not a character')
# # #
# # # ###############################################
# # #
# # # if char_.islower():
# # #     print(f'{char_} is in lower case')
# # # elif char_.isupper():
# # #     print(f'{char_} is in upper case')
# # # else:
# # #     print(f'{char_} is not a character')
# # #
# # #
# # # # to check iterable is empty or not
# # #
# # # a = []
# # # if bool(a):
# # #     print("it is not empty")
# # # else:
# # #     print("it is empty")
# # #
# # #     #or
# # #
# # # a = ()
# # # if a:
# # #     print("it is not empty")
# # # else:
# # #     print("it is empty")
# # #
# # #     #or
# # #
# # # a = 'hai'
# # # if len(a) > 0:
# # #     print("it is not empty")
# # # else:
# # #     print("it is empty")
# #
# # # to check if the given value is default or non-default value
# #
# # # a = ''
# # #
# # # if a:
# # #     print("it is non-default value")
# # # else:
# # #     print("it is default value")
# #
# # # to convert lowercase letter into uppercase and uppercase letter into lowercase letter
# #
# # letter = '2'
# #
# # if letter.islower():
# #     print(letter.upper())
# #
# # elif letter.isupper():
# #     print(letter.lower())
# #
# # else:
# #     print(f"{letter} is not a letter")
# #
# # ######or
# #
# # letter = "w"
# # if 'a' <= letter <= 'z':
# #     upper_case = letter.upper()
# #     print(upper_case)
# #
# # elif 'A' <= letter <= 'Z':
# #     lower_case = letter.lower()
# #     print(lower_case)
# #
# # else:
# #     print("it is not a letter")
# #
# # ##swapcase
# #
# # a = '1111'
# #
# # if a.lower() or a.upper():
# #     print(a.swapcase())
# #
# # else:
# #     print("it is not letter")
#
# # convert lower case to upper and vice versa using ASCII value
# char = '9'
#
# if 'a' <= char <= 'z':
#     print(chr(ord(char) - 32))
#
# elif 'A' <= char <= 'Z':
#     print(chr(ord(char) + 32))
#
# else:
#     print('it is not alphabet')


# check string starts with vowel
#
# string = 'pple'
#
# if string[0] in 'aeiouAEIOU':
#     print("string starts with vowel")
#
# else:
#     print("string does not start with vowel")
#
# # string ending with vowel
#
# string = 'pple'
#
# if string[-1] in 'aeiouAEIOU':
#     print("string ends with vowel")
#
# else:
#     print("string does not end with vowel")


# check string is palindrome or not
#
# string = 'kkk'
#
# if string == string[::-1]:
#     print(f"{string} string is palindrome")
#
# else:
#     print(f"{string} string is not a palindrome")
#
# # check string is palindrome or not irrespective of the case
#
# string = 'MalaYalam'
#
# a = string.lower()
#
# if a == a[::-1]:
#     print(f"{string} string is palindrome")
#
# else:
#     print(f"{string} string is not a palindrome")
#
# # to check an integer is palindrome or not
#
# int_ = 1223
#
# b = str(int_)
#
# if b == b[::-1]:
#     print(f"{int_} string is palindrome")
#
# else:
#     print(f"{int_} string is not a palindrome")

# to check if the iterable has even number of elements.

# ite_ = 'hai'
#
# if len(ite_) % 2 == 0:
#     print(f"{ite_} has even elements")
#
# else:
#     print(f'{ite_} doesnt have even number of elements')

# to check if the first digit in the number is even or not

# num_ = 6567
#
# eve_ = str(num_)
#
# if int(eve_[0]) % 2 == 0:
#     print(f"{num_} has even first digit")
#
# else:
#     print(f"{num_} does not start with even digit")

# find the greatest of three numbers

a = [2, 2, 0]

if a[1] < a[0] > a[2]:
    print(f"{a[0]} is the greatest number")

elif a[0] < a[1] > a[2]:
    print(f"{a[1]} is the greatest number")

else:
    print(f"{a[2]} is the greatest number")

max_num = max(a)

# to check if the entered character is vowel and if its vowel, return its ASCII value
letter = 'u'

if letter in "aeiouAEIOU":
    print(f"{letter} is vowel and its ASCII value:", dict([{letter, ord(letter)}]))

else:
    print(f"{letter} is not vowel")

char = 'O'
d = {}
if char.lower() in 'aeiou':
    #d[char] = ord(char)
    #d.update({char: ord(char)})
    d.setdefault(char, ord(char))
    
    print(d)
