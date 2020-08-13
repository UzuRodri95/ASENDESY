import random

class Desencriptador:
    texto_desencriptado=[]

    def proceso_password(self, password):
        valor = 0
        for letra in password:
            valor += ord(letra)
        return valor

    def desencripto_palabra(self,palabra, password):
        palabra_desencriptada=""
        for letra in palabra:
            valor = ord(letra) - password
            palabra_desencriptada += chr(valor)
        return palabra_desencriptada[::-1]

    def desencripto_diccionario(self,dicEncriptado,password):
        password_procesada = self.proceso_password(password)
        palabras_encriptadas = dicEncriptado.keys()

        for palabra in palabras_encriptadas:
            posiciones = dicEncriptado.get(palabra)
            palabra = self.desencripto_palabra(palabra, password_procesada)
            for posicion in posiciones:
                    self.texto_desencriptado.insert(posicion, palabra)
        return self.texto_desencriptado
