# Assemble All Statues

## Problem Statement

L. Lalit has opened up a new museum in his town. He decided to organise a display for statues in his new museum. The statues are scattered all around the museum. For the comfort of visiters, he wants them to be aligned in a straight line. Now, moving a statue required a certain amount of money to be spent. Since Lalit has already spent a huge sum of money on building the museum and buying statues, he wants to minimize this cost, and he turns to you to help him solve this problem.

Imagine the museum as a 2-d grid in xy plane with 0,0 as the center of museum. There are n statues located at position (x[i], y[i]) where 0 <= i < n.

To move a statue from A (x[a], y[a]) to B (x[b], y[b]), the cost is abs(x[b] - x[a]) + abs(y[b] - y[a]), where abs(p) is absolute value of p.

Calculate the minimum cost to arrange all the statues side-by-side in a straight line parallel to x-axis.

## Input Format

First line of input contains N = Number of statues

Second line of input contains space separated integers, X position of statues

Third line of input contains space separated integers, Y position of statues.

## Constraints

1 <= N <= 10^5

-10^7 <= X, Y <= 10^7

## Output Format

Output a single integer: minimum cost.

## Sample Problems

**Input 1:**

    n = 2
    x = [1, 4]
    y = [1, 4]

**Output 1:**

    5

## Explaination

Here we have two statues situated at coordinates [1, 1] and [4, 4].

The optimal solution is to move [1, 1] to [3, 1] and cost for moving = 2,
same with [4, 4] to [4, 1] and the cost of moving = 3. So total cost is 2+3 = 5.

![image](https://s3.amazonaws.com/hr-assets/0/1670076390-75a3fb6e75-Untitled-1.png)

## Solution

Since we need to find out the minimum cost, one naive approach can be to calculate the cost for each point on both the axis and the take the minimum of it. We can do this for both the axis individually and the get the minimum cost.

Because we need to find out the cost for each point, the time complexity for this solution is **Max(X, Y) \* N**.

If we output the costs of the above implementation, we can notice a trend where the cost first decreases, reaches a minimum, then proceeds to increase again. Thus, we can optimize the above algorithm using binary search.

We start with the middle of the possible positions.
We then calculate the cost at that position, and for the position one behind it.

If the cost of the position behind it is more, we are approaching the minimum.

If the cost is less, then the minimum is behind it.

In this way we can optimise the solution. And the time complexity of this method is **log(Max(X, Y)) \* N**.
