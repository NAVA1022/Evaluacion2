#Juan Jose Navarrete Garibay    18420470
#Evaluacion Numero 2
import json


def metodo_Municipio(municipio):
    CPDATOSDICC = {}
    try:
        Archivo_cadena = open("CPdescarga.txt")
        lista = Archivo_cadena.readlines()

    except FileNotFoundError:
        print("Archivo no encontrado")
    else:
        for cp1 in lista[2:]:
            cod_post = {}
            cp = cp1.split('|')
            if cp[3] == municipio:
                # print("Calis para ver por que no entra")
                cod_post["Codigo Postal"] = cp[0]
                cod_post["Tipo de asentamiento"] = cp[2]
                cod_post["Zona"] = cp[13]
                CPDATOSDICC[cp[0]] = cod_post
        jsontext = json.dumps(CPDATOSDICC, indent=4)
        print(jsontext)

def codigos_postales_Municipio(municipio):
    arreglo=[]
    

#Metodo que recibe un estado y genera un archivo json con los Codigos postales y el nombre del municipio
def metodo_Estado(estado):
    CPDATOSDICC = {}
    try:
        Archivo_cadena = open("CPdescarga.txt")
        lista = Archivo_cadena.readlines()

    except FileNotFoundError:
        print("Archivo no encontrado")
    else:
        for cp1 in lista[2:]:
            cod_post = {}
            cp = cp1.split('|')
            if cp[4] == estado:
                cod_post["Municipio"] = cp[3]
                cod_post["Codigo Postal"] = cp[0]
                CPDATOSDICC[cp[0]] = cod_post
        jsontext2 = json.dumps(CPDATOSDICC, indent=4)
        print(jsontext2)
        with open("Archivo_JSON", 'w') as archivo:
            json.dump(CPDATOSDICC, archivo, indent=4)


metodo_Municipio("Jiquilpan")
metodo_Estado("Michoacán de Ocampo")