import re

filename = "regex_sum_82324.txt"
hand = open(filename)
numlist = []

for line in hand:
    line = line.rstrip()
    results = re.findall('[0-9]+', line)

    if not results: continue

    for result in results:
        num = int(result)
        numlist.append(num)

sum_num = sum(numlist)
print(sum_num)