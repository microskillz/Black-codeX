alist = [1, 2, 3, -2, -2, .5]

indexing_length = len(alist) - 1
sort = False

while not sort:
    sort = True
    for x in range(0, indexing_length):
        if alist[x] > alist[x + 1]:
            sort = False
            alist[x], alist[x + 1] = alist[x + 1], alist[x]

            print(alist)
