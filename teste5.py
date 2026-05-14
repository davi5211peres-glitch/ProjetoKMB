def cifra_cesar(texto, deslocamento):
    resultado = ""
    for i in range(len(texto)):
        char = texto[i]
        
        # Criptografar maiúsculas
        if char.isupper():
            resultado += chr((ord(char) + deslocamento - 65) % 26 + 65)
        # Criptografar minúsculas
        elif char.islower():
            resultado += chr((ord(char) + deslocamento - 97) % 26 + 97)
        else:
            resultado += char
    return resultado

mensagem = "Peres"
chave = 3
mensagem_cifrada = cifra_cesar(mensagem, chave)
print(f"Original: {mensagem}")
print(f"Cifrada: {mensagem_cifrada}") 