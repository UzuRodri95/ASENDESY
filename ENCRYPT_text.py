from argparse import ArgumentParser
import sys
from encriptador import Encriptador
import os

if __name__ == "__main__":
    #ARGUMENTS OPTIONS ARE ADDED
    parser = ArgumentParser(description='%(prog)s is an ArgumentParser demo')
    parser.add_argument('fichero', type=str, help='ayuda del fichero')
    parser.add_argument('password', type=str, help='contraseña')

    #INITIALIZE ARGUMENTS AND THE OBJECT ENCRYPT
    args = parser.parse_args()
    encrypt = Encriptador()

    #FILE THATS GONNA BE ENCRYPTED IS OPEN FOR BEING READ AND WE CREATE A NEW FILE FOR THE OUTPUT
    input = open(args.fichero,'r')
    output = open(args.fichero + ".cryp", "w")
    passw = args.password

    #TEXT IS ASSIGNED TO mensaje
    mensaje = input.read()

    #TEXT IS SPLITED BY " " AND ASSIGNED IN mensaje_split
    mensaje_split = mensaje.split()

    #TEXT IS ENCRYPTED BY THE FUNCTION OF Encriptador CLASS AND ASSIGNED TO texto_encriptado_split
    texto_encriptado_split = encrypt.encripto_texto(mensaje_split,passw)

    #TEXT IS JOINED BY " " AND ASSIGNED TO texto_encriptado
    texto_encriptado = " ".join(texto_encriptado_split)
    print(texto_encriptado)
    output.write(texto_encriptado)
    input.close()
    output.close()
