'''def print_pairs(items):
    for i in items:
        for j in items:
            print(i,j)
print_pairs([1, 2, 3])'''


def has_duplicate(item):
    n = len(items)
    for i in range(n):
        for j in range(i+1,n):
            if items[i] == item[j]:
                return True
