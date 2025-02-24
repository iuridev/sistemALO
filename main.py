import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk  # Importe Image e ImageTk do Pillow
from CadastroAluno import CadastroAluno
from CadastroProfessor import CadastroProfessor


class InterfacePrincipal:
    def __init__(self, root):
        self.root = root
        self.root.title(
            "Sistema de Gerenciamento Interno - EE PEI ALEXANDRE LOPES OLIVEIRA")

        # Carregar e redimensionar a imagem do logo
        try:
            imagem_pil = Image.open("logo.png")  # Abre a imagem com Pillow
            largura_desejada = 150  # Defina a largura desejada
            altura_desejada = 100  # Defina a altura desejada
            imagem_redimensionada = imagem_pil.resize(
                # Redimensiona a imagem
                (largura_desejada, altura_desejada), Image.Resampling.LANCZOS)
            self.logo_img = ImageTk.PhotoImage(
                imagem_redimensionada)  # Converte para PhotoImage
            logo_label = ttk.Label(root, image=self.logo_img)
            logo_label.pack(pady=6)  # Adiciona espaço abaixo do logo
        except FileNotFoundError:
            print("Erro: Imagem do logo não encontrada.")
        except Exception as e:
            print(f"Erro ao carregar ou redimensionar imagem: {e}")

        # Estilo ttk
        style = ttk.Style()
        style.configure("TButton", padding=10, font=('Arial', 12))

        # Frames para organizar os botões
        frame_botoes = ttk.Frame(root, padding="20 10 20 10")
        frame_botoes.pack(fill=tk.BOTH, expand=True)

        # Botões com layout grid
        botoes = [
            ("Cadastrar Aluno", self.abrir_cadastro_aluno),
            ("Cadastrar Professor", self.abrir_cadastro_professor),
            ("Cadastrar Eletiva", self.abrir_cadastro_eletiva),
            ("Cadastrar Clube", self.abrir_cadastro_clube),
            ("Cadastrar Turma", self.abrir_cadastro_turma),
            ("Pesquisar Aluno", self.abrir_pesquisa_aluno),
            ("Lista do Tutor", self.abrir_lista_tutor),
            ("Lista da Eletiva", self.abrir_lista_eletiva),
            ("Lista do Clube", self.abrir_lista_clube),
        ]

        for i, (texto, comando) in enumerate(botoes):
            btn = ttk.Button(frame_botoes, text=texto, command=comando)
            btn.grid(row=i // 3, column=i % 3, padx=5, pady=5, sticky="ew")

        # Configurar peso das colunas para expandir os botões
        for i in range(3):
            frame_botoes.columnconfigure(i, weight=1)

    # Métodos para abrir as outras interfaces
    def abrir_cadastro_aluno(self):
        nova_janela = tk.Toplevel(self.root)
        app_cadastro = CadastroAluno(nova_janela)

    def abrir_cadastro_professor(self):
        nova_janela = tk.Toplevel(self.root)
        app_cadastro = CadastroProfessor(nova_janela)

    def abrir_cadastro_eletiva(self):
        nova_janela = tk.Toplevel(self.root)
        nova_janela.title("Cadastro de Eletiva")
        label = ttk.Label(nova_janela, text="Interface de Cadastro de Eletiva")
        label.pack(padx=20, pady=20)

    def abrir_cadastro_clube(self):
        nova_janela = tk.Toplevel(self.root)
        nova_janela.title("Cadastro de Clube")
        label = ttk.Label(nova_janela, text="Interface de Cadastro de Clube")
        label.pack(padx=20, pady=20)

    def abrir_cadastro_turma(self):
        nova_janela = tk.Toplevel(self.root)
        nova_janela.title("Cadastro de Turma")
        label = ttk.Label(nova_janela, text="Interface de Cadastro de Turma")
        label.pack(padx=20, pady=20)

    def abrir_pesquisa_aluno(self):
        nova_janela = tk.Toplevel(self.root)
        nova_janela.title("Pesquisar Aluno")
        label = ttk.Label(nova_janela, text="Interface de Pesquisa de Aluno")
        label.pack(padx=20, pady=20)

    def abrir_lista_tutor(self):
        nova_janela = tk.Toplevel(self.root)
        nova_janela.title("Lista de Tutores")
        label = ttk.Label(nova_janela, text="Interface de Lista de Tutores")
        label.pack(padx=20, pady=20)

    def abrir_lista_eletiva(self):
        nova_janela = tk.Toplevel(self.root)
        nova_janela.title("Lista de Eletivas")
        label = ttk.Label(nova_janela, text="Interface de Lista de Eletivas")
        label.pack(padx=20, pady=20)

    def abrir_lista_clube(self):
        nova_janela = tk.Toplevel(self.root)
        nova_janela.title("Lista de Clubes")
        label = ttk.Label(nova_janela, text="Interface de Lista de Clubes")
        label.pack(padx=20, pady=20)


if __name__ == "__main__":
    root = tk.Tk()
    app = InterfacePrincipal(root)
    root.mainloop()
