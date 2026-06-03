from utils import *

class Aluno:
    def __init__(self, nome, nota1, nota2):
        self.nome = nome
        self.nota1 = nota1
        self.nota2 = nota2
        
    def media(self):
        media = (self.nota1 + self.nota2) / 2
        return media
    
    def aprovado(self):
        media = self.media()
        if media >= 6:
            print("APROVADO!")
        else:
            print("REPROVADO!")
    
    def __str__(self):
        return f"{self.nome} | Nota 1: {self.nota1} | Nota 2: {self.nota2}"