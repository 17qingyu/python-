tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

maxLen = [0 for i in range(0, len(tableData[0]))]
for j in range(0, len(tableData[0])):
    for i in range(0, len(tableData)):
        if len(tableData[i][j]) > maxLen[j]:
            maxLen[j] = len(tableData[i][j])

for i in range(0, len(tableData)):
    for j in range(0, len(tableData[i])):
        print(tableData[i][j].rjust(maxLen[j]), end="|")
    print()
