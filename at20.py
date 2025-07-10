def intercalar_listas(lista1, lista2):
    result = [] 
    for i in range(len(lista1)):
        result.append(lista1[i])  
        result.append(lista2[i])
    return result
print(intercalar_listas([1, 2, 3], ["a", "b", "c"]))