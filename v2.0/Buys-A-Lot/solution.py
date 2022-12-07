def AllGadgets(moneyWithBob, moneyWithFriend, prices):
    prices.sort()  # sort the array 1st
    bob = []
    friend = []
    for i in prices:
        if i % 2 == 0:  # if the price is even, friend can buy that
            friend.append(i)
        else:
            bob.append(i)  # if the price is odd, bob can buy that

    count = 0
    bobSum = 0
    for i in bob:  # traverse the list of gadgets which bob can buy
        if bobSum + i < moneyWithBob:  # check bobSum is less than total money with bob
            bobSum += i  # if yes- add the product value, also increase the count
            count += 1
    friendSum = 0
    for i in friend:
        if friendSum + i < moneyWithFriend:
            friendSum += i
            count += 1
    return count
