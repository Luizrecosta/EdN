# 1 - Programa de Saudação
def saudacao():
    nome = input("Digite o nome: ")

    print(f"Saudação, recruta {nome}")
# 2 - Calculadora de Soma
def soma():
    a = float(input("a: "))
    b = float(input("b: "))

    x = a + b

    print(f"Resultado: {x} ")
# 3 - Calculadora de Volume
def volume():
    altura, largura, comprimento = map(float, input("Insira a altura, largura e comprimento separados por espaço: ").split())

    print(f"O volume eh: {altura*largura*comprimento}")
# 4 - Calculadora de Preço Total

def PrecoTotal():
    valor = 0
    soma = 0
    while True:
        print(f"Valor Total: {soma}")
        preco,quantidade = map(float, input("Digite o valor do produto e sua quantidade respectivamente separados por espaço: ").split())
        
        if(preco < 0):
            break
        soma +=preco*quantidade
        
    print(f"Preco Total: R$ {soma}")
    
    
    
    
saudacao()
soma()
volume()
PrecoTotal()