def soma(x, y):
    return x+y; #retorna a soma de x por y
def subtracao(x, y):
    return x-y; #retorna a subtração de x por y
def divisao(x, y):
    print("modulo da divisão(resto): ", x%y); #mostra na tela o resto da divisao de x por y
    return x/y #retorna a divisao de x por y
def multiplicacao (x, y):
    return x*y; #retorna a multiplicação de x por y

op = True;
while op != False:

    escolha = input("Escolha a operação desejada.: '+' , '-' , '*' , '/' DIGITE 0 OU SAIR PARA ENCERRAR O PROGRAMA: ");
    num1 = int(input("Entre com o primeiro numero: " ));
    num2 = int(input("Entre com o segundo numero: " ));
    if escolha == "+":
        print(soma(num1, num2));
    elif escolha == "-":
        print(subtracao(num1, num2));
    elif escolha == "*":
        print(multiplicacao(num1, num2));
    elif escolha == "/":
        print(divisao(num1, num2));
    elif escolha == 0 or escolha == "sair" or escolha ==  "Sair" or escolha == "SAIR":
        print("PROGRAMA FINALIZADO")
        op = False;
