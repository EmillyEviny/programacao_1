def palindromo(palavra):
    palavra = palavra.lower()
    if palavra == palavra[::-1]:
        return True 
    return False

print(palindromo("arara")) 
print(palindromo("aranha"))