def senha_segura(senha):
    if len(senha) < 8:
        return False

    maiuscula = False
    minuscula = False
    num = False

    for caractere in senha:
        if caractere.isupper():
            maiuscula = True
        elif caractere.islower():
            minuscula = True
        elif caractere.isdigit():
            num = True

    if maiuscula and minuscula and num:
        return True
    else:
        return False
dados = input("Digite uma senha: ")

if senha_segura(dados):
    print("True")
else:
    print("False")
