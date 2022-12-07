# Last Max Standing

## Problem Statement

Given a circular array of 'n' elements.

Find the last maximum element on which the following operation is performed :-

Get the maximum element of the array, check if the next two elements are in strictly increasing order, then delete the maximum and next adjacent element from the arrray. else delete the maximum element only.

Note : If duplicate occurence is present, then consider the first occuring index.

## Input Format

First line contains 'n' which denotes the number of elements in the array.

Second line contains n space separated integers.

## Constraints

1 <= n <= 10^5

## Output Format

Print the last maximum element.

## Sample Problems

**Input 1:**

    n = 6
    arr = {6, 1, 9, 0, 2, 4}

**Output 1:**

    4

## Explaination

{6, 1, 9, 0, 2, 4}

Maximum element = 9, next two element 0 and 2, and 0 < 2, so 9 and 0 are deleted.

Now array becomes {6, 1, 2, 4}

Max element = 6, next two element 1 < 2, so 6 and 1 are deleted.

Array becomes { 2, 4}

Max element = 4, next two element 2 < 4, so 4 and 2 are deleted.

The last max element which followed the gived operation is 4.

## Solution

While there is more than one element in the array, find the maximum element in the array, then check if the next two element are in strictly increasing order. If yes, the remove current and adjacent element, else delete the current element only.
