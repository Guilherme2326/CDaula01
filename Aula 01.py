import datetime #para contar tempo de execução do codigo
import math

def computar( fim, inicio =1): #definindo uma função
    pos = inicio 
    while pos < fim:
        pos += 1
        math.sqrt((pos - 1000000) * (pos - 1000000)) #operação matematica

def main(): #função principal
    inicio = datetime.datetime.now() #guarda a data inicial
    fim=5000000
    computar(fim)
    tempo = datetime.datetime.now() - inicio #subtrai a data atual da data inicial
    print(f"Terminou em{tempo.total_seconds():.2f} segundos.")
            
if __name__ == '__main__':
    main()
        