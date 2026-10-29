# CCC 2011 J2 - Who Has Seen The Wind
# https://dmoj.ca/problem/ccc11j2

h = int(input())
m = int(input())
touched = False
for t in range(1, m + 1):
    altitude = -6 * t**4 + h * t**3 + 2 * t**2 + t
    if altitude <= 0:
        print('The balloon first touches ground at hour:')
        print(t)
        touched = True
        break
if not touched:
    print('The balloon does not touch ground in the given time.')
