def contar_palavras(frase):
    palavras = frase.strip().split()
    return len(palavras)
print(contar_palavras("Eu gosto de python."))