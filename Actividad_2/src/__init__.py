
#Funcion para filtrar lineas cuyas segunda palabra inicia con una vocal
def vowel_filter (text):
    vowels=('AEIOUaeiou')
    
    lines = text.split('\n')
    
    for line in lines:
        word=line.split()
        if len(word) > 1:
            second_word=word[1]
            if second_word[0] in(vowels):
                print(line)

