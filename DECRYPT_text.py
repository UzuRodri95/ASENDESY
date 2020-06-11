from argparse import ArgumentParser
import sys
from desencriptador import Desencriptador
import os

if __name__ == "__main__":
    #ARGUMENTS OPTIONS ARE ADDED
    parser = ArgumentParser(description='%(prog)s is an ArgumentParser demo')
    parser.add_argument('fichero', type=str, help='ayuda del fichero')
    parser.add_argument('password', type=str, help='contraseña')

    #INITIALIZE ARGUMENTS AND THE OBJECT ENCRYPT
    args = parser.parse_args()
    decrypt = Desencriptador()

    #FILE THATS GONNA BE ENCRYPTED IS OPEN FOR BEING READ AND WE CREATE A NEW FILE FOR THE OUTPUT
    input = open(args.fichero,'r')
    if args.fichero.endswith(".cryp"):
        output = open(args.fichero + ".decryp", "w")
        passw = args.password

        #TEXT IS ASSIGNED TO mensaje
        mensaje = input.read()

        #TEXT IS SPLITED BY " " AND ASSIGNED IN mensaje_split
        mensaje_split = mensaje.split()

        #TEXT IS ENCRYPTED BY THE FUNCTION OF Encriptador CLASS AND ASSIGNED TO texto_encriptado_split
        texto_desencriptado_split = decrypt.desencripto_texto(mensaje_split,passw)

        #TEXT IS JOINED BY " " AND ASSIGNED TO texto_encriptado
        texto_desencriptado = " ".join(texto_desencriptado_split)
        output.write(texto_desencriptado)
        output.close()
    else:
        print("Error in file format, must be .cryp")
        input.close()
    