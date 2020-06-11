import random

class Encriptador:
    texto_encriptado=[]

    def proceso_password(self, password):
        valor = 0
        for letra in password:
            valor += ord(letra)
        return valor

    def encripto_palabra(self,palabra, password):
        palabra_encriptada=""
        for letra in palabra:
            valor = ord(letra) + password
            palabra_encriptada += chr(valor)
        return palabra_encriptada[::-1]

    def encripto_texto(self,texto,password):
        password_procesada = self.proceso_password(password)
        for palabra in texto:
            palabra = self.encripto_palabra(palabra, password_procesada)
            self.texto_encriptado.insert(0, palabra)
        return self.texto_encriptado
            
