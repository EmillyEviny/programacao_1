def vogais (palavra):
    palavra = palavra.lower()
    v = ["a","e","i","o","u"]
    cont = 0
    for letra in palavra:
        if letra in v:
            cont += 1
    return cont
print(vogais("python"))
print(vogais("Emilly"))