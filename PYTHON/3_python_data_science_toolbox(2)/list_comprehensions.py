#%%
# Populate a list with a for loop, add 1 to a list of number
nums = [12,8,21,3,16]

# create a new empty list
added_nums = []
# use for loop to add 1
for i in nums:
    added_nums.append(i + 1)


print(type(nums))
print(added_nums)


# %%
# Using list comprehension for 1 line code
new_nums = [num + 1 for num in nums]
print(new_nums)

# %%
#NESTED LOOP

pair_1 = []
for num1 in range(0, 2):
    for num2 in range(6, 8):
        pair_1.append((num1, num2))

print(pair_1)


# %%
# use list comprehension 
pairs_2 = [(num1,num2) for num1 in range(0,2) for num2 in range(6,8)]
print(pairs_2)


# %%
# Write a basic list comprehension
doctor = ['house', 'cuddy', 'chase', 'thirteen', 'wilson']

# produce a list of the first character of each string

first_letter = [doc[0] for doc in doctor]
print(first_letter)
# %%
list = []
for doc in doctor:
    list.append(doc[0])
print(list)


# %%
# write a list comprehension that produces a list of the squares
# of the numbers ranging from 0 to 9

squares_list = [i **2 for i in range(0,10)]
print(squares_list)


# %%
# writing a list comprehesion within another list comprehension (nested list)

matrix = [[0, 1, 2, 3, 4],
          [0, 1, 2, 3, 4],
          [0, 1, 2, 3, 4],
          [0, 1, 2, 3, 4],
          [0, 1, 2, 3, 4]]

# recreate this matrix by using nested listed comprehensions.
# supply the list comprehension as the output expression of the overall list comprehension:
# [[output expression] for iterator variable in iterable]
# output expression is the first list comprehension

matrix_list = [[col for col in range(5)] for row in range(5) ]

for row in matrix:
    print(row)
print(matrix_list)
print(matrix)



# %%
# CONDITIONALS IN COMPREHENSIONS

# square values only divided by 2
divided2 = [i ** 2 for i in range(10) if i % 2 == 0]
print(divided2)
# %%
# use if else in conditionals comprehensions

divided20 = [i ** 2 if i % 2 == 0 else 0 for i in range(10)]
print(divided20)
# put if else before for


# %%
# create dictionaries comprehensions
# create postive and negative dic number

pos_neg = {num: -num for num in range(10)}

print(pos_neg)


# %%
# Create a list of strings: fellowship
fellowship = ['frodo', 'samwise', 'merry', 'aragorn', 'legolas', 'boromir', 'gimli']

# create a list of members of fellowships with only 7 length or more

new_fellowship = [mem for mem in fellowship if len(mem) >= 7]
print(new_fellowship)
# %%
# same above conditions with replace other with empty string

new_fellowship1 = [mem if len(mem) >= 7 else "" for mem in fellowship]
print(new_fellowship1)



# %%
# DICT COMPREHENSIONS
# <key> : <value>
# create a list as members as keys and values as length of each string

new_fellowship = {member : len(member) for member in fellowship}
print(new_fellowship)



# %%
# GENERATORS
# not store all the list to memory instead creating obj
# use () instead of []

# List of strings
fellowship = ['frodo', 'samwise', 'merry', 'aragorn', 'legolas', 'boromir', 'gimli']

# List comprehension
fellow1 = [member for member in fellowship if len(member) >= 7]

# Generator expression
fellow2 = (member for member in fellowship if len(member) >= 7)
# %%

# create a generator object that will produce values from 0 to 30.
# num as iterator variable

result = (num for num in range(31))
print(next(result))
print(next(result))

# print rest of the result
for i in result:
    print(i)

# %%
# give list of strings lannister, using a generator expression,
# create a generator object that iterate over the print its values
# create generator obj and print the values of lengths each character 

lannister = ['cersei', 'jaime', 'tywin', 'tyrion', 'joffrey']

# Create a generator object: lengths
lengths = (len(person) for person in lannister)

# iterate over and print the values in lengths
for i in lengths:
    print(i)

# %%
# Create a generator function with a similar mechanism as lengths above

# Define generator function get_lengths
def get_lengths(input_list):
    """Generator function that yields the length of the strings in input_list."""
    # Yield the length of a string
    for person in input_list:
        yield len(person)

# Print the values generated by get_lengths()
for i in get_lengths(lannister):
    print(i)
# %%
    length_count = []
    # Yield the length of a string
    for person in lannister:
        length_count.append(len(person))
# Print the values generated by get_lengths()
print(length_count)
# %%
for i in lannister:
    print(list(len(i)))    
# %%
