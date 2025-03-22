
#1 Función para filtrar lineas cuyas segunda palabra inicia con una vocal
def filtrar_2dapalabra_vocal(text):
    vocal=("AEIOUaeiou")
    lines= text.split('\n')
    for line in lines: 
        if len(line)>2:
            word=line.split(' ')
            if word[1][0] in vocal:
                print(line)


#2 Función Título más largo
def titulo_mas_largo(titulos):
    maximo=0
    titulo_max =[]
    for titulo in titulos:
        word=titulo.split(' ')
        largo=len(word)
        if largo==maximo:
            titulo_max.append(titulo)
        elif largo>maximo:
            maximo=largo
            titulo_max=[titulo]
    return titulo_max


#4 Función valida usuario
def validacion_usuario(usuario):
    #Inicializo variables
    cumple=False
    cant_minuscula=0
    cant_mayuscula=0
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
            #
            if cant_minuscula>=1  and cant_mayuscula>=1:
                cumple=True
            i=i+1
    if cumple:
           print("El nombre de usuario es válido.")
    else:
           print("El nombre de usuario no cumple con los requisitos.")

#