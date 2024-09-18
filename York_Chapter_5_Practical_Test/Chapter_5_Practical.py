import csv
from contextlib import nullcontext

# Pull in the CSV file
filename = 'candy_type.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    # Loop through the csv file and create two lists
    candy_type = []
    candy_price = []

    for row in reader:
        candy = row[1]
        price = float(row[2])
        candy_type.append(candy)
        candy_price.append(price)
    print(candy_type)
    print(candy_price)

candy_type2 = candy_type[:]
candy_type2.sort()
duplicate_list = []
count = 1

for type_one in candy_type2:
    for type_two in range(len(candy_type2)-1):
        if type_two+count >= len(candy_type2):
            True
        else:
            if type_one == candy_type2[type_two + count]:
                duplicate_list.append(candy_type2[type_two + count])
    count += 1

duplicate_list.sort()
duplicate_list = set(duplicate_list)
candy_type2 = set(candy_type2)

print(f"All of these are duplicates: {duplicate_list}")

print(f"{candy_type[23]} costs ${candy_price[23]}")
print(f"{candy_type[24]} costs ${candy_price[24]}")
print(f"{candy_type[25]} costs ${candy_price[25]}")
print(f"{candy_type[26]} costs ${candy_price[26]}")
print(f"{candy_type[27]} costs ${candy_price[27]}")

count = 0

for price in candy_price:
    if price > 3.00:
        candy_price.pop(count)
    count += 1
print(candy_price)

total = 0

for sum in candy_price:
    total += sum

print(f"The total is ${total}.")