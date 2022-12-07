# Shifted Primes

## Problem Statement

Aman is curious about prime numbers.He has been provided with an array depicted in the following manner, [[a0,k0],[a1,k1],....upto n elements]
where 'a0' depicts the value of 'a' at the 0-th index, 'k0' depicts the value of 'k' at the 0-th. Aman has been instructed to check whether the numbers given
to him are prime or not by following the given instructions --->
Convert 'a' to binary form and check the number of 1's in it,if :-

- 'a' has even number of 1's, then perform right shifting operation on it 'k' times.
- 'a' has odd number of 1's, then perform left shifting operation on it 'k' times.

If the resultant number after performing the above operations is prime then return 1 else 0.

## Input Format

First line contains integer N
where N is size of array

Second line contains N space separated integers denoting 'a'

Third line contains N space separated integers shift denoting 'k'

## Constraints

0 < N <= 10^5

0 < a <= 10^7

0 <= k <= 15

## Output Format

An array of booleans.

## Sample

**Input 1**

    2
    2 20
    4 2

**Output 1**

    0 1

**Explaination:**

The binary form of 2 is 10 .It has off number of 1's,thus we perform left shifting 4 times and the resultant value becomes
100000 which is equal to 32. 32 is not a prime number hence Aman receives 0 as the answer.

The binary value of 20 is 10100. It has even number of 1's, thus we perform right shifting operation 2 times and the resultant becomes
101 which is equal to 5. 5 is a prime number hence Aman receives 1 as the answer

## Solution

A niave approach is to iterate over the list of elements, perform the required operation and calculate if the resultant number is prime or not.

This approach has a time complexity of N \* sqrt(a).

Since we calculate primes multiple times, we can optimize it by pre calculating all the primes in given range, and then just check if the resultant number is in the given list or not. Primes can be efficiently calculated using Sieve of Eratosthenes. The time complexity for this approach is N \* a log(log(a)), and we are using an extra N.
