import customtkinter as ctk

## Funções
## Constrói janela principal da aplicação

def constroi_janela_principal():
    janela_principal = ctk.CTk()
    janela_principal.geometry('500x500')
    janela_principal.title('Janela Principal')
    janela_principal.iconbitmap("icons/cadastro.ico")

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


    label_mensagem_login = ctk.CTkLabel(frame_login, text='', font=("Arial", 15, "bold"))
    label_mensagem_login.pack(pady=7)

    login.mainloop()