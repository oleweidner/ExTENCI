#!/usr/bin/python

""" This sifts throug the raw results 'results.csv' and 
    generates a Gnuplot barchart from it. 
"""

import csv, sys

dataset = dict()

# Read and re-format the data from csv file

with open('results.csv', 'rb') as f:
    reader = csv.DictReader(f)
    try:
        for row in reader:
            if row['filesize'] not in dataset:
                dataset[row['filesize']] = dict()
            dataset[row['filesize']][row['resource']] = row['duration']

    except csv.Error as e:
        sys.exit('file %s, line %d: %s' % (filename, reader.line_num, e))

# add sums, averages and totals to the dataset

fs_keys = dataset.keys()    # filsize keys
rs_keys = dataset['16'].keys() # resource names 

sys.stdout.write("%-12s" % 'Filesize')
for rs_key in rs_keys:
    sys.stdout.write("%-21s" % rs_key)
print('TOTAL \n')

# convert keys to int
for 

for fs_key in fs_keys:
    sys.stdout.write('%-12s  ' % fs_key)
    total = 0.0
    for rs_key in rs_keys:
        value = dataset[fs_key][rs_key]
        sys.stdout.write("%-21s" % value)
        if value != '-':
            total += float(dataset[fs_key][rs_key])
    sys.stdout.write('%f\n' % (total))

sys.exit(0)
