

def bubble_sort(lista):
    n = len(lista)
    for i in range(n-1):
        for i in range(n-1):
            if lista[i] > lista[i+1]:
                # troca de elementos nas posições i e i+1
                lista[i], lista[i+1] = lista[i+1], lista[i]


# Selection Sort
def selection_sort(lista):
    n = len(lista)
    for j in range(n-1):
        min_index = j
        for i in range(j, n):
            if lista[i] < lista[min_index]:
                min_index = i
        if lista[j] > lista[min_index]:
            aux = lista[j]
            lista[j] = lista[min_index]
            lista[min_index] = aux

# Quicksort
def quicksort(lista, inicio=0, fim=None):
    if fim is None:
        fim = len(lista)-1
    if inicio < fim:
        p = partition(lista, inicio, fim)
        quicksort(lista, inicio, p-1)
        quicksort(lista, p+1, fim)

def partition(lista, inicio, fim):
    pivot = lista[fim]
    i = inicio
    for j in range(inicio, fim):
        if lista[j] <= pivot:
            lista[j], lista[i] = lista[i], lista[j]
            i = i +1
    lista[i], lista[fim] = lista[fim], lista[i]
    return i
                  
