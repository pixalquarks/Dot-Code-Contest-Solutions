# Most optimised solution for a size of list N involves Sieve of Eratosthenes as its prime focus.


def solution(arr):

    # finding the max element in order to finalise the size for the sieve.
    n = -(2**31)
    for i in range(len(arr)):
        n = max(n, arr[i][0])

    # Sieve of Eratosthenes
    prime = [True for i in range(n + 1)]
    prime[0], prime[1] = False, False
    p = 2
    while p * p <= n:
        if prime[p] == True:
            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1

    # All the prime numbers upto n(which is the max no. in the array) have been successfully stored as True in the primes list.

    # Storing all the suitable numbers in the ans list by following the given instructions.
    ans = []
    for i in range(len(arr)):
        num = arr[i][0]
        binary = bin(arr[i][0])[2:]
        k = arr[i][1]
        if binary.count("1") % 2 == 0:
            num = num >> k
        else:
            num = num << k
        if prime[num]:
            ans.append(True)
        else:
            ans.append(False)
    return ans

    # The time complexity for the above program is N*log(log(N)).
    # The space complexity for the above program is N.
