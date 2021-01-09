import pandas as pd
csv_test = pd.read_csv('./a.csv')

print(csv_test.columns)


int_sum = 0

for i in (csv_test.columns):
    int_sum += float(i)

print(int_sum)

import csv

int_sum = 0

f = open('./a.csv', 'r', encoding='utf-8-sig')
rdr = csv.reader(f)
for line in rdr:
    for i in line:
        int_sum += int(i)

print(int_sum)
f.close()
