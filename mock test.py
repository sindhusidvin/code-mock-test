# Implement palindrome using iterator(for loop) and generator mechanism.

user_inp = int(input("Enter a number: "))
def seperating_digit(num):
    while num > 0:
        rem = num % 10
        num = num // 10
        yield rem


def reverse_num(user):
    reverse_digit = 0
    for i in seperating_digit(user):
        reverse_digit = (reverse_digit * 10) + i
    return reverse_digit


if user_inp == reverse_num(user_inp):
    print("the no is palindrome!")
else:
    print(" this is not a palindrome no.!")

# =======================================================================================================================================================================================

# print("""2. Sum of 2 digits into output
# n1 = 1234 # int(input("Enter number1 :" ))
# n2 = 9999 # int(input("Enter number2 :" ))
# Output: 9+1 2+9 3+9 4+9
# 10 + 11 + 12 + 13 = 46""")

def seperating_digit(num):
    while num > 0:
        rem = num % 10
        num = num // 10
        yield rem

print()
n1 = int(input("Enter the first numbers: "))
n2 = int(input("Enter the first numbers: "))

list_n1 = [i for i in seperating_digit(n1)]
list_n2 = [i for i in seperating_digit(n2)]

list_n1.sort()
list_n2.sort()

total = []

for no_1, no_2 in zip(list_n1, list_n2):
    print(f" {no_1} + {no_2}", end=",")
    total.append(no_1 + no_2)

print()
for i in total:
    if i == total[-1]:
        print(i)
    else:
        print(f" {i} +", end="  ")

print(f"{sum(total)}")
# ============================================================================================================================================================================

# print("""3. st = "ab@#cd!ef"
#    Reverse string considering only alphabets. Symbols should not be reversed
#    # Output: fe@#dc!ba""")

st = "ab@#cd!ef"


# convert string into list
listSample = list(st)

i = 0
j = len(listSample) - 1

while i < j:
    if not listSample[i].isalpha():
        i += 1
    elif not listSample[j].isalpha():
        j -= 1
    else:
        # swap the element in the list
        # if both elements are alphabets
        listSample[i], listSample[j] = listSample[j], listSample[i]
        i += 1
        j -= 1

# convert list into string
# by concatinating each element in the list
strOut = ''.join(listSample)
print(strOut)

# =============================================================================================================================================================================
some_list = ["a", "b", "c", "d", "n", "a", "b", "m", "n", "m"]
# # # find out elements duplicate count output in  dict format

some_list.remove("c")
some_list.remove("d")
print(some_list)
from collections import Counter
x = Counter(some_list)
print(x)

# ============================================================================================================================================================================
t1 = (1, 2, 3, "a", "c")
t2 = ("b", "d", 9, 8, 7)


def sort_ele_of_diff_types_t1(inp):
    strs = list(filter(lambda x: type(x) == str, inp))
    ints = list(filter(lambda x: type(x) == int, inp))

    output = sorted(ints) + sorted(strs)
    return output


def sort_ele_of_diff_types(inp):
    strs = list(filter(lambda x: type(x) == str, inp))
    ints = list(filter(lambda x: type(x) == int, inp))

    output = sorted(ints, reverse=True) + sorted(strs)
    return output


list_of_t1 = sort_ele_of_diff_types_t1(t1)
list_of_t2 = sort_ele_of_diff_types(t2)

for t_1, t_2 in zip(list_of_t1, list_of_t2):
    print(t_1 + t_2)

# =====================================================================================================================================================================================
# Write a Python program to remove leading zeros from an IP address.
# 			  inp = "216.08.094.196"
			# o/p =  216.8.94.196
ip = '216.08.094.196'
print(ip.replace('0', ''))

# ============================================================================================================================================================================
# l = [1, 2, [3, 4, [5, 6]], 7, 8, [9, [10]]]
# output= [1,2,3,4,5,6,7,8,9,10]

l = [1, 2, [3, 4, [5, 6]], 7, 8, [9, [10]]]

# output list
output = []


# function used for removing nested
# lists in python using recursion
def removeNestings(l):
    for i in l:
        if type(i) == list:
            removeNestings(i)
        else:
            output.append(i)


# Driver code
print('The original list: ', l)
removeNestings(l)
print('The list after removing nesting: ', output)

# ===========================================================================================================================================================================
# Load sample content in text file.
#    Read data and find
#     1. No of lines in file
# 	2. No of words in each line
# 	3. No of chars in each line
# 	4. No of vowels and consonants
# 	5. No of special chars linewise and total

with open("sample.txt", "r") as file:
    file_content = file.read()
    print("the no. of lines in file is ",  len(file_content.split("\n")))
    words_count = 0
    chars_count = 0
    vowels = 0
    consonant = 0
    for i in file_content.split("\n"):
        for j in i.split(" "):
            if not j.isalpha() and not j.isalnum():
                continue
            else:
                words_count += 1

        for j in i:
            if not j.isalpha() and not j.isalnum():
                continue
            else:
                chars_count += 1

        for j in i:
            if j.lower() in "aeiou":
                vowels += 1
            else:
                consonant += 1

    print("the total words in file is ", words_count)
    print("the total words in file is ", chars_count)
    print("the total vowels in file is ", vowels)
    print("the total consonant in file is ", consonant)

