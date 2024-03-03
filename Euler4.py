'''
A palindromic number reads the same both ways. The largest palindrome made
from the product of two 2-digit numbers is 9009 = 91 Ö 99.
Find the largest palindrome made from the product of two 3-digit numbers.
'''


def is_palindrome(n):
    return str(n) == str(n)[::-1]


if __name__ == "__main__":
    largestPalindrome = 0
    for i in range(100, 999):  # 3 digits range
        for j in range(100, 999):
            prod = i * j
            if is_palindrome(prod):
                if prod > largestPalindrome:
                    largestPalindrome = prod
    print(f'The largest palindrome from the 3 digits product is {largestPalindrome}')




