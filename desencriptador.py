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

    def desencripto_texto(self,texto,password):
        password_procesada = self.proceso_password(password)
        for palabra in texto:
            palabra = self.desencripto_palabra(palabra, password_procesada)
            self.texto_desencriptado.insert(0, palabra)
        return self.texto_desencriptado