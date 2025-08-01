import customtkinter as ctk
from customtkinter import CTkLabel, CTkButton


## Funções

## Função que exclui cadastros

def excluir_cadastros():
    try:
        with open("arquivo-persistencia/cadastrar-usuario.txt", "w", encoding="utf-8") as arquivo:
            arquivo.write("")
        ctk.CTkMessagebox(title="Sucesso", message="Todos os cadastros foram excluídos com sucesso!", icon="check")
    except FileNotFoundError:
        ctk.CTkMessagebox(title="Erro", message="Nenhum arquivo encontrado para excluir.", icon="cancel")

## Função que grava arquivos no .txt

def gravar_arquivo(input_usuario_cadastrar, input_senha_cadastrar):
    usuario = input_usuario_cadastrar.get()
    senha = input_senha_cadastrar.get()

    with open("arquivo-persistencia/cadastrar-usuario.txt", "a", encoding="utf-8") as arquivo:
        conteudo = f"Usuário: {usuario} | Senha: {senha}\n"
        arquivo.write(conteudo)


## Verifica registros no sistema

def verificar_registros():
    verificar_usuarios = ctk.CTkToplevel()
    verificar_usuarios.geometry('600x300')
    verificar_usuarios.title('Verificar registros')
    verificar_usuarios.iconbitmap("icons/cadastro.ico")

    try:
        with open("arquivo-persistencia/cadastrar-usuario.txt", "r", encoding="utf-8") as arquivo:
            conteudo = arquivo.read()
    except FileNotFoundError:
        conteudo = "Nenhum cadastro encontrado."

    label_resultado = CTkLabel(
        verificar_usuarios,
        text=conteudo,
        font=("Arial", 14),
        wraplength=550,
        justify="left"
    )
    label_resultado.pack(padx=20, pady=20)


## Registra novos usuários no sistema

def registrar_usuario():
    cadastrar_usuario = ctk.CTkToplevel()
    cadastrar_usuario.geometry('600x300')
    cadastrar_usuario.title('Cadastrar usuário')
    cadastrar_usuario.iconbitmap("icons/cadastro.ico")

    label_cadastrar_usuario = CTkLabel(
        cadastrar_usuario,
        text='Cadastre aqui um novo usuário',
        font=("Arial", 16, "bold"))
    label_cadastrar_usuario.pack(pady=20)

    input_usuario_cadastrar = ctk.CTkEntry(
        cadastrar_usuario,
        placeholder_text='Digite o usuário',
        corner_radius=15,
        width=300,
        height=35,
        text_color='black'
    )
    input_usuario_cadastrar.pack(pady=5)

    input_senha_cadastrar = ctk.CTkEntry(
        cadastrar_usuario,
        placeholder_text='Digite a senha',
        corner_radius=15,
        width=300,
        height=35,
        text_color='black'
    )
    input_senha_cadastrar.pack(pady=5)

    button_registrar_usuario = CTkButton(
        cadastrar_usuario,
        width=200,
        height=35,
        fg_color='#3B82F6',
        text='Registrar Usuário',
        command=lambda: gravar_arquivo(input_usuario_cadastrar, input_senha_cadastrar)
    )
    button_registrar_usuario.pack(pady=10)


## Constrói janela principal da aplicação

def constroi_janela_principal():
    janela_principal = ctk.CTk()
    janela_principal.geometry('500x500')
    janela_principal.title('Janela Principal')
    janela_principal.iconbitmap("icons/cadastro.ico")

    frame_principal = ctk.CTkFrame(janela_principal, fg_color="transparent")
    frame_principal.place(relx=0.5, rely=0.5, anchor='center')

    label_apresentacao_janela_principal = CTkLabel(janela_principal, text='Seja bem-vindo(a) ao nosso sistema de cadastro!', font=("Arial", 16, "bold"))
    label_apresentacao_janela_principal.pack(pady=20)

    button_registrar_usuario = CTkButton(
        frame_principal,
        width=200,
        height=35,
        fg_color='#3B82F6',
        text='Registrar usuário',
        command=lambda: registrar_usuario()
    )
    button_registrar_usuario.pack(pady=10)

    button_verificar_usuarios_registrados = CTkButton(
        frame_principal,
        width=200,
        height=35,
        fg_color='#3B82F6',
        text='Verificar cadastros',
        command=lambda: verificar_registros()
    )
    button_verificar_usuarios_registrados.pack(pady=10)

    button_excluir_cadastros = CTkButton(
        frame_principal,
        width=200,
        height=35,
        fg_color='#3B82F6',
        text='Excluir cadastros',
        command=lambda: excluir_cadastros()
    )
    button_excluir_cadastros.pack(pady=10)

    button_sair_aplicativo = CTkButton(
        frame_principal,
        width=200,
        height=35,
        fg_color='#3B82F6',
        text='Sair do aplicativo',
        command=lambda: janela_principal.destroy()
    )
    button_sair_aplicativo.pack(pady=10)

    janela_principal.mainloop()



## Função que valida login

def validar_login():
    usuario_digitado = input_usuario.get()
    senha_digitada = input_senha.get()

    if usuario_digitado.strip() == '' or senha_digitada.strip() == '':
        label_mensagem_login.configure(text='Campos em branco, preencha-os!', text_color='#B71C1C')
    else:
        if usuario_digitado == 'testeapp' and senha_digitada == 'testeapp':
            login.destroy()
            constroi_janela_principal()
        else:
            label_mensagem_login.configure(text='Senha ou usuário incorreto(s)', text_color='#B71C1C')



## Parte do Login

if __name__ == '__main__':
    login = ctk.CTk()
    login.geometry('500x500')
    login.title('Cadastro de Usuários | Sistema de Login')
    login.iconbitmap("icons/cadastro.ico")

    frame_login = ctk.CTkFrame(login, fg_color="transparent")
    frame_login.place(relx=0.5, rely=0.5, anchor='center')

    label_usuario = ctk.CTkLabel(frame_login, text='Usuário', font=("Arial", 20, "bold"))
    label_usuario.pack(pady=5)

    input_usuario = ctk.CTkEntry(
        frame_login,
        placeholder_text='Digite seu usuário',
        corner_radius=15,
        width=300,
        height=35,
        text_color='black'
    )
    input_usuario.pack(pady=5)

    label_senha = ctk.CTkLabel(frame_login, text='Senha', font=("Arial", 20, "bold"))
    label_senha.pack(pady=5)

    input_senha = ctk.CTkEntry(
        frame_login,
        placeholder_text='Digite sua senha',
        corner_radius=15,
        width=300,
        height=35,
        text_color='black'
    )
    input_senha.pack(pady=5)

    button_confirmar_login = ctk.CTkButton(
        frame_login,
        width=300,
        height=35,
        fg_color='#3B82F6',
        text='Confirmar login',
        command=lambda: validar_login()
    )
    button_confirmar_login.pack(pady=16)

    button_sair_login = ctk.CTkButton(
        frame_login,
        width=300,
        height=35,
        text='Sair aplicação',
        fg_color='transparent',
        text_color='black',
        hover_color='#D3D3D3',
        command=lambda: login.destroy()
    )
    button_sair_login.pack(pady=10)


    label_mensagem_login = ctk.CTkLabel(frame_login, text='', font=("Arial", 15, "bold"))
    label_mensagem_login.pack(pady=7)

    login.mainloop()