panagram = """The quick brown
fox jumps\tover 
the lazy dog"""

words = panagram.split()
print(words)

numbers = "9,223,337,807"
print(numbers.split(","))

values_list = [
    '9', '223', '372', '036', '854', '775', '807'
]

# replace the values in place
for index in range(len(values_list)):
    values_list[index] = int(values_list[index])

print(values_list)

# create a new list
integer_values = []
for value in values_list:
    integer_values.append(int(value))

print(integer_values)