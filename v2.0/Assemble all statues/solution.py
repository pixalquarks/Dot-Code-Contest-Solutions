def calc_cost(arr, position, y):
    cost = 0
    for i in arr:
        cost += abs(position - i)
        if (
            not y
        ):  # if we are calculating the cost for x axis, then we need to increment the position by 1, as we need to align next to each other.
            position += 1
    return cost


def binary(arr, y):
    l, h = -(10**7), 10**7  # Min and max value for position.

    min_cost = float("inf")
    while l <= h:
        mid = l + (h - l) // 2
        c1 = calc_cost(arr, mid, y)  # Calculate cost for the current position.
        c2 = calc_cost(
            arr, mid + 1, y
        )  # Calculate cost for the position after the current position.

        # If the cost for the current position is less than the cost for the position after the current position, that means minimum is behind the current position, i.e. in the range [l, mid - 1].
        if c1 < c2:
            min_cost = min(min_cost, c1)
            h = mid - 1
        # If the cost for the current position is greater than the cost for the position after the current position, that means minimum is ahead of the current position, i.e. in the range [mid + 1, h].
        else:
            min_cost = min(min_cost, c2)
            l = mid + 1
    return min_cost


def minimunAlignmentCost(numberOfStatues, xPositions, yPositions):
    y_cost = binary(yPositions, True)  # calculate cost for y axis.
    x_cost = binary(xPositions, False)  # calculate cost for x axis.
    return x_cost + y_cost
