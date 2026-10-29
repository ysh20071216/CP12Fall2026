# CCC 2021 J2 - Silent Auction
# https://dmoj.ca/problem/ccc21j2

n = int(input())
winning_name = ''
highest_bid = -1
for i in range(n):
    name = input().strip()
    amount = int(input())
    if amount > highest_bid:
        highest_bid = amount
        winning_name = name
print(winning_name)
