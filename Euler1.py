'''
1 Euler Problem 1
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get
3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
'''


def euler1(n):
    multiples_of_3_5 = []
    sum_of_multiples_3_5 = 0
    for i in range(n):
        if i % 3 == 0 or i % 5 == 0:
            multiples_of_3_5.append(i)
            sum_of_multiples_3_5 += i
    print("Sum of multiples of 3 and 5 is : %d" % sum_of_multiples_3_5)
    print("List of  is : %s" % multiples_of_3_5)


if __name__ == "__main__":
    euler1(1000)



