from tkinter import *
from tkinter import messagebox
import string
import os

os.system('cls')
print("Sistema Rodando...")


#Busca o usuário fazendo a verificação se ele existe no sistema, se existe verifica a senha.
#Verifica se no login possui caracteres especiais ou não.

cadastros = [['admin', 'admin']]
def busca_usuario(login, senha):
    
    try:
        with open('cadastros.txt', 'r+', encoding= 'Utf-8') as arquivo:
            for linha in arquivo:
                linha = linha.strip(",")
                cadastros.append(linha.split())

            # print(cadastros)
            for cadastro in cadastros:
                login_registrado = cadastro[0]
                senha_registrada = cadastro[1]

                # print(login_registrado, senha_registrada)
                if login == login_registrado and senha == senha_registrada:
                    usuario_existe = True
                    break

                else:
                    usuario_existe = False

    except FileNotFoundError:
        messagebox.showinfo("Erro Arquivo não Encontrado", "O arquivo de cadastro não foi encontrado,\
                            favor contactar o adminstrador!")
    
    return usuario_existe
    

#Caracteres de A-Z e números de 0-9 e underline -> "_" 
CARACTERES_PERMITIDOS = string.ascii_letters + string.digits + "_"

def validar_login(login):
    for caractere in login:
        if caractere not in CARACTERES_PERMITIDOS:
            return False
    return True


#Captura o login e senha da interface de login, faz a verificação pela função busca_usuario e baseado no retorno ativa o evento. 
# No momento apenas avisa que conseguiu logar!
def logar():


    login = entry_login.get()
    senha = entry_senha.get()
    usuario = busca_usuario(login, senha)

    if usuario == True:
        messagebox.showinfo("Sucesso ao logar","Login realizado com sucesso")
    else:
        messagebox.showinfo("Usuário ou senha incorretos.","Você deve ter digitado seu nome de usuário ou senha errado\n\
                            Por favor, verifique.")


#Captura o liogn e senha da interface de registro, faz a verificação pela função busca_usuario e baseado no retorno aceita ao cadastro, 
#Recusa o cadastro por já existir aquele login e também verifica caracteres especiais
def janela_registrar():

    def registrar():

        login = entry_reg_login.get()
        senha = entry_reg_senha.get()
        usuario = busca_usuario(login, senha)

        if usuario == True:
            messagebox.showinfo("Usuário já existe.", "O usuário já existe. Por favor, utilize outro login!")
        else:
            with open('cadastros.txt', 'a+', encoding='Utf-8', newline='') as arquivo:
                arquivo.seek(0)

                cadastros = arquivo.readlines()
                logins_existentes = [cadastro.split()[0] for cadastro in cadastros]
                
                print(logins_existentes)

                if login in logins_existentes:
                    messagebox.showinfo("Usuário já existe.", "O usuário já existe. Por favor, utilize outro login!")
                else:
                    arquivo.writelines(f'{login} {senha}\n')
                    messagebox.showinfo("Cadastro Aprovado","Cadastro aprovado")


    #BASE TK
    janela_registro = Toplevel(janela)
    janela_registro.title("Registrar")
    janela_registro.resizable(width=FALSE, height=FALSE)


    #CENTRALIZAR JANELA REGISTRO
    largura_janela_reg = 275
    altura_janela_reg = 200
    largura_tela_reg = janela.winfo_screenwidth()
    altura_tela_reg = janela.winfo_screenheight()
    pos_x_reg = (largura_tela_reg - largura_janela_reg) // 2
    pos_y_reg = (altura_tela_reg - altura_janela_reg) // 2
    janela_registro.geometry(f'{largura_janela_reg}x{altura_janela_reg}+{pos_x_reg}+{pos_y_reg}')


    #TÍTULO
    label_reg_titulo = Label(janela_registro, width=35, height=2, bg='red', text='REGISTRO RESTRITO', fg='white', font='Arial 10 bold')
    label_reg_titulo.place(x=0, y=5)


    #LOGIN
    label_reg_login = Label(janela_registro, width=8, height=1, bg='black', text='Login', fg='white')
    label_reg_login.place(x=20, y=55)
    entry_reg_login = Entry(janela_registro, width=24, font='Arial 10 bold', bg='yellow' )
    entry_reg_login.place(x=90, y=55)


    #SENHA
    label_reg_senha = Label(janela_registro, width=8, height=1, bg='black', text='Senha', fg='white')
    label_reg_senha.place(x=20, y=90)
    entry_reg_senha = Entry(janela_registro, width=24, font='Arial 10 bold', bg='yellow', show='*')
    entry_reg_senha.place(x=90, y=90)


    #BOTÃO REGISTRAR
    botao_registrar = Button(janela_registro, width=7, font='Arial 10 bold', text='Registrar', command=registrar)
    botao_registrar.place(x=100, y=145)


#BASE TK
janela = Tk()
janela.title('Sistema de Login')
janela.resizable(width=FALSE, height=FALSE)


#CENTRALIZAR JANELA
largura_janela = 275
altura_janela = 200
largura_tela = janela.winfo_screenwidth()
altura_tela = janela.winfo_screenheight()
pos_x = (largura_tela - largura_janela) // 2
pos_y = (altura_tela - altura_janela) // 2
janela.geometry(f'{largura_janela}x{altura_janela}+{pos_x}+{pos_y}')


#TÍTULO
label_titulo = Label(janela, width=35, height=2, bg='red', text='ACESSO RESTRITO', fg='white', font='Arial 10 bold')
label_titulo.place(x=0, y=5)


#LOGIN
label_login = Label(janela, width=8, height=1, bg='black', text='Login', fg='white')
label_login.place(x=20, y=55)
entry_login = Entry(janela, width=24, font='Arial 10 bold', bg='yellow', )
entry_login.place(x=90, y=55)


#SENHA
label_senha = Label(janela, width=8, height=1, bg='black', text='Senha', fg='white')
label_senha.place(x=20, y=90)
entry_senha = Entry(janela, width=24, font='Arial 10 bold', bg='yellow', show='*')
entry_senha.place(x=90, y=90)


#BOTÃO REGISTRAR
botao_registrar_no_login = Button(janela, text="Registrar", font='Times 10 bold', command=janela_registrar, relief='flat', fg='blue', )
botao_registrar_no_login.place(x=20, y=150)


#BOTÃO ENTRAR
botao_entrar = Button(janela, width=5, font='Arial 13 bold', text='Entrar', command=logar)
botao_entrar.place(x=100, y=145)



janela.mainloop()