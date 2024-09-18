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
new_list = []
dup = []

for type in candy_type2[:]:
    if type == "Almond Joy":
        candy_type2.remove(type)

print(candy_type2)
print(new_list)
