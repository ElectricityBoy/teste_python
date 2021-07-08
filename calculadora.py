def soma(x,y):
    return x+y
    
def sub(x,y):
    return x-y

def main():
    x=10
    y=20
    resultado1 = soma(x,y)
    resultado2 = sub(x,y)
    resultado3 = mult(x,y)

    print(f'Resultados {resultado1} , {resultado2}, {resultado3}')

def mult(x,y):
    return x*y
    
main()
