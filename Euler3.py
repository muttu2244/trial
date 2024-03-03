'''
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
'''


def euler3(n):

    listofprimeFactors = []
    smallestPrimeNum = 2

    for i in range(2, n):
        if n % i == 0:
            listofprimeFactors.append(i)
            print(i)
            #smallestPrimeNum += 1
    print(f'the largest prime factor for the given number is: {max(listofprimeFactors)}')


    #print("Sum of multiples of 3 and 5 is : %d" % sum_of_multiples_3_5)
    #print("List of  is : %s" % multiples_of_3_5)
    #print(f'sum of fibonacci even numbers  {evensum}')


if __name__ == "__main__":
    euler3(600851475143)



