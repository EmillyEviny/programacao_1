def analisa_lista(lista):
    maior = max(lista)
    menor = min(lista)
    media = sum(lista) / len(lista)
    return maior, menor, media

print(analisa_lista([10, 20, 30]))