import csv
import random

def fiveRandom(length):
    random_indices = []
    for x in range(5):
        random_indices.append(random.randint(0,length-1))
    return random_indices

cardFile = open('DeepNet.csv', 'r')
cardReader = csv.reader(cardFile,delimiter='\n')

data = []
for row in cardReader:
    addList = list(row[0])
    addList = list(filter(lambda a: a != ',',addList))
    data.append(addList)

del data[0] #Removing header

#Removing first column
for i in range(len(data)):
   data[i].pop(0)

over_seventy_five_counter = 0
for y in range(100):
    indices = set()
    for x in range(30):
        row_indices = fiveRandom(len(data))
        column_indices = fiveRandom(len(data[0]))
        for x in range(5):
            indices.add(str(row_indices[x])+','+str(column_indices[x]))

    probability = len(indices)/(len(data)*len(data[0]))

    if(probability>0.75):
        over_seventy_five_counter += 1


print('Over Seventy Five of map as a probability : ',over_seventy_five_counter/100)
