def multiply(x, y):
    result = x * y
    return result


def is_palindrome(string: str) -> bool:
    # backwards = string[::-1]
    # return backwards == string
    return string[::-1].casefold() == string.casefold()


def palindrome_sentence(sentence: str) -> bool:
    string = ""
    for char in sentence:
        if char.isalnum():
            string += char
    return is_palindrome(string)

# answer = multiply(3, 5)
# print(answer)
#
# print()
#
# for val in range(1, 5):
#     two_times = multiply(2, val)
#     print(two_times)


# word = input("Please enter a word to check: ")
# if palindrome_sentence(word):
#     print("'{}' is a palindrome".format(word))
# else:
#     print("'{}' is not a palindrome".format(word))
# answer = multiply(18, 3)
# print(answer)


def fibonacci(n):
    """Return the `n`th Fibonacci number, for positive `n`."""
    if 0 <= n <= 1:
        return n
    n_minus1, n_minus2 = 1, 0

    result = None
    for f in range(n - 1):
        result = n_minus2 + n_minus1
        n_minus2 = n_minus1
        n_minus1 = result

    return result


for i in range(36):
    print(i, fibonacci(i))
