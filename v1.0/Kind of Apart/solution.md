# Kind of Apart

## Problem Statement

Given a string A of length N and an integer K, remove all the elements exactly K characters apart from each other in english alphabet. A[i] and A[j] are K element apart if A[i] = A[j] - K, where A[i] and A[j] are elements of A and i != j.

## Input Format

First line contains N and K Second line is the string A itself

## Constraints

0 <= N <= 10^7 0 <= K <= 26 each character in A is a lowercase english alphabet.

## Output Format

A single line output containing the resulting string.

## Sample

**Input 1**

    16 5
    chamberofsecrets

**Output 1**

    amberofsecrets

**Example:**

1. Input: N = 5, K = 7 A = "hello" Output: "hlo"

**Explaination:**
'e' and 'l' are seperate by exaclty 7 characters in english alphabet, so they both will be removed and string becomes "hlo". Now no adjacent elements in string are K characters apart, so "hlo" is our final string.

2. Input N = 6, K = 10 A = "axishi" Output: "ai"

**Explaination:**
'i' and 's' are 10 characters apart so we remove them. Now we are left with string "axhi". 'x' and 'h' are also 10 characters apart so we remove them, now we are left with "ai", which is our resulting string.

## Solution

Naive Approach:

We will traverse though the array, and check each consecutive pair of characters that if they are K apart. If not then we return the string else, remove the pair and start again from the begining.
In best case(when no consecutive pairs are k apart), the time complexity will be O(n). But in worst case it will be O(n^2).

Using Stack:
When we remove a pair, we don't actually need to start from the very beginning again. We can just check go for the next character, and check if the previous character, after removing the pair, is consecutive or not. We will need to use the stack for storing character.

Initialize the stack, then traverse through the string.
On each iteration check if the stack is empty, if it is, just push the character into the stack and move on.
If it is not then check if the top most character satisfies our condition. If yes then pop the character and continue, else push the current character into the stack.

**Note :** There can be a condition where, ASCII(A[i]) - K is less than 97(ASCII value of 'a'), in this case we need to add 26(number of lowercase english alphabets) to it, to make it a valid lowercase english character. Example : ASCII(h) = 104, 104 - 10 = 94 which is less than 97, so we add 26 and make it 120, which is ASCII of 'x'.
