#imagine que você tenha um programa com mais de 1000 linhas e tenha que fazer algum cálculo:
#pense em uma funcionalidade mais complexa e que de repente você precisa repetir essa funcionalidade varias vezes
#por isso existe a funcionalidade de definir funções


#def: define uma função a uma variável
#variável(): chama a função para executá-la


#e se você quiser usar a função para qualquer par de números?
#existe a possibilidade de PASSAR INFORMAÇÕES para a função e ela vai trabalhar com elas.
#os parametros vão dentro da definição da variável
def soma(num1,num2):
    soma1= num1
    soma2= num2
    soma_total= soma1+soma2
    print(soma_total)

def sub(num1,num2):
    sub1= num1
    sub2= num2
    sub_total= sub1-sub2
    print(sub_total)

def mult(num1,num2):
    mult1=num1
    mult2=num2
    mult_total=mult1*mult2
    print(mult_total)

def div(num1,num2):
    div1=num1
    div2=num2
    div_total=div1/div2
    print(div_total)

soma(5,3) #isso são os argumentos, os valores que você dá aos parâmetros
soma(4.5,5)
soma(10,10000)

sub(20,5)
sub(10,50)

mult(10,5)
mult(5,5)

div(10,2)
div(45,9)
