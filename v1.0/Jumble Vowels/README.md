# JUMBLE VOWELS

## Problem Statement

You are given a string of length N.You have to reverse only the vowels occurring in the string and print it.

## Input Format

First line contains N. The Second line contains the string itself.

## Constraints

The string consists of only lower case alphabets and spaces. 1<=N<=10^8

## Output Format

Print only the string after performing the desired operation.

## Sample Problems

**Input 1:**

    13
    shinra tensai

**Output 1:**

    shinra tensai

**Input 2:**

    5
    hello

**Output 2:**

    holle

## Explaination

**Example:**

1. Input :- “hello” Output:- “holle” 

**Explanation** :- The only vowels occurring in the given string are ‘e’ and ‘o’ and after reversing them in there respective order as per the string the new order become ‘o’ and ‘e’ and hence the string “holle” is printed.

2. Input :- “haldia” Output :- “haldia” 

**Explanation** :- The sequence of vowels is ‘a’,’i’,’a’ which is behaves like a palindrome and hence the string remains unaffected.


## Solution

One approach can be of using two pointers, where we initialize one from the start of the string and one from the end.

Let's say we initialize two variables namely **i = 0** and **j = n - 1**. (zero based indexing)

Now on each iteration, we can have 4 of the following conditions

- both the character at position i and j are not vowels, in this case we can simply increment **i** and decrement **j**.
- character at **i** is a vowel, in this case we decrement **j**.
- character at **j** is a vowel, in this case we increament **i**.
- both the character at **i** and **j** are vowels, in this case we just swap the characters and then increment **i** and decrement **j** respectively.

we can repeat this process while **i** is less than **j**. And in the end we will have the string with it's vowels reversed.
