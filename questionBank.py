import os

count = 0
file = open('./count.txt')
for eachline in file:
    count = int(eachline)
file.close()

num = input('Enter number of questions : ')
num = int(num)
for i in range(0,num):
    question = input('Enter question ' + str(i+1) + '\n')
    while(1):
        difficulty = input('Enter ' + str(i) + ' difficulty' + ' : ')
        difficulty = int(difficulty)
        if(difficulty >= 0 and difficulty <= 5)
            break
    count = count + 1
    file = open('./BANK.txt','a')
    file.write(str(count) + ':' +  question + ':' + str(difficulty) + '\n')
    file.close()
file = open('./count.txt','w')
file.write(str(count))
file.close()
