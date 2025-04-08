import sys
import os
import csv

def leer_archivo(ruta_archivo):
    with open(ruta_archivo, encoding='utf-8') as archivo_csv:
        reader = csv.reader(archivo_csv, delimiter=";")
        return list(reader)



def procesar_archivos(ruta, tipo="hogar"):
    datos_unificados = []
    cabecera = None

    for nombre_archivo in os.listdir(ruta):
        if tipo in nombre_archivo and nombre_archivo.endswith(".txt"):
            ruta_archivo = os.path.join(ruta, nombre_archivo)
            filas = leer_archivo(ruta_archivo)

            if not filas:
                continue

            if cabecera is None:
                cabecera = filas[0]
                datos_unificados.extend(filas[1:]) 
            else:
                if filas[0] == cabecera:
                    datos_unificados.extend(filas[1:])
                else:
                    print(f"⚠️ Cabecera diferente en: {nombre_archivo}")

    return [cabecera] + datos_unificados

def guardar_en_csv(datos, ruta_destino, nombre_archivo="hogares_unificados.csv"):
    # Crear la ruta completa del archivo
    ruta_completa = os.path.join(ruta_destino, nombre_archivo)

    # Asegurarse de que la carpeta de destino exista (solo la carpeta, no el archivo)
    os.makedirs(ruta_destino, exist_ok=True)

    # Guardar los datos en el archivo CSV
    with open(ruta_completa, mode='w', encoding='utf-8', newline='') as archivo_csv:
        writer = csv.writer(archivo_csv, delimiter=";")
        writer.writerows(datos)
    
    print(f"✅ Archivo CSV guardado en: {ruta_completa}")
