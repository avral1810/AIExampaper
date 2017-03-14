import os
import random

diff_range = [0,20]
util_range = [0,5]

minQforeach = int(int(diff_range[1])/int(util_range[1]))

while(1):
    avgDiff = input('Enter  diff of paper : ')
    avgDiff = int(avgDiff)
    if(avgDiff >= 0 and avgDiff <= diff_range[1]):
        break

QB = {}
CHECK = {}
file = open('./BANK.txt')
for e in file:
    count,question,diff = e.split(':')
    diff = diff[:-1]
    diff = int(diff)
    val = {question:diff}
    val2 = {question:'0'}
    QB.update(val)
    CHECK.update(val2)

if len(QB) < (minQforeach*(int(util_range[1])+1)):
    print('Too less questions, enter again')
    exit(0)

huval = int(0)

huval = avgDiff % minQforeach
if huval == 0:
    huval = int(avgDiff/minQforeach)
else:
    huval = int((avgDiff/minQforeach))+1
huval = int(huval)

quesList=[]
counter = int(0)


ll =[]

for e in QB.keys():
    ll.append(e)

lee = int(len(QB))

for j in range(0,(minQforeach-(minQforeach-(avgDiff%minQforeach)))):
    while(1):
        currQ = ll[random.randrange(0,lee)]
        if (QB[currQ] == huval) and (CHECK[currQ] == '0'):
            quesList.append(currQ)
            CHECK[currQ] = '1'
            break

for i in range(0,(minQforeach-(avgDiff%minQforeach))):
    while(1):
        currQ = ll[random.randrange(0,lee)]
        if (QB[currQ] == (huval-1)) and (CHECK[currQ] == '0'):
            quesList.append(currQ)
            CHECK[currQ] = '1'
            break

file = open('QUESTIONPAPER.txt','w')
ii = int(1)
for each in quesList:
    file.write('Q' + str(ii) + '. ' + each + '\n')
    ii = ii + 1
file.close()