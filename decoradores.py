def valida_entrada(func):
    def validar(*args, **kwargs):
        print('validando...')

        new_args = []
        for arg in args:
            if isinstance(arg,int):
                new_args.append(arg) 
            elif isinstance(arg,str) and arg.isdigit():
                new_args.append(int(arg))
            else:
                new_args.append(0)

        resultado = func(*new_args, **kwargs)

        print('O resultado é: ', resultado)

        return resultado

    return validar

@valida_entrada
def somar(n1,n2,n3=0,n4=0,n5=0):
    print('somando...')
    return n1 + n2 + n3 + n4 + n5

@valida_entrada
def subtrair(n1,n2):
    print('subtraindo...')
    return int(n1) - int(n2)

@valida_entrada
def multiplicar(n1,n2):
    print('multiplicando...')
    return int(n1) * int(n2)

@valida_entrada
def dividir(n1,n2):
    print('dividindo...')
    return int(n1) / int(n2)

"""
def somar(n1,n2):
    print('somando...')

    if isinstance(n1,str) and n1.isdigit():
        n1 = int(n1)
    else:
        n1 = 0

    if isinstance(n2,str) and n2.isdigit():
        n2 = int(n2)
    else:
        n2 = 0

    return int(n1) + int(n2)

def subtrair(n1,n2):
    print('subtraindo...')
    if isinstance(n1,str) and n1.isdigit():
        n1 = int(n1)
    else:
        n1 = 0

    if isinstance(n2,str) and n2.isdigit():
        n2 = int(n2)
    else:
        n2 = 0
        
    return int(n1) - int(n2)
"""

print(somar('1 aa','6aaaa', 3, 6, '5'))
print(subtrair(1,6))
