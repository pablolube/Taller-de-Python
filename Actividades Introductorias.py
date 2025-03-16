## Actividades introductorias

'''
1. Desarrolla un programa que solicite al usuario que ingrese su edad y luego calcule y muestre cuántos años le faltan para alcanzar los 100 años.
2. Haz un programa que pida al usuario que ingrese una temperatura en grados Celsius y luego convierta esa temperatura a grados Fahrenheit, mostrando el resultado.
3. Crea un programa que calcule la suma de los primeros 100 números naturales utilizando un bucle for.
4. Cree un programa que dada una lista de números imprima sólo los que son pares. Nota: utilice la sentencia `continue` donde haga falta.
5. Implementa un programa que solicite al usuario que ingrese una lista de números. Luego, imprime la lista pero detén la impresión si encuentras un número negativo. Nota: utilice la sentencia `break` cuando haga falta.
6. Modifique el ejercicio 4 para que dada la lista de número genere dos nuevas listas, una con los número pares y otras con los que son impares. Imprima las listas al terminar de procesarlas.
7. Escribe un programa que tome una lista de números enteros como entrada del usuario. Luego, convierte cada número en la lista a string y únelos en una sola cadena, separados por guiones ('-'). Sin embargo, excluye cualquier número que sea múltiplo de 3 de la cadena final.

# 1. Desarrolla un programa que solicite al usuario que ingrese su edad y luego calcule y muestre cuántos años le faltan para alcanzar los 100 años.

def vida_restante():
    edad = int(input("Ingrese su edad: "))
    print(f"Te faltan {100 - edad} años para llegar a los 100 años.")
vida_restante()

# 2. Haz un programa que pida al usuario que ingrese una temperatura en grados Celsius y luego convierta esa temperatura a grados Fahrenheit, mostrando el resultado.

def conversor_temperatura():
    Celsius = float(input("Ingrese su temperatura: "))
    fahrenheit = Celsius*9/5 + 32
    print(f"La temperatura en Fahrenheit es  de {fahrenheit} grados Fahrenheit ")
conversor_temperatura()

#3. Crea un programa que calcule la suma de los primeros 100 números naturales utilizando un bucle for.

def sumatoria_naturales():
    total=0
    for i in range (1,101):
        total +=i
    return total

total=sumatoria_naturales()
print(f"La suma de los primeros 100 números naturales es: {total}")

## 4. Cree un programa que dada una lista de números imprima sólo los que son pares. Nota: utilice la sentencia `continue` donde haga falta.
import random

def num_pares(lista):
    for i in lista:
        if  i % 2==0:
            print(i)
        else:
            continue


def lista_aleatoria(minimo, maximo, cantidad):
    lista = [random.randint(minimo, maximo) for k in range(cantidad)]
    return lista

# Ejemplo de uso
minimo = int(input("Ingrese el valor mínimo: "))
maximo = int(input("Ingrese el valor máximo: "))
cantidad = int(input("Ingrese la cantidad de números a generar: "))
lista=lista_aleatoria(minimo, maximo, cantidad)
num_pares(lista)

# 5. Implementa un programa que solicite al usuario que ingrese una lista de números. Luego, imprime la lista pero detén la impresión si encuentras un número negativo. Nota: utilice la sentencia `break` cuando haga falta.

def lista_numeros():
    lista = []
    while True:
        numero = input("Ingrese un número o ingrese 'stop' para terminar: ")
        
        # Verifica si la entrada es 'stop' para terminar el bucle
        if numero.lower() == "stop":
            break
        
        # Intenta convertir la entrada a un número
        else:
            numero = float(numero)
            lista.append(numero)
       
    return lista

lista = lista_numeros()

for i in lista:
    if i<0:
        break   
    else:
        print(i)

#6. Modifique el ejercicio 4 para que dada la lista de número genere dos nuevas listas, una con los número pares y otras con los que son impares. Imprima las listas al terminar de procesarlas.

import random

def par_impar(lista):
    lista_par = []
    lista_impar = []  
    for i in lista:
        if i % 2 == 0:
            lista_par.append(i)
        else:
            lista_impar.append(i)  # Aquí debes agregar a lista_impar los números impares
    return lista_par, lista_impar

def lista_aleatoria(minimo, maximo, cantidad):
    lista = [random.randint(minimo, maximo) for k in range(cantidad)]
    return lista

# Ejemplo de uso
minimo = int(input("Ingrese el valor mínimo: "))
maximo = int(input("Ingrese el valor máximo: "))
cantidad = int(input("Ingrese la cantidad de números a generar: "))
lista = lista_aleatoria(minimo, maximo, cantidad)

# Llamar a la función par_impar
lista_par, lista_impar = par_impar(lista)

# Imprimir los resultados
print(f"Lista de números pares: {lista_par}")
print(f"Lista de números impares: {lista_impar}")


'''
#7. Escribe un programa que tome una lista de números enteros como entrada del usuario. Luego, convierte cada número en la lista a string 
# #  únelos en una sola cadena, separados por guiones ('-'). Sin embargo, excluye cualquier número que sea múltiplo de 3 de la cadena final.

def lista_numeros():
    lista = []
    while True:
        numero = input('Ingrese un número o ingrese stop para terminar: ')
        
        # Verifica si la entrada es 'stop' para terminar el bucle
        if numero == 'stop':
            break
        
        # Intenta convertir la entrada a un número
        else:
            numero = int(numero)
            lista.append(numero)
    return lista


def convertir_string(lista):
#Convierte numeros string
    cadena=''
    for i in  lista:
        if  i %3 ==0:
            continue

        elif cadena:
            cadena+='-'
        cadena+=str(i)
    print(cadena)   
         
def convertir_string2(lista):
#Convierte numeros string
    cadena=''
    for i in  lista:
        if  i %3 ==0:
            continue
        else:
            cadena +=str(i)
    print(f'cadena 1 {cadena}')
    cadena='-'.join(cadena)    
    print(f'cadena 2 {cadena}')
  
#lista=lista_numeros()
lista=[3, 7, 12, 18, 25, 30, 41, 50, 60, 77]
convertir_string2(lista)        