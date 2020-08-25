row = {
    'A': 0,
    'B': 1,
    'C': 2,
    'D': 3,
    '12': 0,
    '3': 1,
    '6': 2,
    '9': 3
}

hashMap = {
    100: 0,
    75: 0,
    50: 0,
    25: 0
}

def analyse(array,row,col):
    for x in range(0,4):
        if x in row:
            continue
        else:
            for y in range(0,4):
                if y in col:
                    conti


testCase = input()
rowCoordinate = []
colCoordinate = []
score = []
input_x = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
init = 0
for x in range(0, int(testCase)):
    arr1 = list(input().split())
    input_x[row[arr1[0]]][row[arr1[1]]] = input_x[row[arr1[0]]][row[arr1[1]]]+1
    if init < input_x[row[arr1[0]]][row[arr1[1]]]:
        init = input_x[row[arr1[0]]][row[arr1[1]]]
        colCoordinate[0] = row[arr1[1]]
        rowCoordinate[0] = row[arr1[0]]


