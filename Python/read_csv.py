print("-----------------read teks .csv-------------------")
import csv
f = open('d:/DQLAB/datadki.csv', 'r')
reader = csv.reader(f)
for row in reader :
    print(row)

print("-----------------read teks .csv using pandas------------------")

import pandas as pd
f = pd.read_csv('d:/DQLAB/datadki.csv')
f.head()
print(f)

