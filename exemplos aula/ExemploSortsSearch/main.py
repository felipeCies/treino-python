# import module
from sorts import *
from search import *
from hashtable import *

# exemplos https://www.programiz.com/dsa/heap-sort

data = [9, 5, 1, 4, 3, 10, 23, 10001, 2000]

insertionSort(data)
print('Ordenando vetor(insertionsort):')
print(data)

size = len(data)
selectionSort(data, size)
print('Ordenando vetor(selectionsort):')
print(data)

quickSort(data, 0, size - 1)
print('Ordenando vetor(quicksort):')
print(data)

mergeSort(data)
print('Ordenando vetor(mergesort):')
print(data)

heapSort(data)
print('Ordenando vetor(heapsort):')
print(data)

x = 18
n = len(data)
print("Pesquisa Sequencial!")
result = linearSearch(data, x)
if (result == -1):
    print("Elemento não encontrado!")
else:
    print("Elemento encontrado no índice: ", result)

x = 4
print("Pesquisa Binária!")
result = binarySearch(data, x, 0, len(data) - 1)
if (result == -1):
    print("Elemento não encontrado!")
else:
    print("Elemento encontrado no índice: ", result)

print("Pesquisa Hash - HashTable")
ht = HashTable()
ht.insert("10", "Valor 1")
ht.insert("11", "Valor 2")
ht.insert("12", "Valor 3")
ht.insert("13", "Valor 4")
ht.insert("109", "Valor 5")
print(ht.buckets)
print(ht.find("d"))
