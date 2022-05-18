# Trail of Zeros

## Problem Statement

There is an array A where every element appears twice, but for one element which appears exactly once. Return the number of trailing zeros after the calculation of factorial of that number.

## Input Format

The first line contains N, the number of integers in the Array.
The second line contains N space separated integers.

## Constraints

0 <= n <= 10^5
0 <= A[i] <= 10^9

## Output Format

A single integer output contaning number of zeroes.

## Sample

**Input 1**

    7
    2 5 3 12 3 2 5

**Output 1**

    2

**Input 2**

    3
    100 248 100

**Output 2**

    59

## Explaination

**Example**

1. A = [5,3,9,10,3,9,5]. In this array the unique element is 10. Now 10! = 36,28,800 which has two trailing zeros, so the answer is 2.
2. A = [11,4,23,10,23,9,9,11,10]. In this array the unique element is 4. 4! = 24 which has no trailing zeros, so the answer is 0.

This problem can be divided into two sub problems:

1. Find the unique element.
2. Find the number of trailing zeros in the factorial of unique number.

Now there are multiple way to find a unique element in an array.

### Naive Approach

A naive approach could be just go through the array elements one by one, and check if there is a duplicate element in the array, until we find the unique element.
This approach has a time complexity of **O(n^2)**, which is not great.

### Sorting

We can sort the array, after sorting all the occurance of elements become consecutive, and then we can easily find the unique element by traversing the array in **O(n)** time.
This approach has a time complexity of **O(nlogn)**. But we can do better.

### Using a hashmap

We can use a hashmap to store the count of number of times an element was encountered in array, and then we can easily find out the unique element.
This approach has time complexity of **O(n)** as we traverse through the array only once, but the space complexity is **O(n)**, because we hashmap to store elements.

### Bitwise Xor

Using hashmap is a good approach, but we trade off time with space.
How Bitwise Xor works?
It is a bitwise operator (represented by ^) which stands for "exclusive or", which evaluated to **False(0)** when both input bits are same, else **True(1)**.
| A | B | A^B |
|-----|-----|:-------:|
| 1 | 1 | 0 |
| 1 | 0 | 1 |
| 0 | 1 | 1 |
| 0 | 0 | 0 |

Example :

    A = 5, B = 3
    then A^B = 6,
    becase bin(5) = 101, and bin(3) = 011,
    so A^B = 110 which is 6 in decimal.

Another Example:

    A = 7, B = 7,
    then A^B = 0,
    because bin(7) = 111 and since both the values are same, the result will be 000 which is 0 in decimal.

We can apply this knowledge to our problem.
We will traverse through the array Xoring all the elements, each of the duplicate element will evaluate to zero with only our unique element left.
This approach has a time complexity of **O(n)** and constant space complexity.

#### Now that we have our unique element, we need to find the trailing zeros of it's factorial.

### Naive Approach

A simple approach can be just calculating the factorial and then count the number of zeros in the end.
This works fine for small numbers, but factorial can be extremly large for medium to big numbers. So this won't work.

### Other way:

A number

    N = 12340000 can be represneted as 1234 X 10^4, and 4 is the number of trailing zeros. 10^4 can be written as 2^4 X 5^4.

This means if we just count the number of 2's and 5's in the factorial, then the number of zeros will be the least of the both values.
Also because number of 5's will always be less than 2's, we only need to count the number of times we encounter the multiple of 5's
In our first example

    10! which is 1 X 2 X 3 X 4 X 5 X 6 X 7 X 8 X 9 X 10

has 2 fives, one five itself and 10 = 2 \* 5.
and so 10! will have 2 trailing zeros, which is correct.
