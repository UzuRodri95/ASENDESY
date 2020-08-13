import random


class Encriptador:
    texto_encriptado=[]
    dicPalabras = {}
    contadorPosiciones = 0

    #Codifico la propia contraseña sumando el valor ASCII de cada una de las letras de la contraseña
    def proceso_password(self, password):
        valor = 0
        for letra in password:
            valor += ord(letra)
        return valor

    #Codifico letra a letra y cuando tengo la palabra codificada la devuelvo de derecha a izquierda
    def encripto_palabra(self,palabra, password):
        palabra_encriptada=""
        for letra in palabra:
            valor = ord(letra) + password
            palabra_encriptada += chr(valor)

        return palabra_encriptada[::-1]

    def encripto_texto(self,texto,password):
        #Encriptamos la palabra
        password_procesada = self.proceso_password(password)
        for palabra in texto:
            #Sacamos la palabra encriptada y la metemos en la variable palabra
            palabra = self.encripto_palabra(palabra, password_procesada)

            #Comprobamos si la palabra encriptada esta en el diccionario dicPalabras
            if self.dicPalabras.get(palabra) == None:
                self.dicPalabras[palabra] = [self.contadorPosiciones]
            else:
                #Podemos codificar el numero de la posicion y meterlo como un string el valor de las posiciones
                aux = self.dicPalabras.get(palabra)
                aux.append(self.contadorPosiciones)
                self.dicPalabras[palabra] = aux

            self.contadorPosiciones += 1

        return self.dicPalabras
