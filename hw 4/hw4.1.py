
# File: hw4.1.py
# Author(s): Bryce Benjamin


def compute_Category_Totals(list, category_total, category1_total, category2_total, category3_total, category4_total):
    
    for l in list:
        if l[1] == "meal":
            category1_total += l[2]
              
        elif l[1] == "travel":
            category2_total += l[2]
            
        elif l[1] == "supply":
            category3_total += l[2]
        
        elif l[1] == "util":
            category4_total += l[2]
            
        category_total += l[2]
    return category1_total, category2_total, category3_total, category4_total, category_total


# hw3.1.b
# print("\n1.b:")
records2 = []
with open('expenses.txt', 'rt', encoding='utf-8') as fin:
    for line in fin:
        columns = line[:-1].split(':')
        records2.append(columns)

# for row in records2:
#     print(row)

# hw3.1.d
# print("\n1.d:")
header = records2[0].copy()
data = records2[1:].copy()

# print(header)
# for d in data:
#     print(d)

# hw3.1.e
# print("\n1.e:")

for d in data:
    d[0] = float(d[0])  # change str to float
    
# print(header)
# for d in data:
#     print(d)

# hw3.1.f
# print("\n1.f")
data.sort()
print(header)
for d in data:
    print(d)

# hw3.1.g

categories = set()
for d in data:
    categories.add(d[1])  # column sub-1 contains the categories

print('\nThere are', len(categories), 'expense categories:')
for c in categories:
    print(c)

# hw3.1.h

# dictionary of month number to 3-letter month name string

n2s = { '01': 'Jan',
        '02': 'Feb',
        '03': 'Mar',
        '04': 'Apr',
        '05': 'May',
        '06': 'Jun',
        '07': 'Jul',
        '08': 'Aug',
        '09': 'Sep',
        '10': 'Oct',
        '11': 'Nov',
        '12': 'Dec' }

print("\nKey\tValue")
for i in n2s.items():
    print(i[0] + "\t" + i[1])
#hw4.1.a

# hw4.1.b
print("\n")
print("-------------------------------------------------------")
data = sorted(data)
[print("{:8s}  {:10s}{:10s}{:10s}".format(header[0], header[1], header[2], header[3]))]
[print("{:8.2f}  {:10s}{:10s}{:10s}".format(d[0], d[1], d[2], d[3])) for d in data]
# hw4.1.c
print("\n")
print("-------------------------------------------------------")
[print("{:10s}{:10s}{:8s}  {:10s}".format(header[2], header[1], header[0], header[3]))]
[print("{:10s}{:10s}{:8.2f}  {:10s}".format(d[2], d[1], d[0], d[3])) for d in data]
# hw4.1.d
print("\n")
print("-------------------------------------------------------")
for d in data:
    date = d[2]
    year = date[0:4]
    num_month = date[4:6]
    day = date[6:]
    for i in n2s.keys():
        if num_month == i:
            month = n2s.get(i, 'None')
    d[2] = "{}-{}-{}".format(day,month,year)
[print("{:15s}{:10s}{:8s}  {:10s}".format(header[2], header[1], header[0], header[3]))]
[print("{:15s}{:10s}{:8.2f}  {:10s}".format(d[2], d[1], d[0], d[3])) for d in data]
# hw4.1.e
print("\n")
print("-------------------------------------------------------")
data_copy = data.copy()
for d in data_copy: #swapping the date and amount columns
    d[0], d[2] = d[2], d[0]

header[0], header[2] = header[2], header[0]
data_copy = sorted(data_copy)
[print("{:15s}{:10s}{:8s}  {:10s}".format(header[0], header[1], header[2], header[3]))]
[print("{:15s}{:10s}{:8.2f}  {:10s}".format(d[0], d[1], d[2], d[3])) for d in data_copy]

# hw4.1.f
print("\n")
print("-------------------------------------------------------")
total = 0
meal_total = 0
travel_total = 0
supply_total = 0
entr_total = 0
education_total = 0
util_total = 0
meal_total = float(meal_total)
travel_total = float(travel_total)
supply_total = float(supply_total)
entr_total = float(entr_total)
education_total = float(education_total)
util_total = float(util_total)
total = float(total)
[print("{:15s}{:10s}{:8s}  {:10s}".format(header[0], header[1], header[2], header[3]))]
[print("{:15s}{:10s}{:8.2f}  {:10s}".format(d[0], d[1], d[2], d[3])) for d in data_copy]

meal_total, travel_total, util_total, supply_total, total = compute_Category_Totals(data_copy, total , meal_total, travel_total , supply_total, util_total)
print("{:>25s}{:8.2f}".format("Total: ", total))
print("{:>25s}{:8.2f}".format("Meal Total: ", meal_total))
print("{:>25s}{:8.2f}".format("Travel Total: ", travel_total))
print("{:>25s}{:8.2f}".format("Supply Total: ", supply_total))
print("{:>25s}{:8.2f}".format("Utility Total: ", util_total))

#hw4.1.gh