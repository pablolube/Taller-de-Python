
#Funcion para filtrar lineas cuyas segunda palabra inicia con una vocal
def filtrar_2dapalabra_vocal(text):
    vocal=("AEIOUaeiou")
    lines= text.split('\n')
    for line in lines: 
        if len(line)>2:
            word=line.split(' ')
            if word[1][0] in vocal:
                print(line)

