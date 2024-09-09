import numpy as np


def partition(arry, p, q):
    piv = arry[p]
    while p < q:
        while p < q and arry[q] > piv:
            q = q - 1
        arry[p], arry[q] = arry[q], arry[p]
        while p < q and arry[p] <= piv:
            p = p + 1
        # arry[p], arry[q] = arry[q], arry[p]
    return q


def quickSort(arry, p, q):
    if p < q:
        r = partition(arry, p, q)
        print(f"quickSort({p},{r})")
        print(f"quickSort({r+1},{q})")
        if r > 0:
            quickSort(arry, p, r - 1)
        else:
            quickSort(arry, p, r)
        quickSort(arry, r + 1, q)


lista = [2, 1, 12, 0, 3, 7, 9, 4]
z = np.array(lista)

print(z)
print(quickSort(z, 0, 7))
print(z)
