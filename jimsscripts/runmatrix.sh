#!/bin/bash

hostname -f
echo
echo
echo "**************************************************"
#module load python
python -V
echo
echo "**************************************************"
cat << "EOF" >matrixl.py
#!/usr/bin/python
# -*- coding: utf-8 -*-
# usage: python matrix.py [total_minutes [notify_minutes] [outfile]]

import copy
import sys
import random
from datetime import datetime
def testcols(a):
    keys = 'JLMA'
    cols = 0
    for c in range(10):
        counts = [0,0,0,0]
        for r in range(10):
            l = a[r][c]
            i = keys.index(l)
            counts[i] += 1
        if counts[0]+counts[1] != counts[2]+counts[3]:
            return cols
        if counts[0]>3 or counts[1]>3 or counts[2]>3 or counts[3]>3:
            return cols
        if counts[0]<2 or counts[1]<2 or counts[2]<2 or counts[3]<2:
            return cols
        if (c+1) > cols:
            cols = c+1
    return cols
def trunc(s):
    i = s.index('.')
    return(s[0:i+3])
start = datetime.now()
minute = 650000
trys = 3
notify = 1
outfile = 'out.txt'
if len(sys.argv) > 1:
    trys = int(sys.argv[1])
    if len(sys.argv) > 2:
        notify = int(sys.argv[2])
    else:
        notify = max(trys/10,1)
    if len(sys.argv) > 3:
        outfile = sys.argv[3] + 'out.txt'
try:
    f = open(outfile, 'w')
except IOError:
    print 'Cannot open %s\n' % (outfile)
    exit(1)
f.write('Start at: %s\n'%(trunc(str(start))))
f.flush()
trys = trys * minute
notify = notify * minute
max = 0
tottrys = 0
a = [['J', 'J', 'L', 'L', 'L', 'M', 'M', 'A', 'A', 'A'],
     ['J', 'J', 'L', 'L', 'L', 'M', 'M', 'M', 'A', 'A'],
     ['J', 'J', 'J', 'L', 'L', 'M', 'M', 'A', 'A', 'A'],
     ['J', 'J', 'J', 'L', 'L', 'M', 'M', 'M', 'A', 'A'],
     ['J', 'J', 'L', 'L', 'L', 'M', 'M', 'A', 'A', 'A'],
     ['J', 'J', 'L', 'L', 'L', 'M', 'M', 'M', 'A', 'A'],
     ['J', 'J', 'J', 'L', 'L', 'M', 'M', 'A', 'A', 'A'],
     ['J', 'J', 'J', 'L', 'L', 'M', 'M', 'M', 'A', 'A'],
     ['J', 'J', 'L', 'L', 'L', 'M', 'M', 'A', 'A', 'A'],
     ['J', 'J', 'J', 'L', 'L', 'M', 'M', 'M', 'A', 'A']]
result = [['-' for i in range(10)] for j in range(10)]
n = 0
map(random.shuffle,a)
previous = start
while max<10:
    new = testcols(a)
    if new > max:
        max = new
        result = copy.deepcopy(a)
        tottrys = n + 1
    n += 1
    if n%(notify) == 0:
        time = datetime.now()
        delta = time - previous
        f.write('Try: %10d   Cols:%3d    Time: %s\n'%\
        (n, max, trunc(str(delta))))
        f.flush()
        previous = time
    if n >= trys:
        tottrys = n
        break
    map(random.shuffle,a)
if max == 10:
    f.write('Success\n')
    print 'Success'
else:
    f.write('Fail\n')
    print 'Fail'
end = datetime.now()
f.write('End at: %s\n'%(trunc(str(end))))
f.write('Total Tries: %10d\n' % tottrys)
print 'Total Tries: %10d' % tottrys
f.write('Elapsed time: %s\n'%(trunc(str(end-start))))
f.write('Columns meeting criteria: %3d\n'% (max))
print 'Columns meeting criteria: %3d'% (max)
for r in range(10):
    for c in range(10):
        if c < 9:
            f.write('%s\t'%(result[r][c]))
        else:
            f.write('%s\n'%(result[r][c]))
f.close()
EOF
python matrixl.py $*
