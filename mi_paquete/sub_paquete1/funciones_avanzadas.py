def contar_letras(frase):
    numero_letras = 0
    for l in frase:
        if l != ' ':
            numero_letras += 1
    return numero_letras
