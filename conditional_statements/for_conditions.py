# print numbers from 1 to 10
#
# for num in range(1, 11):
#     print(num)

# print 10 to 1

# for num in range(10, 0, -1):
#     print(num)

# print fron -1 to -10

# for num in range(-1, -11, -1):
#     print(num)

# print from -10 to -1
# for num in range(-10, 0):
#     print(num)

# print even numbers between 1 to 10
# for num in range(1, 11):
#     if num % 2 == 0:
#         print(num)

# print odd numbers
# for num in range(1,11):
#     if not num % 2 == 0:
#         print(num)

# traversing through string

s = 'Republic'
#
# for item in range(len(s)):
#     print(s[item], end=" ")

#OR

# for char in s:
#     print(char, end=" ")

# traverse through list

list1 = [4, 2, 3, 1, 5]

# for i in list1:
#     print(i)

#OR

# for j in range(len(list1)):
#     print(list1[j])

# traverse through tuple

#tuppy = (6, 5, 3, 4)
#
# for p in range(len(tuppy)):
#     print(tuppy[p])

#or
#
# for q in tuppy:
#     print(q)

# traverse through sets
#
# sets1 = {1, 'hai', 6, 8, 4, 2}
#
# for ele in sets1:
#     print(ele, end=" ")

#traversing through dictionaries

# dict1 = {'one': 1, 'two': 2, 'three': 3}
#
# for k in dict1:
#     print(k, dict1[k], sep=':')

# program to print index and element in a string

str1 = 'Republic'

# for ele in range(len(str1)):
#     print(ele, str1[ele], sep='->')

#unpacking list
# for item in enumerate(str1):
#     print(item)
#     print(item[0], item[1])

# for index, item in enumerate(str1):
#     print(index, item, sep="->")

#traverse through string in reverse order

# s1 = "Republic"
#
# for item in range(len(s1)-1, -1, -1):
#     print(s1[item], end=" ")
# print()
#
# #or
#
# for char in s1[::-1]:
#     print(char, end=' ')
# print()
#
# #or
#
# for ele in reversed(s1):
#     print(ele, end=" ")

#program to count the number of characters in a string

# s2 = "Republic"
#
# # count = 0
# # for _ in s2:
# #     count += 1
# # print(count)
#
# #print the even index characters
# for item in range(0, len(s2), 2):
#     print(s2[item], end=" ")
#
# print()
#
# for char in s2[::2]:
#     print(char, end=" ")

#print the digits present inside string

s = "hello 123 hai4%978"

# for char in s:
#     if '0' <= char <= '9':
#         print(char, end=" ")
#
#     # if char.isdigit():
#     #     print(char, end=" ")
count = 0
for ele in s:
    if ele.isdigit():
        count += 1
print(ele)




