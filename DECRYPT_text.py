from argparse import ArgumentParser
from desencriptador import Desencriptador
import sys
import os
import pickle

if __name__ == "__main__":
    #ARGUMENTS OPTIONS ARE ADDED
    parser = ArgumentParser(description='%(prog)s is an ArgumentParser demo')
    parser.add_argument('fichero', type=str, help='ayuda del fichero')
    parser.add_argument('password', type=str, help='contraseña')

    #INITIALIZE ARGUMENTS AND THE OBJECT ENCRYPT
    args = parser.parse_args()
    decrypt = Desencriptador()

    #FILE THATS GONNA BE ENCRYPTED IS OPEN FOR BEING READ AND WE CREATE A NEW FILE FOR THE OUTPUT

    if args.fichero.endswith(".cryp"):
        #Cargamos el fichero en input y sacamos de el el diccionario
        input = open(args.fichero,'rb')
        dicEncriptado = pickle.load(input)

        #print(contenidoFichero)
        #Creamos el fichero donde se va a desencriptar el archivo.
        outputFichero = open(args.fichero[0:-5] + "_DECRYPTED" + ".txt", "w")
        passw = args.password

        textoDesencriptado = decrypt.desencripto_diccionario(dicEncriptado, passw)
        textoDesencriptado = " ".join(textoDesencriptado)
        outputFichero.write(textoDesencriptado)

        input.close()
        outputFichero.close()
    else:
        print("Error in file format, must be .cryp")
