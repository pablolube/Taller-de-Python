#importo librerias 
import string
import random

#1 Función para filtrar lineas cuyas segunda palabra inicia con una vocal
def filtrar_2dapalabra_vocal(text):
    vocal=("AEIOUaeiou")
    lineas= text.split('\n')
    for linea in lineas: 
        if len(linea)>=2:
            palabra=linea.split(' ')
            if palabra[1][0] in vocal:
                print(linea)


#2 Función Título más largo
def titulo_mas_largo(titulos):
    maximo=0
    titulo_max =""
    for titulo in titulos:
        palabra=titulo.split(' ')
        largo=len(palabra)
        if  largo>=maximo:
            maximo=largo
            titulo_max=titulo
    return titulo_max

#3 Imprime reglas que cumplen con palabra
def buscar_regla(reglas,palabra):
    reglas=reglas.split('\n')
    for regla in reglas:
        if palabra.lower() in regla.lower():
            print(regla)

              
#4 Función valida usuario

def validacion_usuario(usuario):
    #Inicializo variables
    cumple=False
    cant_minuscula=0
    cant_mayuscula=0
    cant_numeros=0
    i=0
    
    #Valido que al menos tenga 5 caracteres 
    #Valido que sea alfanumerico y 
    if  len(usuario)>=5 and usuario.isalnum():
        while not cumple and i<len(usuario):
            char=usuario[i]
            #sumo si encuentra minuscula
            if char.isupper():
                cant_minuscula+=1
            #sumo si encuentra mayuscula
            if char.islower():
                    cant_mayuscula+=1
            if char.isdigit():
                cant_numeros+=1
                 
            if cant_minuscula>=1  and cant_mayuscula>=1 and cant_numeros>=1:
                cumple=True
            i=i+1
    if cumple:
           print("El nombre de usuario es válido.")
    else:
           print("El nombre de usuario no cumple con los requisitos.")


#5 Funcion de velocidad de reacción en un juego

def tiempo_reaccion(tiempo):
        if not tiempo.isdigit():
             print("No ha ingresado un numero, ingrese la veolicidad de reaccion en ms")
        tiempo=int(tiempo)
         
        if  tiempo <0 :
            print("Tiempo ingresado es menor a 0, vuelva a ingresar")
            return
        reaccion="" 
        #Menos de 200 ms: Rápido 
        if  0<= tiempo <200:
            reaccion="Rápido"

        #Entre 200 y 500 ms: Normal
        elif 200<=tiempo<=500:      
            reaccion="Normal"

        #Más de 500 ms: Lento
        else:
             reaccion="Lento"
               
        print (f"categoria: {reaccion}")

#6 Análisis de descripciones de una plataforma de stream

def cuenta_palabras(texto):
    palabras_buscar=["música","charla","entretenimiento"]
    contador={"música":0,"charla":0,"entretenimiento":0}

    for line in texto:
        palabras = line.lower().split()
        for palabra_buscar in palabras_buscar:
            if palabra_buscar.lower() in palabras:
                contador[palabra_buscar]+=1
    # Imprimir las menciones
    for palabra_buscar, cantidad in contador.items():
        print(f"Menciones de '{palabra_buscar}': {cantidad}")

#7 Generador de códigos de descuento

def codigo_descuento(usuario,fecha):
    if len(usuario)<=15:
       
        usuario=usuario.upper()
        fecha=str(fecha).replace("-","")
        
        codigo=usuario+"-"+fecha

        caracteres=string.ascii_uppercase + string.digits

        restantes=30-len(codigo)
        
        codigo += "-" + ''.join(random.choices(caracteres, k=restantes))
        print(codigo)       
    else: 
        print("El usuario supera los 15 caracteres")


# 8. Identificación de anagrama
def son_anagramas(palabra1, palabra2):
    
    if sorted(palabra1) == sorted(palabra2):
        print("Son anagramas")
    else:
        print("No son anagramas")

#9. Limpieza de Datos para un Sistema de Clientes
def elimino_nulos(lista):
    #Elimino elementos nulos
        lista =[elemento for elemento in lista if elemento not in [None, "", " "]]
        return lista
    
def elimino_blancos(lista):
    #Elimino espacios en blanco al inicio y final
        lista =[elemento.strip() for elemento in lista]
        #Elimino espacios en blanco en el medio
        lista =[elemento.replace("  "," ") for elemento in lista]
        return lista
        
    

    #Capitalizo primera letra
def capitalizo_palabras(lista):
        lista=[elemento.title() for elemento in lista]
        return lista

def elimino_repetidos(lista):
    #Elimino repetidos
        lista_sin_repetidos=[]
        for elemento in lista:
            if elemento not in lista_sin_repetidos:
                lista_sin_repetidos.append(elemento)
        return lista_sin_repetidos

def limpieza_nombres(nombres):
        nombres=elimino_nulos(nombres)
        nombres=elimino_blancos(nombres)
        nombres=capitalizo_palabras(nombres)
        nombres=elimino_repetidos(nombres)
        return nombres
#10  Limpieza de Datos para un Sistema de Clientes
def inicializo(tabla_general,jugador):
    if jugador not in tabla_general:
        tabla_general[jugador]={'kills': 0, 'assists': 0, 'deaths': 0,'MVPs':0,'Puntajes':0}
    return tabla_general


def calculo_puntaje(ronda_datos, jugador, puntos):
    ronda_datos[jugador]['Puntajes'] = (ronda_datos[jugador]['kills'] * puntos['kills'] +
                                        ronda_datos[jugador]['assists'] * puntos['assists'] +
                                        int(ronda_datos[jugador]['deaths']) * puntos['deaths'])
    return ronda_datos[jugador]


def calcula_max_ronda(ronda_datos,jugador,max_ronda,jugador_mvp):
    if ronda_datos[jugador]['Puntajes']>max_ronda:
       max_ronda=ronda_datos[jugador]['Puntajes']
       jugador_mvp=jugador
    return jugador_mvp,max_ronda

def acumulo_ronda(tabla_general, jugador, rdo_jugador_ronda):
    tabla_general[jugador]['kills'] += rdo_jugador_ronda[jugador]['kills']
    tabla_general[jugador]['assists'] += rdo_jugador_ronda[jugador]['assists']
    tabla_general[jugador]['deaths'] += int(rdo_jugador_ronda[jugador]['deaths'])
    tabla_general[jugador]['Puntajes'] += rdo_jugador_ronda[jugador]['Puntajes']
    return tabla_general

#PROCESO RONDA
def procesar_ronda(ronda_datos, tabla_general,puntos):
    max_ronda=0
    jugador_mvp=""
    for jugador in  ronda_datos:

        #Inicializo la tabla general si el jugador es nuevo
        inicializo(tabla_general,jugador)

        #Calculo puntaje 
        calculo_puntaje(ronda_datos,jugador,puntos)

        #Guarda si es el max puntaje ronda       
        jugador_mvp,max_ronda=calcula_max_ronda(ronda_datos,jugador,max_ronda,jugador_mvp)
        

        #Acumulo resultados de ronda a la tabla géneral
        acumulo_ronda(tabla_general,jugador,ronda_datos)
        
        #inicializo mvp de la ronda
        ronda_datos[jugador]['MVPs'] = 0
             
       
    if jugador_mvp:
        ronda_datos[jugador_mvp]['MVPs'] = 1 
        tabla_general[jugador_mvp]['MVPs'] += 1
    
    
    return tabla_general

def imprimir_tabla(tabla):
    print("{:<10} {:<7} {:<7} {:<7} {:<7} {:<10}".format("Jugador", "Kills", "Asists", "Deaths", "MVPs", "Puntajes"))
    print("-" * 50)
    
    tabla_ordenada = sorted(tabla.items(), key=lambda x: x[1]['Puntajes'], reverse=True)

    for jugador, stats in tabla_ordenada:
        print("{:<10} {:<7} {:<7} {:<7} {:<7} {:<10}".format(
            jugador,
            stats['kills'],
            stats['assists'],
            stats['deaths'],
            stats['MVPs'],
            stats['Puntajes']
        ))
    print("\n")
    