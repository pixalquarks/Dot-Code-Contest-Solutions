# Buys-A-Lot

## Problem Statement

Bob and his friend have some money to buy some gadgets. All the gadgets are different but their cost can be same. Bob only buys those gadgets whose cost is odd and his friend buys the gadgets whose cost is even. Find the maximum number of gadgets they can buy together.

## Input Format

First line of input contains:
**T** = number of test cases

For next T lines contains:
**N** = number of gadgets

## Constraints

1 <= T <= 10^3
1 <= N <= 10^5

## Output Format

Output A single integer: Maximum number of gadgets they can buy together.

## Sample Problems

**Input 1:**

    2
    8 75 62
    23 34 12 44 29 39 19 28
    10 73 54
    12 34 25 32 10 15 20 39 29 30

**Output 1:**

    5
    6

## Explaination

Bob can buy gadgets costing – 23, 29, 39, 19. Hence, bob will buy the gadgets costing 19, 23, 29.He cannot buy next one because he has only 75 as total amount.

His friend can but gadgets costing – 34, 12, 44, 28. Hence, he will buy the gadgets costing 12, 28. He cannot buy next two because he has only 62 as total amount.

Hence, the answer is 3 2 = 5.

## Solution

A simple approach to this question, go greedy. Sort the array of elements, and then divide them into two arrays, one with all the items with even cost, and other with odd. Then just iterate over the both the array one by one, and buy all the items until, until money runs out and not more item can be bought.
