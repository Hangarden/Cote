changes= int(input())

coins = [500,400,100]
count = 0
for x in coins:
    if changes < x:
        continue
    else:
        while changes >=x:
            changes -= x
            count += 1
print(count)