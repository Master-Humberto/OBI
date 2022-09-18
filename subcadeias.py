def eh_palindromo(s):
    boleano = False
    for i in range(0,len(s)):
        if s[i] == s[-i-1]:
            boleano = True
        else:
            boleano = False
            break
    return boleano
def subcadeias(s):
    lista = []
    for i in range(0, len(s)):
        for j in range(0,len(s)):
            lista.append(s[i:j+1])

    return lista

palavra = input()
lista = subcadeias(palavra)
maior = 0 
for i in range(0,len(lista)):
    if eh_palindromo(lista[i]) and len(lista[i]) > maior : 
        maior = len(lista[i])
print(maior)
    



