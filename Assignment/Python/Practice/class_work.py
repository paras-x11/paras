import random

names = [
    'rashid shaikh', 'jash patel', 'harshni patil', 'rohit visave',
    'Sandip upadhyay', 'Ganesh', 'bipin jaiswal', 'KULBHUSHAN',
    'parth patel', 'manoj patil', 'paras rana', 'Parthvi paneliya'
]


random.shuffle(names)


if len(names) % 2 == 0:
    pairs = []
    for i in range(0,len(names),2):
        pair = (names[i], names[i + 1])
        pairs.append(pair)
        print(pair)
else:
    print('Cannot form a pair with an odd number of players.')

# for pair in pairs:
#     print(pair)