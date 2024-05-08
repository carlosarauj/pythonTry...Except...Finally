try:
    num = int(input("Digite um número: "))
    print(num)

except ZeroDivisionError:
    print("Divisão por zero impossível")
except ValueError:
    print("Digite um valor válido")
except:
    print("Erro inesperado")

finally:
    print("Finally")
#usa o terminal com: python nomedoarquivo.py