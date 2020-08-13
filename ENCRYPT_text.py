from argparse import ArgumentParser
from encriptador import Encriptador
import sys
import os
import pickle
import time

if __name__ == "__main__":
    #Argumentos para pasar por parametro
    parser = ArgumentParser(description='%(prog)s is an ArgumentParser demo')
    parser.add_argument('fichero', type=str, help='ayuda del fichero')
    parser.add_argument('password', type=str, help='contraseña')

    #Inicializamos el contenedor de los argumentos y el objeto de la clase Encriptador
    args = parser.parse_args()
    encrypt = Encriptador()

    print("\n\t", "#"*60)
    print("\t","#"*20," ENCRIPTADOR v1.1 ","#"*20)
    print("\t", "#"*60,"\n")

    input = open(args.fichero,'r')                                  #Fichero de entrada de texto normal
    ficheroOutput = open(args.fichero[0:-4] + ".cryp", "wb")        #Fichero de salida con el diccionario encriptado

    print("\tEL FICHERO", input.name, "VA A SER ENCRIPTADO")
    time.sleep(1)
    print("\n\tENCRIPTANDO")
    time.sleep(1)
    print("\t.")
    time.sleep(1)
    print("\t.")
    time.sleep(1)
    print("\t.")

    passw = args.password

    #Leemos el texto y lo separamos por espacios
    mensaje = input.read()
    mensaje_split = mensaje.split()

    diccionarioEncriptacion = encrypt.encripto_texto(mensaje_split,passw)

    pickle.dump(diccionarioEncriptacion, ficheroOutput)

    print("\tEL FICHERO", ficheroOutput.name, "HA SIDO CREADO CON EXITO")

    input.close()
    ficheroOutput.close()
