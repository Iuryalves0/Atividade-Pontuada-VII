import os

# Função sem retorno.
def logoSenai():
    os.system("cls || clear")
    print("=== SENAI === ")

# Função para classificar o IMC
def classificar_imc(imc):
    if imc < 18.5:
        return "Abaixo do peso"
    elif 18.5 <= imc < 25:
        return "Peso normal"
    elif 25 <= imc < 30:
        return "Sobrepeso"
    elif 30 <= imc < 35:
        return "Obesidade grau I"
    elif 35 <= imc < 40:
        return "Obesidade grau II"
    else:
        return "Obesidade grau III (mórbida)"

#função pedir dados
def pedir_dados():
       
    idade = int(input("Digite a idade do usuário: "))
    altura = float(input("Digite a altura do usuário (em metros): "))
    peso = float(input("Digite o peso do usuário (em quilogramas): "))
    

    return idade, altura, peso

#adicionar dados as listas
def adicionar():
    idade, altura, peso = pedir_dados()
    nomes.append(nome)
    sobrenomes.append(sobrenome)
    idades.append(idade)
    alturas.append(altura)
    pesos.append(peso)

# Definindo listas vazias para armazenar os dados dos usuários
nomes = []
sobrenomes = []
idades = []
alturas = []
pesos = []

# Solicitando os dados dos usuários em um loop
while True:
    logoSenai()
    nome = input("Digite o nome do usuário (ou digite 'sair' para encerrar): ")
    
    #verificando se o usuario quer sair
    if nome.lower() == 'sair':
        break
    
    sobrenome = input("Digite o sobrenome do usuário: ")

    # Adicionando os dados às listas
    adicionar()

# Exibindo os dados armazenados
logoSenai()
print("\nDados dos usuários:")
for i in range(len(nomes)):
    print(f"\nUsuário {i+1}:")
    print("Nome:", nomes[i], sobrenomes[i])
    print("Idade:", idades[i])
    print("Altura:", alturas[i], "metros")
    print("Peso:", pesos[i], "quilogramas")

    # Calculando o IMC
    imc = pesos[i] / (alturas[i] ** 2)
    
    # Classificando o IMC
    classificacao = classificar_imc(imc)

    # Exibindo IMC e classificação
    print(f"IMC: {imc:.2f} - Classificação: {classificacao}")
    print()