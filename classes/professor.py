class professor:
    def __init__(self, nome, rg, cpf, diciplinas):
        self.nome = nome
        self.rg = rg
        self.cpf = cpf
        self.diciplinas = diciplinas

    def __str__(self):
        return f"{self.nome} - RG: {self.rg}, CPF: {self.cpf}, Diciplinas: {', '.join(str(d) for d in self.diciplinas)}."
