class Aluno:
    def __init__(self, nome, ra, rm):
        self.nome = nome
        self.ra = ra
        self.rm = rm

    def __str__(self):
        return f"{self.nome} - Matrícula: {self.rm}, RA: {self.ra}."
